from uuid import uuid4

from app.models.domain import CareerEvidence, EvidenceTrace, JobProfile, ResumeProfile, TailoredResumeDraft


def assemble_tailored_resume(
    resume: ResumeProfile,
    job: JobProfile,
    evidence_items: list[CareerEvidence],
) -> TailoredResumeDraft:
    target_skills = list(dict.fromkeys([*job.core_skills, *job.bonus_skills]))
    evidence_trace = [_trace_evidence(item, target_skills) for item in evidence_items]
    supported_skills = {
        skill
        for trace in evidence_trace
        for skill in trace.matched_skills
    }
    resume_skills = {skill.name for skill in resume.skills}
    unsupported_claims = [skill for skill in job.core_skills if skill not in supported_skills]
    highlighted_skills = [skill for skill in target_skills if skill in resume_skills or skill in supported_skills]

    markdown = _build_markdown(
        resume=resume,
        job=job,
        highlighted_skills=highlighted_skills,
        evidence_items=evidence_items,
        unsupported_claims=unsupported_claims,
    )

    return TailoredResumeDraft(
        id=f"draft_{uuid4().hex[:8]}",
        target_role=job.target_role,
        markdown=markdown,
        evidence_trace=[trace for trace in evidence_trace if trace.matched_skills],
        unsupported_claims=unsupported_claims,
    )


def _trace_evidence(evidence: CareerEvidence, target_skills: list[str]) -> EvidenceTrace:
    matched_skills = [skill for skill in target_skills if skill in evidence.skills]
    return EvidenceTrace(
        evidence_id=evidence.id,
        title=evidence.title,
        matched_skills=matched_skills,
        artifacts=evidence.artifacts,
    )


def _build_markdown(
    *,
    resume: ResumeProfile,
    job: JobProfile,
    highlighted_skills: list[str],
    evidence_items: list[CareerEvidence],
    unsupported_claims: list[str],
) -> str:
    name = str(resume.basics.get("name") or resume.basics.get("姓名") or "候选人")
    lines = [
        "## 定向简历草稿",
        "",
        f"### {name} - {job.target_role}",
        "",
        "### 目标岗位关键词",
        ", ".join(highlighted_skills) if highlighted_skills else "暂无可验证关键词",
        "",
        "### 项目与职业证据",
    ]

    bullets = [bullet for item in evidence_items for bullet in item.resume_bullets]
    if bullets:
        lines.extend([f"- {bullet}" for bullet in bullets])
    else:
        lines.append("- 暂无可验证 evidence，请先完成任务或手动录入证据。")

    lines.extend(["", "### Evidence Trace"])
    for item in evidence_items:
        matched = ", ".join(skill for skill in item.skills if skill in [*job.core_skills, *job.bonus_skills])
        lines.append(f"- {item.title}: {matched or '未命中 JD 技能'}")

    lines.extend(["", "### Unsupported Claims"])
    if unsupported_claims:
        lines.extend([f"- {skill}" for skill in unsupported_claims])
    else:
        lines.append("- 暂无")

    return "\n".join(lines)
