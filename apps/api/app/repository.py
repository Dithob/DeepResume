from app.models.domain import CareerEvidence, GapReport, JobProfile, LearningPlan, LearningTask, ResumeProfile


class MemoryRepository:
    def __init__(self) -> None:
        self.resumes: dict[str, ResumeProfile] = {}
        self.jobs: dict[str, JobProfile] = {}
        self.gap_reports: dict[str, GapReport] = {}
        self.plans: dict[str, LearningPlan] = {}
        self.tasks: dict[str, LearningTask] = {}
        self.evidence: dict[str, CareerEvidence] = {}

    def save_plan(self, plan: LearningPlan) -> LearningPlan:
        self.plans[plan.id] = plan
        for milestone in plan.milestones:
            for task in milestone.tasks:
                self.tasks[task.id] = task
        return plan


repository = MemoryRepository()
