from app.models.domain import LearningTask, TaskStatus
from app.services.evidence import create_evidence_from_task, judge_evidence_strength
from app.services.gap_analyzer import analyze_gap
from app.services.job_parser import parse_job_description
from app.services.resume_parser import parse_resume_text


def test_gap_analyzer_finds_missing_and_weak_evidence_skills():
    resume = "熟悉 LangChain、FastAPI、Docker。项目中使用 LangChain 和 FastAPI 构建 RAG 服务。"
    jd = """
    AI 应用开发工程师
    必备要求：LangChain、FastAPI、LangGraph、Qdrant、Agent Evaluation。
    加分项：Docker、Rerank、RAGAS。
    """

    report = analyze_gap(parse_resume_text(resume), parse_job_description(jd))

    assert report.match_score < 100
    assert {"LangChain", "FastAPI"}.issubset(set(report.strengths))
    assert {"LangGraph", "Qdrant", "Agent Evaluation"}.issubset(set(report.missing_core_skills))
    assert "Docker" in report.weak_evidence_skills
    assert report.learning_priorities[0].priority == "high"
    assert "缺少" in report.learning_priorities[0].reason


def test_gap_analyzer_outputs_evidence_aware_skill_gap_details():
    resume = "熟悉 LangChain、FastAPI、Docker。项目中使用 LangChain 和 FastAPI 构建 RAG 服务。"
    jd = """
    AI 应用开发工程师
    必备要求：LangChain、FastAPI、LangGraph、Qdrant、Agent Evaluation。
    加分项：Docker、Rerank、RAGAS。
    """

    report = analyze_gap(parse_resume_text(resume), parse_job_description(jd))
    gaps = {item.skill: item for item in report.skill_gaps}

    assert gaps["LangChain"].status == "verified"
    assert gaps["LangChain"].requirement_type == "core"
    assert gaps["LangChain"].priority == "low"
    assert gaps["LangChain"].evidence is not None

    assert gaps["Docker"].status == "weak_evidence"
    assert gaps["Docker"].requirement_type == "bonus"
    assert gaps["Docker"].priority == "medium"
    assert "可验证产出" in gaps["Docker"].reason

    assert gaps["LangGraph"].status == "missing"
    assert gaps["LangGraph"].requirement_type == "core"
    assert gaps["LangGraph"].priority == "high"
    assert gaps["LangGraph"].suggested_task_title == "完成 LangGraph 项目化练习"
    assert "demo" in gaps["LangGraph"].suggested_deliverable.lower()


def test_evidence_strength_requires_artifact_links():
    assert judge_evidence_strength({"github": "https://github.com/demo/repo", "demo": ""}) == "medium"
    assert judge_evidence_strength({"github": "https://github.com/demo/repo", "demo": "https://demo.example.com"}) == "strong"
    assert judge_evidence_strength({}) == "weak"


def test_done_task_can_be_converted_to_career_evidence():
    task = LearningTask(
        id="task_001",
        title="实现 LangGraph Resume Parser",
        status=TaskStatus.done,
        deliverable="FastAPI 接口 + LangGraph 节点 + 示例输出",
        skills=["LangGraph", "FastAPI", "Pydantic"],
        completion_notes="完成接口、README 和示例响应。",
        artifacts={"github": "https://github.com/demo/cv2offer-agent"},
    )

    evidence = create_evidence_from_task(task)

    assert evidence.source_task_id == "task_001"
    assert evidence.title == "实现 LangGraph Resume Parser"
    assert evidence.evidence_strength == "medium"
    assert "LangGraph" in evidence.resume_bullets[0]
