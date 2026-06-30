from enum import StrEnum
from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field


class TaskStatus(StrEnum):
    todo = "todo"
    doing = "doing"
    blocked = "blocked"
    done = "done"


class EvidenceStrength(StrEnum):
    weak = "weak"
    medium = "medium"
    strong = "strong"


class EvidenceType(StrEnum):
    project = "project"
    work = "work"
    learning = "learning"
    certificate = "certificate"


class ResumeSkill(BaseModel):
    name: str
    category: str = "general"
    evidence: str | None = None
    confidence: float = 0.7
    evidence_strength: EvidenceStrength = EvidenceStrength.weak


class ResumeProfile(BaseModel):
    id: str = ""
    basics: dict[str, Any] = Field(default_factory=dict)
    skills: list[ResumeSkill] = Field(default_factory=list)
    projects: list[dict[str, Any]] = Field(default_factory=list)
    work_experience: list[dict[str, Any]] = Field(default_factory=list)
    education: list[dict[str, Any]] = Field(default_factory=list)
    raw_text: str = ""


class JobProfile(BaseModel):
    id: str = ""
    target_role: str
    core_skills: list[str] = Field(default_factory=list)
    bonus_skills: list[str] = Field(default_factory=list)
    responsibilities: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)
    weights: dict[str, float] = Field(default_factory=dict)
    raw_text: str = ""


class LearningPriority(BaseModel):
    skill: str
    priority: str
    reason: str
    suggested_task_title: str | None = None
    suggested_deliverable: str | None = None
    estimated_hours: float = 3


class TaskCheckIn(BaseModel):
    id: str
    note: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class SkillGapDetail(BaseModel):
    skill: str
    requirement_type: str
    status: str
    priority: str
    reason: str
    evidence: str | None = None
    evidence_strength: EvidenceStrength | None = None
    suggested_task_title: str
    suggested_deliverable: str
    estimated_hours: float = 3


class GapReport(BaseModel):
    id: str = ""
    resume_id: str | None = None
    job_id: str | None = None
    match_score: int
    strengths: list[str] = Field(default_factory=list)
    missing_core_skills: list[str] = Field(default_factory=list)
    weak_evidence_skills: list[str] = Field(default_factory=list)
    skill_gaps: list[SkillGapDetail] = Field(default_factory=list)
    learning_priorities: list[LearningPriority] = Field(default_factory=list)
    metrics: dict[str, float] = Field(default_factory=dict)


class LearningTask(BaseModel):
    id: str
    title: str
    status: TaskStatus = TaskStatus.todo
    estimated_hours: float = 2
    actual_hours: float | None = None
    deliverable: str
    skills: list[str] = Field(default_factory=list)
    completion_notes: str | None = None
    artifacts: dict[str, str] = Field(default_factory=dict)
    check_ins: list[TaskCheckIn] = Field(default_factory=list)


class LearningMilestone(BaseModel):
    week: int
    goal: str
    tasks: list[LearningTask] = Field(default_factory=list)


class LearningPlan(BaseModel):
    id: str = ""
    title: str
    duration_weeks: int
    weekly_hours: int
    milestones: list[LearningMilestone] = Field(default_factory=list)


class CareerEvidence(BaseModel):
    id: str = ""
    title: str
    type: EvidenceType = EvidenceType.learning
    skills: list[str] = Field(default_factory=list)
    artifacts: dict[str, str] = Field(default_factory=dict)
    source_task_id: str | None = None
    verified: bool = False
    evidence_strength: EvidenceStrength = EvidenceStrength.weak
    resume_bullets: list[str] = Field(default_factory=list)


class EvidenceTrace(BaseModel):
    evidence_id: str
    title: str
    matched_skills: list[str] = Field(default_factory=list)
    artifacts: dict[str, str] = Field(default_factory=dict)


class TailoredResumeDraft(BaseModel):
    id: str = ""
    target_role: str
    markdown: str
    evidence_trace: list[EvidenceTrace] = Field(default_factory=list)
    unsupported_claims: list[str] = Field(default_factory=list)
