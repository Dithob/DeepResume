from app.services.job_parser import parse_job_description
from app.services.learning_plan_parser import import_learning_plan_markdown
from app.services.resume_parser import parse_resume_text


def test_resume_parser_extracts_skills_with_source_evidence():
    resume = """
    ## 专业技能
    熟悉 Dify、LangChain、FastAPI、Docker、Redis，并使用 Milvus 与 MySQL 构建 RAG 系统。
    ## 项目经历
    基于 RAG 的医药数据分析问答助手，结合 RAGAS、Golden Dataset 与 SQL 自纠错。
    """

    profile = parse_resume_text(resume)

    skill_names = {skill.name for skill in profile.skills}
    assert {"LangChain", "FastAPI", "Docker", "Milvus", "RAGAS"}.issubset(skill_names)
    fastapi = next(skill for skill in profile.skills if skill.name == "FastAPI")
    assert fastapi.evidence is not None
    assert "FastAPI" in fastapi.evidence


def test_job_parser_extracts_role_core_bonus_and_keywords():
    jd = """
    AI 应用开发工程师
    岗位职责：负责 RAG 问答、Agent workflow、模型服务接口与评估闭环。
    必备要求：熟悉 LangChain、FastAPI、向量数据库、Prompt Engineering。
    加分项：熟悉 LangGraph、Qdrant、Rerank、RAGAS、Docker。
    """

    job = parse_job_description(jd)

    assert job.target_role == "AI 应用开发工程师"
    assert {"LangChain", "FastAPI", "Vector Database", "Prompt Engineering"}.issubset(set(job.core_skills))
    assert {"LangGraph", "Qdrant", "Rerank", "RAGAS", "Docker"}.issubset(set(job.bonus_skills))
    assert "Agent" in job.keywords


def test_job_parser_extracts_numbered_chinese_requirement_sections():
    jd = """
    agent开发实习生
    招聘系列：日常实习
    职位类别：研发技术类
    工作地点：杭州
    岗位职责
    1、负责同花顺核心业务单元的agent架构设计与技术落地，构建具备高效迭代能力和高扩展性的agent服务框架。
    2、支撑同花顺 AI 业务的后端持续迭代，主导相关系统重构与性能优化工作，保障 AI 能力稳定输出。

    岗位要求
    1、掌握Agent开发和架构，具有落地经验。
    2、熟练掌握 Spring Boot、Spring Cloud、MyBatis 等主流框架，具备微服务架构设计、分布式系统开发经验。
    3、熟悉 Redis、RabbitMQ/Kafka、MySQL 等中间件与数据库，能熟练进行性能调优与问题排查。
    4、具备大型分布式系统架构设计、重构及性能优化实战经验，理解高可用、高并发、可扩展性设计原则。
    """

    job = parse_job_description(jd)

    assert job.target_role == "agent开发实习生"
    assert {
        "Agent",
        "Spring Boot",
        "Spring Cloud",
        "MyBatis",
        "Microservices",
        "Distributed Systems",
        "Redis",
        "RabbitMQ",
        "Kafka",
        "MySQL",
        "Performance Optimization",
        "High Availability",
        "High Concurrency",
    }.issubset(set(job.core_skills))
    assert any("agent架构设计" in item for item in job.responsibilities)
    assert "AI Engineering" in job.keywords


def test_learning_plan_markdown_expands_week_ranges_into_each_week():
    markdown = """
    # 学习主线与阶段规划

    | 阶段 | 时间 | 目标 | 主要内容 | 输出物 |
    |---|---:|---|---|---|
    | 快速补基础 | 第 1-2 周 | 守住算法题和 CS 基础 | 数据结构、Python、MySQL、Redis | 每天 2-3 题；整理错题 |
    | RAG / Agent 应用 | 第 3-4 周 | 把项目深挖到可面试 | RAG、Agent、Text-to-SQL | 每个项目准备 10 个追问答案 |
    """

    plan = import_learning_plan_markdown(markdown, weekly_hours=8)

    assert plan.title == "学习主线与阶段规划"
    assert plan.duration_weeks == 4
    assert [milestone.week for milestone in plan.milestones] == [1, 2, 3, 4]
    assert plan.milestones[0].goal == "守住算法题和 CS 基础（1/2）"
    assert plan.milestones[1].goal == "守住算法题和 CS 基础（2/2）"
    assert plan.milestones[2].tasks[0].title == "RAG / Agent 应用（1/2）：把项目深挖到可面试"
    assert plan.milestones[0].tasks[0].deliverable == "每天 2-3 题；整理错题"
    assert {"Python", "MySQL", "Redis"}.issubset(set(plan.milestones[0].tasks[0].skills))
