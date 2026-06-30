from app.models.domain import EvidenceStrength


SKILL_CATALOG: dict[str, tuple[str, list[str]]] = {
    "LangChain": ("ai_application", ["langchain"]),
    "LangGraph": ("ai_application", ["langgraph"]),
    "RAG": ("ai_application", ["rag", "检索增强"]),
    "FastAPI": ("backend", ["fastapi"]),
    "Pydantic": ("backend", ["pydantic"]),
    "Docker": ("infra", ["docker"]),
    "Redis": ("infra", ["redis"]),
    "MySQL": ("database", ["mysql"]),
    "PostgreSQL": ("database", ["postgresql", "postgres"]),
    "Milvus": ("vector_database", ["milvus"]),
    "Qdrant": ("vector_database", ["qdrant"]),
    "Vector Database": ("vector_database", ["向量数据库", "vector database", "pgvector"]),
    "Prompt Engineering": ("ai_application", ["prompt engineering", "prompt", "提示词"]),
    "Rerank": ("retrieval", ["rerank", "精排"]),
    "RRF": ("retrieval", ["rrf"]),
    "BM25": ("retrieval", ["bm25"]),
    "RAGAS": ("evaluation", ["ragas"]),
    "Agent": ("ai_application", ["agent", "智能体"]),
    "Agent Evaluation": ("evaluation", ["agent evaluation", "agent 评估", "评估闭环"]),
    "Text-to-SQL": ("ai_application", ["text-to-sql", "sql 生成", "schema linking"]),
    "Python": ("language", ["python"]),
    "Java": ("language", ["java"]),
    "Spring Boot": ("backend", ["spring boot", "springboot"]),
    "Spring Cloud": ("backend", ["spring cloud"]),
    "MyBatis": ("backend", ["mybatis"]),
    "Microservices": ("architecture", ["微服务", "microservice", "microservices"]),
    "Distributed Systems": ("architecture", ["分布式系统", "分布式"]),
    "RabbitMQ": ("middleware", ["rabbitmq"]),
    "Kafka": ("middleware", ["kafka"]),
    "Performance Optimization": ("architecture", ["性能优化", "性能调优", "调优"]),
    "High Availability": ("architecture", ["高可用", "稳定性"]),
    "High Concurrency": ("architecture", ["高并发"]),
    "Scalability": ("architecture", ["可扩展性", "扩展性", "高扩展性"]),
    "AI Engineering": ("ai_application", ["ai 工程化", "ai 落地", "ai 软件工程", "ai 工具链", "ai 业务", "ai 能力"]),
    "Code Generation": ("ai_application", ["代码生成", "代码生成工具链"]),
    "Qwen": ("model", ["qwen", "通义千问"]),
    "vLLM": ("inference", ["vllm"]),
}


def normalize_skill(name: str) -> str:
    lowered = name.strip().lower()
    for canonical, (_, aliases) in SKILL_CATALOG.items():
        if lowered == canonical.lower() or lowered in [alias.lower() for alias in aliases]:
            return canonical
    return name.strip()


def extract_known_skills(text: str) -> list[str]:
    lowered = text.lower()
    found: list[str] = []
    for canonical, (_, aliases) in SKILL_CATALOG.items():
        tokens = [canonical, *aliases]
        if any(token.lower() in lowered for token in tokens):
            found.append(canonical)
    return found


def category_for_skill(skill: str) -> str:
    return SKILL_CATALOG.get(normalize_skill(skill), ("general", []))[0]


def judge_text_evidence_strength(sentence: str) -> EvidenceStrength:
    strong_markers = ["项目", "构建", "实现", "封装", "部署", "评估", "github", "demo"]
    medium_markers = ["使用", "基于", "结合", "负责"]
    if any(marker.lower() in sentence.lower() for marker in strong_markers):
        return EvidenceStrength.strong
    if any(marker.lower() in sentence.lower() for marker in medium_markers):
        return EvidenceStrength.medium
    return EvidenceStrength.weak
