from uuid import uuid4

from app.models.domain import CareerEvidence, EvidenceStrength, LearningTask, TaskStatus


def judge_evidence_strength(artifacts: dict[str, str]) -> EvidenceStrength:
    filled_links = [value for value in artifacts.values() if value and value.startswith(("http://", "https://"))]
    if len(filled_links) >= 2:
        return EvidenceStrength.strong
    if len(filled_links) == 1:
        return EvidenceStrength.medium
    return EvidenceStrength.weak


def create_evidence_from_task(task: LearningTask) -> CareerEvidence:
    if task.status != TaskStatus.done:
        raise ValueError("Only done tasks can be converted to career evidence.")
    strength = judge_evidence_strength(task.artifacts)
    skills = "、".join(task.skills) if task.skills else "相关技术"
    bullet = f"围绕 {skills} 完成「{task.title}」，交付 {task.deliverable}，形成可验证学习产出。"
    return CareerEvidence(
        id=f"evidence_{uuid4().hex[:8]}",
        title=task.title,
        skills=task.skills,
        artifacts=task.artifacts,
        source_task_id=task.id,
        verified=strength != EvidenceStrength.weak,
        evidence_strength=strength,
        resume_bullets=[bullet],
    )
