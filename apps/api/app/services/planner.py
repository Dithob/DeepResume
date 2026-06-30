from uuid import uuid4

from app.models.domain import GapReport, LearningMilestone, LearningPlan, LearningTask


def generate_learning_plan(report: GapReport, weekly_hours: int, duration_weeks: int) -> LearningPlan:
    priorities = report.learning_priorities
    milestones: list[LearningMilestone] = []

    for week in range(1, duration_weeks + 1):
        priority = priorities[(week - 1) % len(priorities)] if priorities else None
        if priority:
            title = priority.suggested_task_title or f"完成 {priority.skill} 项目化练习"
            deliverable = priority.suggested_deliverable or f"{priority.skill} demo、README 和关键设计说明"
            estimated_hours = min(float(weekly_hours), max(1.0, priority.estimated_hours))
            goal = f"补齐 {priority.skill}：{priority.reason}"
            skills = [priority.skill]
        else:
            title = "复盘已有项目证据"
            deliverable = "项目追问清单、指标口径、简历 bullet 草稿"
            estimated_hours = min(float(weekly_hours), 3.0)
            goal = "巩固已有项目证据"
            skills = []

        task = LearningTask(
            id=f"task_{uuid4().hex[:8]}",
            title=title,
            estimated_hours=estimated_hours,
            deliverable=deliverable,
            skills=skills,
        )
        milestones.append(LearningMilestone(week=week, goal=goal, tasks=[task]))

    return LearningPlan(
        id=f"plan_{uuid4().hex[:8]}",
        title="CV-JD 差距驱动学习计划",
        duration_weeks=duration_weeks,
        weekly_hours=weekly_hours,
        milestones=milestones,
    )
