from uuid import uuid4

from app.models.domain import (
    EvidenceStrength,
    GapReport,
    JobProfile,
    LearningPriority,
    ResumeProfile,
    SkillGapDetail,
)


def analyze_gap(resume: ResumeProfile, job: JobProfile) -> GapReport:
    resume_skills = {skill.name: skill for skill in resume.skills}
    core_skills = job.core_skills
    all_job_skills = list(dict.fromkeys([*job.core_skills, *job.bonus_skills]))

    skill_gaps = [_build_skill_gap(skill, resume_skills, job) for skill in all_job_skills]

    strengths = [gap.skill for gap in skill_gaps if gap.status == "verified"]
    missing_core = [gap.skill for gap in skill_gaps if gap.requirement_type == "core" and gap.status == "missing"]
    weak_evidence = [gap.skill for gap in skill_gaps if gap.status == "weak_evidence"]

    core_coverage = _ratio(len([skill for skill in core_skills if skill in resume_skills]), len(core_skills))
    evidence_coverage = _ratio(len(strengths), len(all_job_skills))
    keyword_coverage = _ratio(len([keyword for keyword in job.keywords if keyword in resume.raw_text]), len(job.keywords))
    responsibility_match = _ratio(len([item for item in job.responsibilities if item and item in resume.raw_text]), len(job.responsibilities))
    resume_quality = min(1.0, len(resume.skills) / 8)
    score = round(
        100
        * (
            0.35 * core_coverage
            + 0.25 * evidence_coverage
            + 0.20 * responsibility_match
            + 0.10 * keyword_coverage
            + 0.10 * resume_quality
        )
    )

    priorities = [
        LearningPriority(
            skill=gap.skill,
            priority=gap.priority,
            reason=gap.reason,
            suggested_task_title=gap.suggested_task_title,
            suggested_deliverable=gap.suggested_deliverable,
            estimated_hours=gap.estimated_hours,
        )
        for gap in skill_gaps
        if gap.priority in {"high", "medium"}
    ]

    return GapReport(
        id=f"gap_{uuid4().hex[:8]}",
        resume_id=resume.id or None,
        job_id=job.id or None,
        match_score=max(0, min(100, score)),
        strengths=strengths,
        missing_core_skills=missing_core,
        weak_evidence_skills=weak_evidence,
        skill_gaps=skill_gaps,
        learning_priorities=priorities,
        metrics={
            "core_skill_coverage": core_coverage,
            "evidence_coverage": evidence_coverage,
            "responsibility_match": responsibility_match,
            "keyword_coverage": keyword_coverage,
            "resume_quality": resume_quality,
        },
    )


def _build_skill_gap(skill: str, resume_skills: dict, job: JobProfile) -> SkillGapDetail:
    requirement_type = "core" if skill in job.core_skills else "bonus"
    resume_skill = resume_skills.get(skill)
    task_title, deliverable, estimated_hours = _suggested_task(skill, requirement_type)

    if resume_skill is None:
        priority = "high" if requirement_type == "core" else "medium"
        return SkillGapDetail(
            skill=skill,
            requirement_type=requirement_type,
            status="missing",
            priority=priority,
            reason=f"目标 JD 的{_requirement_label(requirement_type)}要求包含 {skill}，当前简历缺少该技能和项目证据。",
            evidence=None,
            evidence_strength=None,
            suggested_task_title=task_title,
            suggested_deliverable=deliverable,
            estimated_hours=estimated_hours,
        )

    if resume_skill.evidence_strength == EvidenceStrength.weak:
        return SkillGapDetail(
            skill=skill,
            requirement_type=requirement_type,
            status="weak_evidence",
            priority="medium",
            reason=f"{skill} 已在简历中出现，但缺少项目、链接或可验证产出支撑。",
            evidence=resume_skill.evidence,
            evidence_strength=resume_skill.evidence_strength,
            suggested_task_title=task_title,
            suggested_deliverable=deliverable,
            estimated_hours=estimated_hours,
        )

    return SkillGapDetail(
        skill=skill,
        requirement_type=requirement_type,
        status="verified",
        priority="low",
        reason=f"{skill} 已有简历证据，可作为当前优势继续保留。",
        evidence=resume_skill.evidence,
        evidence_strength=resume_skill.evidence_strength,
        suggested_task_title=f"复盘并强化 {skill} 项目表达",
        suggested_deliverable=f"{skill} 面试追问清单、指标口径和简历 bullet",
        estimated_hours=1.5,
    )


def _suggested_task(skill: str, requirement_type: str) -> tuple[str, str, float]:
    task_map = {
        "LangGraph": (
            "完成 LangGraph 项目化练习",
            "可运行 multi-node agent demo、README、状态流转图",
            4,
        ),
        "Qdrant": (
            "为 RAG demo 接入 Qdrant",
            "Qdrant collection、检索接口、召回样例和 README",
            3,
        ),
        "Agent Evaluation": (
            "补齐 Agent Evaluation 评估闭环",
            "10 条测试集、成功率指标、失败案例复盘表",
            3,
        ),
        "Rerank": (
            "实现 Rerank 精排对比实验",
            "baseline vs rerank 对比表、Hit Rate 或 MRR 指标",
            3,
        ),
        "RAGAS": (
            "补齐 RAGAS 评估报告",
            "RAGAS 指标输出、bad case 分析、优化建议",
            2.5,
        ),
    }
    if skill in task_map:
        return task_map[skill]
    return (
        f"完成 {skill} 项目化练习",
        f"{skill} demo、README、关键设计说明和可验证产出链接",
        3 if requirement_type == "core" else 2,
    )


def _requirement_label(requirement_type: str) -> str:
    return "核心技能" if requirement_type == "core" else "加分项"


def _ratio(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 1.0
    return numerator / denominator
