from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_resume_file_upload_parses_text_resume():
    response = client.post(
        "/api/resumes/parse-file",
        files={
            "file": (
                "resume.md",
                "姓名：无绝\n熟悉 LangChain、FastAPI，并使用 Milvus 构建 RAG 系统。".encode("utf-8"),
                "text/markdown",
            )
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["id"].startswith("resume_")
    assert "LangChain" in {skill["name"] for skill in payload["skills"]}
    assert "FastAPI" in {skill["name"] for skill in payload["skills"]}
    assert "Milvus" in {skill["name"] for skill in payload["skills"]}
    assert "姓名：无绝" in payload["raw_text"]


def test_parse_gap_plan_and_evidence_flow():
    resume_response = client.post(
        "/api/resumes/parse",
        json={"resume_text": "熟悉 LangChain 和 FastAPI，项目中使用 RAGAS 评估 RAG 效果。"},
    )
    job_response = client.post(
        "/api/jobs/parse",
        json={"jd_text": "AI 应用开发工程师\n必备要求：LangChain、FastAPI、LangGraph。\n加分项：Qdrant、RAGAS。"},
    )

    assert resume_response.status_code == 200
    assert job_response.status_code == 200

    gap_response = client.post(
        "/api/gap/analyze",
        json={
            "resume_id": resume_response.json()["id"],
            "job_id": job_response.json()["id"],
        },
    )
    assert gap_response.status_code == 200
    assert "LangGraph" in gap_response.json()["missing_core_skills"]

    plan_response = client.post(
        "/api/plans/generate",
        json={
            "gap_report_id": gap_response.json()["id"],
            "weekly_hours": 8,
            "duration_weeks": 4,
        },
    )
    assert plan_response.status_code == 200
    task_id = plan_response.json()["milestones"][0]["tasks"][0]["id"]

    task_response = client.patch(
        f"/api/tasks/{task_id}",
        json={
            "status": "done",
            "completion_notes": "完成 README 和接口示例。",
            "artifacts": {"github": "https://github.com/demo/cv2offer"},
        },
    )
    assert task_response.status_code == 200

    evidence_response = client.post("/api/evidence", json={"source_task_id": task_id})
    assert evidence_response.status_code == 200
    assert evidence_response.json()["source_task_id"] == task_id


def test_manual_evidence_can_be_typed_and_filtered_by_skill_task_strength_and_link():
    created_response = client.post(
        "/api/evidence",
        json={
            "title": "RAG 评估闭环复盘",
            "type": "project",
            "skills": ["RAGAS", "FastAPI"],
            "artifacts": {
                "github": "https://github.com/demo/rag-eval",
                "demo": "https://demo.example.com/rag-eval",
            },
            "source_task_id": "manual_task_001",
            "resume_bullets": ["用 RAGAS 和 Golden Dataset 搭建 RAG 评估闭环。"],
        },
    )

    assert created_response.status_code == 200
    created = created_response.json()
    assert created["type"] == "project"
    assert created["source_task_id"] == "manual_task_001"
    assert created["evidence_strength"] == "strong"
    assert created["resume_bullets"] == ["用 RAGAS 和 Golden Dataset 搭建 RAG 评估闭环。"]

    by_skill = client.get("/api/evidence", params={"skill": "RAGAS"}).json()
    by_task = client.get("/api/evidence", params={"source_task_id": "manual_task_001"}).json()
    by_strength = client.get("/api/evidence", params={"strength": "strong"}).json()
    by_link = client.get("/api/evidence", params={"has_link": True}).json()

    assert any(item["id"] == created["id"] for item in by_skill)
    assert any(item["id"] == created["id"] for item in by_task)
    assert any(item["id"] == created["id"] for item in by_strength)
    assert any(item["id"] == created["id"] for item in by_link)


def test_assemble_resume_draft_uses_evidence_and_flags_unsupported_claims():
    resume_response = client.post(
        "/api/resumes/parse",
        json={"resume_text": "姓名：无绝\n熟悉 Agent、Python、FastAPI，并使用 Redis 与 MySQL 构建后端服务。"},
    )
    job_response = client.post(
        "/api/jobs/parse",
        json={
            "jd_text": """
            agent开发实习生
            岗位要求
            1、掌握Agent开发和架构，具有落地经验。
            2、熟练掌握 Spring Boot、Spring Cloud、MyBatis 等主流框架。
            3、熟悉 Redis、RabbitMQ/Kafka、MySQL 等中间件与数据库。
            """
        },
    )
    evidence_response = client.post(
        "/api/evidence",
        json={
            "title": "Agent 后端服务复盘",
            "type": "project",
            "skills": ["Agent", "Redis", "MySQL"],
            "artifacts": {"github": "https://github.com/demo/agent-backend"},
            "resume_bullets": ["实现 Agent 后端服务，并用 Redis 与 MySQL 支撑会话状态和业务数据。"],
        },
    )

    response = client.post(
        "/api/resumes/assemble",
        json={
            "resume_id": resume_response.json()["id"],
            "job_id": job_response.json()["id"],
            "evidence_ids": [evidence_response.json()["id"]],
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["target_role"] == "agent开发实习生"
    assert "## 定向简历草稿" in payload["markdown"]
    assert "实现 Agent 后端服务" in payload["markdown"]
    assert payload["evidence_trace"][0]["evidence_id"] == evidence_response.json()["id"]
    assert "Spring Boot" in payload["unsupported_claims"]
    assert "MyBatis" in payload["unsupported_claims"]


def test_task_patch_records_check_in_hours_and_requires_completion_artifact():
    plan_response = client.post(
        "/api/plans/import",
        json={
            "weekly_hours": 8,
            "markdown": """
            # Phase 03 Plan

            | 阶段 | 时间 | 目标 | 主要内容 | 输出物 |
            |---|---:|---|---|---|
            | RAG / Agent 应用 | 第 1 周 | 补齐项目证据 | RAG、Agent | demo + README |
            """,
        },
    )
    task_id = plan_response.json()["milestones"][0]["tasks"][0]["id"]

    empty_done_response = client.patch(f"/api/tasks/{task_id}", json={"status": "done"})
    assert empty_done_response.status_code == 400
    assert "completion" in empty_done_response.json()["detail"].lower()

    check_in_response = client.patch(
        f"/api/tasks/{task_id}",
        json={
            "status": "doing",
            "actual_hours": 1.5,
            "check_in": "完成 RAG 项目追问清单初稿。",
        },
    )
    assert check_in_response.status_code == 200
    check_in_payload = check_in_response.json()
    assert check_in_payload["status"] == "doing"
    assert check_in_payload["actual_hours"] == 1.5
    assert check_in_payload["check_ins"][0]["note"] == "完成 RAG 项目追问清单初稿。"

    done_response = client.patch(
        f"/api/tasks/{task_id}",
        json={
            "status": "done",
            "actual_hours": 3,
            "completion_notes": "完成 README、架构说明和可运行 demo。",
            "artifacts": {"github": "https://github.com/demo/rag-agent"},
        },
    )
    assert done_response.status_code == 200
    done_payload = done_response.json()
    assert done_payload["status"] == "done"
    assert done_payload["actual_hours"] == 3
    assert done_payload["completion_notes"] == "完成 README、架构说明和可运行 demo。"
    assert done_payload["artifacts"]["github"] == "https://github.com/demo/rag-agent"
    assert len(done_payload["check_ins"]) == 1

    refreshed_plan = client.get(f"/api/plans/{plan_response.json()['id']}").json()
    refreshed_task = refreshed_plan["milestones"][0]["tasks"][0]
    assert refreshed_task["status"] == "done"
    assert refreshed_task["check_ins"][0]["note"] == "完成 RAG 项目追问清单初稿。"


def test_imported_resume_job_and_plan_can_be_listed():
    resume_response = client.post(
        "/api/resumes/parse",
        json={"resume_text": "熟悉 LangChain、FastAPI，并使用 Milvus 构建 RAG 系统。"},
    )
    job_response = client.post(
        "/api/jobs/parse",
        json={"jd_text": "AI 应用开发工程师\n必备要求：LangChain、FastAPI、向量数据库。"},
    )
    plan_response = client.post(
        "/api/plans/import",
        json={
            "weekly_hours": 8,
            "markdown": """
            # 学习主线与阶段规划

            | 阶段 | 时间 | 目标 | 主要内容 | 输出物 |
            |---|---:|---|---|---|
            | RAG / Agent 应用 | 第 1-2 周 | 补齐项目证据 | RAG、Agent、Text-to-SQL | demo + README |
            """,
        },
    )

    assert resume_response.status_code == 200
    assert job_response.status_code == 200
    assert plan_response.status_code == 200

    resumes = client.get("/api/resumes").json()
    jobs = client.get("/api/jobs").json()
    plans = client.get("/api/plans").json()

    assert any(item["id"] == resume_response.json()["id"] for item in resumes)
    assert any(item["id"] == job_response.json()["id"] for item in jobs)
    assert any(item["id"] == plan_response.json()["id"] for item in plans)
