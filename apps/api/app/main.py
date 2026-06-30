from uuid import uuid4

from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.models.domain import CareerEvidence, EvidenceStrength
from app.repository import repository
from app.schemas import (
    AnalyzeGapRequest,
    AssembleResumeRequest,
    CreateEvidenceRequest,
    GeneratePlanRequest,
    ImportPlanRequest,
    ParseJobRequest,
    ParseResumeRequest,
    UpdateTaskRequest,
)
from app.services.evidence import create_evidence_from_task, judge_evidence_strength
from app.services.gap_analyzer import analyze_gap
from app.services.job_parser import parse_job_description
from app.services.learning_plan_parser import import_learning_plan_markdown
from app.services.planner import generate_learning_plan
from app.services.resume_parser import parse_resume_text
from app.services.resume_assembler import assemble_tailored_resume
from app.services.task_progress import update_learning_task


app = FastAPI(title="CV2Offer Agent API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/resumes/parse")
def parse_resume(request: ParseResumeRequest):
    profile = parse_resume_text(request.resume_text)
    profile.id = f"resume_{uuid4().hex[:8]}"
    repository.resumes[profile.id] = profile
    return profile


@app.post("/api/resumes/parse-file")
async def parse_resume_file(file: UploadFile = File(...)):
    content = await file.read()
    try:
        resume_text = _decode_text_file(content)
    except UnicodeDecodeError as exc:
        raise HTTPException(status_code=400, detail="Only UTF-8 or GBK text/Markdown files are supported in MVP.") from exc
    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="Uploaded resume file is empty.")
    profile = parse_resume_text(resume_text)
    profile.id = f"resume_{uuid4().hex[:8]}"
    repository.resumes[profile.id] = profile
    return profile


@app.get("/api/resumes")
def list_resumes():
    return list(repository.resumes.values())


@app.post("/api/resumes/assemble")
def assemble_resume(request: AssembleResumeRequest):
    resume = repository.resumes.get(request.resume_id)
    job = repository.jobs.get(request.job_id)
    if resume is None or job is None:
        raise HTTPException(status_code=404, detail="Resume or job not found.")
    evidence_items = [
        item
        for item in repository.evidence.values()
        if not request.evidence_ids or item.id in request.evidence_ids
    ]
    return assemble_tailored_resume(resume, job, evidence_items)


@app.post("/api/jobs/parse")
def parse_job(request: ParseJobRequest):
    job = parse_job_description(request.jd_text)
    job.id = f"job_{uuid4().hex[:8]}"
    repository.jobs[job.id] = job
    return job


@app.get("/api/jobs")
def list_jobs():
    return list(repository.jobs.values())


@app.post("/api/gap/analyze")
def analyze(request: AnalyzeGapRequest):
    resume = repository.resumes.get(request.resume_id)
    job = repository.jobs.get(request.job_id)
    if resume is None or job is None:
        raise HTTPException(status_code=404, detail="Resume or job not found.")
    report = analyze_gap(resume, job)
    repository.gap_reports[report.id] = report
    return report


@app.post("/api/plans/generate")
def generate_plan(request: GeneratePlanRequest):
    report = repository.gap_reports.get(request.gap_report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Gap report not found.")
    plan = generate_learning_plan(report, request.weekly_hours, request.duration_weeks)
    return repository.save_plan(plan)


@app.post("/api/plans/import")
def import_plan(request: ImportPlanRequest):
    plan = import_learning_plan_markdown(request.markdown, request.weekly_hours)
    plan.id = f"plan_{uuid4().hex[:8]}"
    return repository.save_plan(plan)


@app.get("/api/plans")
def list_plans():
    return list(repository.plans.values())


@app.get("/api/plans/{plan_id}")
def get_plan(plan_id: str):
    plan = repository.plans.get(plan_id)
    if plan is None:
        raise HTTPException(status_code=404, detail="Plan not found.")
    return plan


@app.patch("/api/tasks/{task_id}")
def update_task(task_id: str, request: UpdateTaskRequest):
    task = repository.tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found.")
    try:
        updated = update_learning_task(task, request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    repository.tasks[task_id] = updated
    for plan in repository.plans.values():
        for milestone in plan.milestones:
            milestone.tasks = [updated if item.id == task_id else item for item in milestone.tasks]
    return updated


@app.post("/api/evidence")
def create_evidence(request: CreateEvidenceRequest):
    if request.source_task_id and not request.title:
        task = repository.tasks.get(request.source_task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found.")
        try:
            evidence = create_evidence_from_task(task)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
    else:
        if not request.title:
            raise HTTPException(status_code=400, detail="title is required for manual evidence.")
        strength = judge_evidence_strength(request.artifacts)
        evidence = CareerEvidence(
            id=f"evidence_{uuid4().hex[:8]}",
            title=request.title,
            type=request.type,
            skills=request.skills,
            artifacts=request.artifacts,
            source_task_id=request.source_task_id,
            verified=strength != EvidenceStrength.weak,
            evidence_strength=strength,
            resume_bullets=request.resume_bullets
            or [f"围绕 {'、'.join(request.skills) or '目标岗位能力'} 形成「{request.title}」职业证据。"],
        )
    repository.evidence[evidence.id] = evidence
    return evidence


@app.get("/api/evidence")
def list_evidence(
    skill: str | None = Query(default=None),
    strength: EvidenceStrength | None = Query(default=None),
    source_task_id: str | None = Query(default=None),
    has_link: bool | None = Query(default=None),
):
    items = list(repository.evidence.values())
    if skill:
        items = [item for item in items if skill in item.skills]
    if strength:
        items = [item for item in items if item.evidence_strength == strength]
    if source_task_id:
        items = [item for item in items if item.source_task_id == source_task_id]
    if has_link is not None:
        items = [item for item in items if _evidence_has_link(item.artifacts) is has_link]
    return items


def _decode_text_file(content: bytes) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gbk"):
        try:
            return content.decode(encoding)
        except UnicodeDecodeError:
            continue
    return content.decode("utf-8")


def _evidence_has_link(artifacts: dict[str, str]) -> bool:
    return any(value.startswith(("http://", "https://")) for value in artifacts.values() if value)
