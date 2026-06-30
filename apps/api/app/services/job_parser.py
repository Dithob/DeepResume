import re

from app.models.domain import JobProfile
from app.services.skills import extract_known_skills


def parse_job_description(jd_text: str) -> JobProfile:
    lines = [line.strip() for line in jd_text.splitlines() if line.strip()]
    target_role = _extract_role(lines)
    core_text = _collect_section_text(
        lines,
        start_markers=["岗位要求", "任职要求", "职位要求", "任职资格", "必备要求", "要求"],
        stop_markers=["岗位职责", "工作职责", "职位描述", "加分项", "优先"],
    )
    bonus_text = _collect_section_text(
        lines,
        start_markers=["加分项", "优先"],
        stop_markers=["岗位职责", "工作职责", "岗位要求", "任职要求", "职位要求"],
    )
    if not core_text:
        core_text = _collect_requirement_text(lines, ["必备", "要求", "任职"])
    responsibilities = _extract_responsibilities(lines)

    core_skills = extract_known_skills(core_text or jd_text)
    bonus_skills = [skill for skill in extract_known_skills(bonus_text) if skill not in core_skills]
    keywords = _keywords_from_text(jd_text, core_skills, bonus_skills)
    weights = {skill: 1.0 for skill in core_skills} | {skill: 0.5 for skill in bonus_skills}

    return JobProfile(
        target_role=target_role,
        core_skills=core_skills,
        bonus_skills=bonus_skills,
        responsibilities=responsibilities,
        keywords=keywords,
        weights=weights,
        raw_text=jd_text,
    )


def _extract_role(lines: list[str]) -> str:
    for line in lines:
        lowered = line.lower()
        if _is_section_heading(line) or "：" in line or ":" in line:
            continue
        if any(token in lowered for token in ["工程师", "developer", "engineer", "实习生", "开发"]):
            return re.split(r"[，,。:：]", line)[0].strip()
    return lines[0] if lines else "Target Role"


def _collect_requirement_text(lines: list[str], markers: list[str]) -> str:
    matched = [line for line in lines if any(marker in line for marker in markers)]
    return " ".join(matched)


def _collect_section_text(lines: list[str], start_markers: list[str], stop_markers: list[str]) -> str:
    chunks: list[str] = []
    in_section = False
    for line in lines:
        if any(marker in line for marker in start_markers):
            in_section = True
            remainder = re.sub(r"^.*?[：:]", "", line).strip()
            if remainder and remainder != line:
                chunks.append(remainder)
            continue
        if in_section and any(marker in line for marker in stop_markers):
            break
        if in_section:
            chunks.append(_clean_numbered_line(line))
    return " ".join(chunks)


def _extract_responsibilities(lines: list[str]) -> list[str]:
    section_text = _collect_section_text(
        lines,
        start_markers=["岗位职责", "工作职责", "职位描述", "职责"],
        stop_markers=["岗位要求", "任职要求", "职位要求", "任职资格", "加分项", "优先"],
    )
    if not section_text:
        section_text = " ".join(line for line in lines if "负责" in line)
    return [_clean_numbered_line(part) for part in re.split(r"(?=\d+[、.．])|[；;]", section_text) if part.strip()]


def _clean_numbered_line(line: str) -> str:
    return re.sub(r"^\s*\d+\s*[、.．]\s*", "", line).strip()


def _is_section_heading(line: str) -> bool:
    normalized = line.strip().rstrip("：:")
    return normalized in {
        "岗位职责",
        "工作职责",
        "职位描述",
        "岗位要求",
        "任职要求",
        "职位要求",
        "任职资格",
        "加分项",
    }


def _keywords_from_text(text: str, core_skills: list[str], bonus_skills: list[str]) -> list[str]:
    keywords = list(dict.fromkeys([*core_skills, *bonus_skills, *extract_known_skills(text)]))
    for token in ["RAG", "Agent", "LLM", "API", "评估", "模型服务", "AI Engineering", "性能优化", "高可用", "高并发"]:
        if token.lower() in text.lower() and token not in keywords:
            keywords.append(token)
    return keywords
