import re
from uuid import uuid4

from app.models.domain import LearningMilestone, LearningPlan, LearningTask
from app.services.skills import extract_known_skills


def import_learning_plan_markdown(markdown: str, weekly_hours: int = 8) -> LearningPlan:
    title = _extract_title(markdown)
    milestones: list[LearningMilestone] = []
    duration_weeks = 1

    for row in _extract_table_rows(markdown):
        if len(row) < 5 or _is_header_row(row):
            continue

        phase, time_text, goal, content, deliverable = row[:5]
        week_start, week_end = _parse_week_range(time_text)
        duration_weeks = max(duration_weeks, week_end)
        milestones.extend(
            _expand_row_to_weekly_milestones(
                phase=phase,
                goal=goal,
                content=content,
                deliverable=deliverable,
                week_start=week_start,
                week_end=week_end,
                weekly_hours=weekly_hours,
            )
        )

    if not milestones:
        milestones = _fallback_heading_plan(markdown, weekly_hours)
        duration_weeks = max((milestone.week for milestone in milestones), default=1)

    return LearningPlan(
        title=title,
        duration_weeks=duration_weeks,
        weekly_hours=weekly_hours,
        milestones=sorted(milestones, key=lambda milestone: milestone.week),
    )


def _expand_row_to_weekly_milestones(
    *,
    phase: str,
    goal: str,
    content: str,
    deliverable: str,
    week_start: int,
    week_end: int,
    weekly_hours: int,
) -> list[LearningMilestone]:
    weeks = list(range(week_start, week_end + 1))
    total_weeks = len(weeks)
    skills = extract_known_skills(content)
    milestones: list[LearningMilestone] = []

    for index, week in enumerate(weeks, start=1):
        suffix = f"（{index}/{total_weeks}）" if total_weeks > 1 else ""
        task = LearningTask(
            id=f"task_{uuid4().hex[:8]}",
            title=f"{phase}{suffix}：{goal}",
            estimated_hours=max(1, weekly_hours / total_weeks),
            deliverable=deliverable,
            skills=skills,
        )
        milestones.append(
            LearningMilestone(
                week=week,
                goal=f"{goal}{suffix}",
                tasks=[task],
            )
        )

    return milestones


def _extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped.removeprefix("# ").strip()
    return "Imported Learning Plan"


def _extract_table_rows(markdown: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        rows.append(cells)
    return rows


def _is_header_row(row: list[str]) -> bool:
    normalized = [cell.strip().lower() for cell in row]
    return "阶段" in normalized or "时间" in normalized or "目标" in normalized


def _parse_week_range(text: str) -> tuple[int, int]:
    numbers = [int(number) for number in re.findall(r"\d+", text)]
    if not numbers:
        return 1, 1
    if len(numbers) == 1:
        return numbers[0], numbers[0]
    start, end = numbers[0], numbers[1]
    if end < start:
        return end, start
    return start, end


def _fallback_heading_plan(markdown: str, weekly_hours: int) -> list[LearningMilestone]:
    headings = [line.lstrip("#").strip() for line in markdown.splitlines() if line.startswith("## ")]
    milestones: list[LearningMilestone] = []
    for index, heading in enumerate(headings[:4], start=1):
        milestones.append(
            LearningMilestone(
                week=index,
                goal=heading,
                tasks=[
                    LearningTask(
                        id=f"task_{uuid4().hex[:8]}",
                        title=f"整理并完成：{heading}",
                        estimated_hours=weekly_hours,
                        deliverable=f"{heading} 学习笔记与复盘",
                        skills=extract_known_skills(heading),
                    )
                ],
            )
        )
    return milestones
