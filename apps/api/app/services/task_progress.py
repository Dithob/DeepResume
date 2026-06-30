from uuid import uuid4

from app.models.domain import LearningTask, TaskCheckIn, TaskStatus
from app.schemas import UpdateTaskRequest


def update_learning_task(task: LearningTask, request: UpdateTaskRequest) -> LearningTask:
    update_data = request.model_dump(exclude_unset=True, exclude={"check_in"})
    merged_artifacts = _merge_artifacts(task.artifacts, request.artifacts)
    if request.artifacts is not None:
        update_data["artifacts"] = merged_artifacts

    check_ins = list(task.check_ins)
    if request.check_in:
        check_ins.append(TaskCheckIn(id=f"checkin_{uuid4().hex[:8]}", note=request.check_in.strip()))
    update_data["check_ins"] = check_ins

    updated = task.model_copy(update=update_data)
    _validate_completion(updated)
    return updated


def _merge_artifacts(current: dict[str, str], incoming: dict[str, str] | None) -> dict[str, str]:
    if incoming is None:
        return current
    merged = dict(current)
    for key, value in incoming.items():
        normalized_key = key.strip()
        if normalized_key:
            merged[normalized_key] = value.strip()
    return merged


def _validate_completion(task: LearningTask) -> None:
    if task.status != TaskStatus.done:
        return

    has_completion_notes = bool(task.completion_notes and task.completion_notes.strip())
    has_artifact = any(value.strip() for value in task.artifacts.values())
    if not has_completion_notes and not has_artifact:
        raise ValueError("Completion requires completion_notes or at least one artifact.")
