import re

from app.models.domain import ResumeProfile, ResumeSkill
from app.services.skills import (
    category_for_skill,
    extract_known_skills,
    judge_text_evidence_strength,
)


def parse_resume_text(resume_text: str) -> ResumeProfile:
    sentences = _split_sentences(resume_text)
    skills_by_name: dict[str, ResumeSkill] = {}

    for sentence in sentences:
        for skill in extract_known_skills(sentence):
            strength = judge_text_evidence_strength(sentence)
            current = skills_by_name.get(skill)
            candidate = ResumeSkill(
                name=skill,
                category=category_for_skill(skill),
                evidence=sentence.strip(),
                confidence=0.9 if strength.value != "weak" else 0.65,
                evidence_strength=strength,
            )
            if current is None or _strength_rank(candidate.evidence_strength.value) > _strength_rank(current.evidence_strength.value):
                skills_by_name[skill] = candidate

    return ResumeProfile(
        basics=_extract_basics(resume_text),
        skills=list(skills_by_name.values()),
        projects=_extract_sections(resume_text, ["项目经历", "项目"]),
        work_experience=_extract_sections(resume_text, ["实习经历", "工作经历"]),
        education=_extract_sections(resume_text, ["教育背景"]),
        raw_text=resume_text,
    )


def _split_sentences(text: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", text)
    return [part.strip() for part in re.split(r"[。；;\n]", normalized) if part.strip()]


def _strength_rank(strength: str) -> int:
    return {"weak": 0, "medium": 1, "strong": 2}.get(strength, 0)


def _extract_basics(text: str) -> dict[str, str]:
    basics: dict[str, str] = {}
    name_match = re.search(r"姓名[:：]\s*([^\s|]+)", text)
    if name_match:
        basics["name"] = name_match.group(1)
    direction_match = re.search(r"求职方向[:：]\s*([^\n]+)", text)
    if direction_match:
        basics["target_direction"] = direction_match.group(1).strip()
    return basics


def _extract_sections(text: str, headings: list[str]) -> list[dict[str, str]]:
    sections: list[dict[str, str]] = []
    for heading in headings:
        if heading in text:
            sections.append({"title": heading, "source": heading})
    return sections
