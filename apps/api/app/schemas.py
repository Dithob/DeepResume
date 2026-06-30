from app.models.domain import EvidenceType, TaskStatus
from pydantic import BaseModel, Field


class ParseResumeRequest(BaseModel):
    resume_text: str = Field(min_length=1)


class ParseJobRequest(BaseModel):
    jd_text: str = Field(min_length=1)


class AnalyzeGapRequest(BaseModel):
    resume_id: str
    job_id: str


class GeneratePlanRequest(BaseModel):
    gap_report_id: str
    weekly_hours: int = Field(default=8, ge=1, le=80)
    duration_weeks: int = Field(default=4, ge=1, le=24)


class ImportPlanRequest(BaseModel):
    markdown: str = Field(min_length=1)
    weekly_hours: int = Field(default=8, ge=1, le=80)


class UpdateTaskRequest(BaseModel):
    status: TaskStatus | None = None
    actual_hours: float | None = Field(default=None, ge=0)
    check_in: str | None = Field(default=None, min_length=1)
    completion_notes: str | None = None
    artifacts: dict[str, str] | None = None


class CreateEvidenceRequest(BaseModel):
    source_task_id: str | None = None
    title: str | None = None
    type: EvidenceType = EvidenceType.learning
    skills: list[str] = []
    artifacts: dict[str, str] = {}
    resume_bullets: list[str] = []


class AssembleResumeRequest(BaseModel):
    resume_id: str
    job_id: str
    evidence_ids: list[str] = []
