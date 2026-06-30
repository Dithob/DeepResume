下面是一个可以直接拿去放进 **Codex / README / 项目设计文档** 的总结版。我建议你把这个项目定位为：

# CV2Offer Agent

**基于 CV-JD 差距分析的学习规划、职业证据沉淀与岗位定向简历组装系统**

------

## 1. 项目背景

当前很多求职者的问题不是“不知道要学什么”，而是：

1. 目标岗位 JD 很多，技能要求分散，不知道优先补什么；
2. 简历已有能力和目标岗位之间存在差距，但差距不够清晰；
3. 学习计划和简历优化是割裂的：学完一个技能或项目后，不知道如何转化成简历表达；
4. 简历优化工具大多只做“CV + JD → 改简历”，容易出现空泛改写、关键词堆砌甚至编造经历；
5. 学习规划工具大多只做“目标岗位 → 学习路线”，缺少进度管理和求职结果导向。

所以这个项目要解决的问题是：

> 根据用户当前简历和目标 JD，识别技能与项目差距，生成学习路线和任务计划；用户完成学习任务后，将学习成果沉淀为可验证职业证据，再根据目标 JD 自动组装一份 ATS 友好、证据支撑、可持续进化的简历。

项目核心不是“AI 帮你编简历”，而是：

> **AI 帮你发现差距、安排学习、沉淀证据、组装简历、继续反向驱动下一轮学习。**

------

## 2. 项目目标

项目面向 AI 应用开发、数据分析、前端、后端等求职方向的用户，MVP 阶段建议先聚焦 **AI 应用开发岗位**，因为这个方向与你自己的简历最匹配，也方便你把项目作为个人求职作品。

系统目标：

```text
输入：当前简历 + 目标 JD + 学习时间约束
输出：
1. CV-JD 差距分析报告
2. 个性化学习路线
3. 周计划 / 任务看板
4. 学习成果证据库
5. JD 定向简历版本
6. ATS / JD 匹配评分与优化建议
```

------

## 3. 主要需求分析

### 3.1 用户核心流程

```text
上传 CV
  ↓
粘贴目标 JD
  ↓
系统解析 CV 和 JD
  ↓
生成 CV-JD 差距分析
  ↓
生成学习路线和任务计划
  ↓
用户完成任务 / 项目 / 笔记
  ↓
系统沉淀 Career Evidence
  ↓
系统根据 JD 组装简历
  ↓
ATS 风格评分与优化建议
  ↓
继续发现新差距，更新学习计划
```

------

## 4. 核心功能模块

### 模块一：CV Parser，简历解析

功能：

- 支持 PDF / DOCX / Markdown / 纯文本简历上传；
- 抽取个人信息、技能、项目经历、实习经历、教育经历；
- 将简历转成结构化 JSON；
- 每个技能都需要绑定来源证据，避免 LLM 幻觉。

输出示例：

```json
{
  "skills": [
    {
      "name": "FastAPI",
      "category": "backend",
      "evidence": "实习经历中提到 FastAPI 服务封装与部署"
    },
    {
      "name": "LangChain",
      "category": "ai_application",
      "evidence": "项目经历中提到基于 LangChain 构建 RAG 问答助手"
    }
  ],
  "projects": [],
  "work_experience": [],
  "education": []
}
```

------

### 模块二：JD Analyzer，岗位 JD 分析

功能：

- 抽取岗位职责；
- 抽取必备技能、加分技能、项目经验要求；
- 识别岗位级别：实习 / 初级 / 中级；
- 将 JD 结构化；
- 给技能设置权重。

输出示例：

```json
{
  "target_role": "AI Application Engineer",
  "core_skills": ["LangChain", "RAG", "FastAPI", "Vector Database", "Prompt Engineering"],
  "bonus_skills": ["LangGraph", "Docker", "vLLM", "Rerank", "RAGAS"],
  "responsibilities": [
    "构建 LLM 应用",
    "设计 RAG 流程",
    "封装模型服务接口",
    "优化问答准确率"
  ]
}
```

------

### 模块三：Gap Analyzer，CV-JD 差距分析

功能：

- 比较当前简历和目标 JD；
- 输出技能覆盖率；
- 输出项目证据覆盖率；
- 标记缺失技能、弱技能、无证据技能；
- 生成学习优先级。

差距类型：

```text
1. 已具备且有证据：可以直接写入简历
2. 已学习但证据弱：需要补项目或产出物
3. 完全缺失：进入学习计划
4. JD 重要但简历表达弱：进入简历优化
```

------

### 模块四：Learning Planner，学习规划 Agent

功能：

- 根据差距生成学习路线；
- 根据用户每周可学习时间拆成周计划；
- 每个任务必须有明确 deliverable；
- 优先项目驱动学习，而不是只推荐课程；
- 学习任务完成后自动进入 Evidence Vault。

任务示例：

```json
{
  "week": 2,
  "goal": "补齐 LangGraph Agent 编排能力",
  "tasks": [
    {
      "title": "实现 Resume Parser Agent",
      "estimated_hours": 3,
      "deliverable": "FastAPI 接口 + LangGraph 节点 + 示例输出",
      "skills": ["LangGraph", "FastAPI", "Pydantic"]
    },
    {
      "title": "实现 JD Analyzer Agent",
      "estimated_hours": 3,
      "deliverable": "结构化 JD JSON 输出",
      "skills": ["LLM structured output", "Prompt Engineering"]
    }
  ]
}
```

------

### 模块五：Progress Tracker，学习进度管理

功能：

- 任务状态：todo / doing / blocked / done；
- 支持每周 check-in；
- 根据实际完成情况自动调整计划；
- 用户完成项目后，引导填写成果链接、GitHub、Demo、笔记；
- 将完成结果转成职业证据。

核心状态：

```text
学习任务状态：
todo / doing / blocked / done

证据状态：
unverified / weak / verified

简历使用状态：
not_used / draft_bullet / included_in_resume
```

------

### 模块六：Career Evidence Vault，职业证据库

这是项目最重要的创新点。

它不是普通学习记录，而是把用户学习结果沉淀成“可写入简历的职业证据”。

示例：

```json
{
  "evidence_id": "rag_project_001",
  "type": "project",
  "title": "基于 RAG 的简历与 JD 分析系统",
  "skills": ["RAG", "LangChain", "FastAPI", "Qdrant"],
  "source": "learning_plan_week_4",
  "artifacts": {
    "github": "https://github.com/xxx/cv2offer-agent",
    "demo": "https://demo.xxx.com",
    "doc": "system-design.md"
  },
  "verified": true,
  "resume_bullets": [
    "基于 LangGraph、FastAPI 与 Qdrant 构建 CV-JD 差距分析 Agent，实现简历解析、岗位技能抽取、差距识别与学习路线生成闭环。"
  ]
}
```

------

### 模块七：JD-Aware Resume Composer，岗位定向简历组装器

功能：

- 根据目标 JD，从 Career Evidence Vault 中挑选最相关内容；
- 自动调整简历模块顺序；
- 自动生成技能区、项目区、经历区 bullet；
- 控制 1 页 / 2 页长度；
- 输出 Markdown / HTML / PDF；
- 不允许编造没有证据支撑的内容。

重点约束：

```text
如果技能没有证据：
不能写成“熟练掌握”。

如果只是学过：
可以写入学习记录，但不应写成项目经验。

如果有项目、GitHub、Demo、文档：
可以写入项目经历。
```

------

### 模块八：ATS / JD Review，匹配评分与优化建议

功能：

- 计算 JD 关键词覆盖率；
- 计算技能匹配度；
- 计算项目证据覆盖率；
- 检查简历是否存在“无证据技能”；
- 给出缺失关键词和优化建议；
- 将新差距反向写入学习计划。

Resume Matcher 这类项目已经提供了 CV 和 JD 匹配、关键词高亮、修改建议、PDF 导出等能力，可以作为参考。([GitHub](https://github.com/srbhr/Resume-Matcher?utm_source=chatgpt.com))

------

## 5. 推荐技术栈

### 5.1 最推荐栈

```text
Frontend:
- Next.js
- TypeScript
- TailwindCSS
- shadcn/ui
- React Flow
- TanStack Table

Backend:
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL

Agent:
- LangGraph
- LangChain
- OpenAI / Qwen / DeepSeek / Claude API

RAG:
- Qdrant 或 PostgreSQL + pgvector

Async / Cache:
- Redis
- Celery 或 RQ

Resume:
- JSON Resume-inspired schema
- Markdown / HTML template
- Playwright / WeasyPrint / Puppeteer PDF export

File Parsing:
- PyMuPDF
- python-docx
- unstructured

Deployment:
- Docker Compose
- GitHub Actions
- 可选：Kubernetes

Evaluation:
- 自定义 CV-JD 匹配评分
- RAGAS
- Prompt / Agent trace logging
```

------

## 6. 为什么用这套技术栈？

### FastAPI

适合做 AI 应用后端，和你简历中已有 FastAPI 服务封装经验匹配。你可以用它封装 CV 解析、JD 分析、学习规划、简历生成等 API。

### LangGraph

这个项目天然是多阶段、有状态、可循环的 Agent 流程。LangGraph 官方定位就是用于构建和管理 long-running、stateful agents 的底层编排框架。([LangChain 文档](https://docs.langchain.com/oss/python/langgraph/overview?utm_source=chatgpt.com))

相比单纯 LangChain chain，LangGraph 更适合：

```text
CV 解析 → JD 分析 → 差距识别 → 学习计划 → 证据沉淀 → 简历组装 → 评分 → 反向更新计划
```

### PostgreSQL

存结构化数据：

```text
用户
简历版本
JD
技能
学习计划
学习任务
职业证据
简历生成版本
匹配报告
```

### Qdrant / pgvector

用于检索：

```text
岗位技能库
学习资源
用户项目证据
历史简历版本
JD 样本
简历 bullet 模板
```

MVP 可以先用 PostgreSQL + pgvector 简化架构；如果想展示 AI 应用栈，可以用 Qdrant。

### JSON Resume-inspired schema

JSON Resume 是开源社区推动的 JSON 简历标准，目标是让简历用结构化数据表达，并支持不同主题渲染和导出。([GitHub](https://github.com/jsonresume?utm_source=chatgpt.com))

你的项目可以不完全照搬，但应该借鉴它的数据结构。

------

## 7. 参考开源项目

### 7.1 Reactive Resume

用途：参考简历编辑器、模板、多版本、PDF 导出、自托管。

Reactive Resume 是开源简历构建器，强调隐私、自托管、无追踪、无广告和 PDF 导出。([GitHub](https://github.com/AmruthPillai/Reactive-Resume?utm_source=chatgpt.com))

不建议一开始 fork 它作为基座，因为它是完整产品，集成成本较高。更适合参考 UI 和数据模型。

------

### 7.2 JSON Resume

用途：参考简历结构化 schema。

JSON Resume 是开源的 JSON 简历标准，主张“写一次结构化简历，再用不同主题渲染、托管和导出”。([GitHub](https://github.com/jsonresume?utm_source=chatgpt.com))

适合作为你的 `resume_schema` 基础。

------

### 7.3 Resume Matcher

用途：参考 JD 匹配、ATS 分数、关键词高亮、简历修改建议。

Resume Matcher 支持根据 JD 和简历生成匹配分、关键词高亮、修改建议，还支持导出定制简历和求职信 PDF。([GitHub](https://github.com/srbhr/Resume-Matcher?utm_source=chatgpt.com))

可以参考它的：

```text
CV-JD match score
keyword coverage
resume improvement suggestions
ATS-style analysis
```

------

### 7.4 Reactive Resume / RenderCV 类项目

用途：参考简历渲染和导出。

如果你想做“简历即代码”，可以参考 YAML / JSON → PDF 的思路；但 MVP 阶段不需要过度投入排版系统。

------

### 7.5 roadmap.sh

用途：参考学习路线内容组织方式。

它可以作为技术路线图内容参考，但你的项目不要只做静态路线图，而要做“基于 CV-JD 差距的动态路线”。

------

## 8. 是否从 0 开始，还是基于现有项目？

我的建议：

## **从 0 开始做主项目，不 fork 大型项目。**

原因：

1. 你的核心创新是 **CV-JD Gap → Learning Plan → Evidence Vault → Resume Composer**，现有项目没有完整闭环；
2. Reactive Resume 太偏简历编辑器，fork 后你会被它的复杂架构绑定；
3. Resume Matcher 太偏 ATS 匹配，缺少学习计划和证据库；
4. 从 0 做可以更好展示你的 AI 应用工程能力；
5. MVP 不需要复杂拖拽编辑器，先做结构化简历和 Markdown/PDF 导出即可。

更好的方式是：

```text
从 0 搭建主项目
  ↓
借鉴 JSON Resume schema
  ↓
借鉴 Resume Matcher 的匹配评分
  ↓
借鉴 Reactive Resume 的简历版本和模板体验
  ↓
后续再考虑接入完整编辑器
```

------

## 9. MVP 开发路线

下面这份路线适合你直接交给 Codex 分阶段开发。

------

# Phase 0：项目初始化

目标：搭建 monorepo 和基础服务。

目录结构建议：

```text
.
  apps/
    web/
    api/
  packages/
    resume-schema/
    prompts/
    evals/
  docs/
    product-design.md
    system-design.md
  references/
    deepresume/
  docker-compose.yml
  README.md
```

技术：

```text
apps/web:
- Next.js
- TypeScript
- TailwindCSS
- shadcn/ui

apps/api:
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL

infra:
- Docker Compose
- PostgreSQL
- Redis
```

交付物：

```text
1. 前后端项目初始化
2. Docker Compose 一键启动
3. FastAPI health check
4. Next.js 首页
5. README 初版
```

------

# Phase 1：CV / JD 结构化解析

目标：实现最小可用的 CV 和 JD 解析。

功能：

```text
1. 上传 / 粘贴简历文本
2. 粘贴 JD 文本
3. LLM 结构化抽取
4. 保存到数据库
5. 在前端展示结构化结果
```

API：

```text
POST /api/resumes/parse
POST /api/jobs/parse
GET  /api/resumes/{id}
GET  /api/jobs/{id}
```

核心模型：

```python
class ResumeSkill(BaseModel):
    name: str
    category: str
    evidence: str | None
    confidence: float

class ParsedResume(BaseModel):
    basics: dict
    skills: list[ResumeSkill]
    projects: list[dict]
    work_experience: list[dict]
    education: list[dict]

class ParsedJobDescription(BaseModel):
    target_role: str
    core_skills: list[str]
    bonus_skills: list[str]
    responsibilities: list[str]
    keywords: list[str]
```

交付物：

```text
1. 能解析一份中文简历
2. 能解析一份中文/英文 JD
3. 能展示技能、项目、经历、岗位要求
```

------

# Phase 2：CV-JD Gap Analyzer

目标：实现差距分析报告。

功能：

```text
1. 技能覆盖率计算
2. JD 关键词覆盖率
3. 项目证据覆盖率
4. 缺失技能列表
5. 弱证据技能列表
6. 学习优先级排序
```

评分建议：

```text
match_score =
  0.35 * core_skill_coverage
+ 0.25 * evidence_coverage
+ 0.20 * responsibility_match
+ 0.10 * keyword_coverage
+ 0.10 * resume_quality
```

输出示例：

```json
{
  "match_score": 68,
  "strengths": ["RAG", "FastAPI", "LangChain"],
  "missing_core_skills": ["LangGraph", "Qdrant", "Agent Evaluation"],
  "weak_evidence_skills": ["Docker", "Rerank"],
  "learning_priorities": [
    {
      "skill": "LangGraph",
      "priority": "high",
      "reason": "JD 要求 Agent workflow，当前简历缺少明确项目证据"
    }
  ]
}
```

交付物：

```text
1. 差距分析页面
2. 匹配分
3. 缺失技能表
4. 技能证据状态
```

------

# Phase 3：Learning Planner Agent

目标：基于差距生成学习路线。

Agent 技术：

```text
LangGraph
Pydantic structured output
Prompt templates
```

功能：

```text
1. 输入 gap report
2. 输入每周可学习时间
3. 生成 4-8 周学习路线
4. 每周拆成任务
5. 每个任务有 deliverable
```

API：

```text
POST /api/plans/generate
GET  /api/plans/{id}
PATCH /api/tasks/{id}
```

输出示例：

```json
{
  "duration_weeks": 6,
  "weekly_hours": 8,
  "milestones": [
    {
      "week": 1,
      "goal": "补齐 LangGraph 基础",
      "tasks": [
        {
          "title": "实现一个多节点 Agent workflow",
          "deliverable": "可运行 LangGraph demo + README",
          "skills": ["LangGraph", "Agent State"]
        }
      ]
    }
  ]
}
```

交付物：

```text
1. 学习路线页面
2. 周计划页面
3. 任务状态更新
4. 任务完成记录
```

------

# Phase 4：Career Evidence Vault

目标：把学习成果变成职业证据。

功能：

```text
1. 用户完成任务后填写成果
2. 支持 GitHub / Demo / 文档链接
3. Agent 生成 resume bullet 草稿
4. 标记证据强度
5. 存入 Evidence Vault
```

API：

```text
POST /api/evidence
GET  /api/evidence
POST /api/evidence/{id}/generate-bullets
```

数据模型：

```python
class CareerEvidence(BaseModel):
    title: str
    type: Literal["project", "work", "learning", "certificate"]
    skills: list[str]
    artifacts: dict
    source_task_id: str | None
    verified: bool
    evidence_strength: Literal["weak", "medium", "strong"]
    resume_bullets: list[str]
```

交付物：

```text
1. Evidence Vault 页面
2. 技能标签
3. 成果链接
4. bullet 生成
5. 证据强度判断
```

------

# Phase 5：JD-Aware Resume Composer

目标：生成岗位定向简历。

功能：

```text
1. 选择目标 JD
2. 选择基础简历
3. 从 Evidence Vault 中挑选相关证据
4. 自动组装简历
5. 输出 Markdown / HTML
6. 导出 PDF
```

约束：

```text
1. 不允许使用无证据技能编造项目
2. 技能必须来自 CV 或 Evidence Vault
3. 项目 bullet 必须绑定 evidence_id
4. 输出 ATS 友好格式
```

API：

```text
POST /api/resumes/compose
GET  /api/resume-versions/{id}
POST /api/resume-versions/{id}/export-pdf
```

简历版本结构：

```json
{
  "target_job_id": "job_001",
  "sections": {
    "summary": "",
    "skills": [],
    "experience": [],
    "projects": [],
    "education": []
  },
  "evidence_used": ["evidence_001", "evidence_002"],
  "unsupported_claims": []
}
```

交付物：

```text
1. 简历预览页面
2. Markdown 编辑
3. PDF 导出
4. evidence trace 展示
```

------

# Phase 6：ATS Review & Feedback Loop

目标：简历生成后重新评分，并反向生成下一轮学习建议。

功能：

```text
1. 计算新简历和 JD 的匹配分
2. 显示关键词覆盖
3. 显示缺失证据
4. 显示 unsupported claims
5. 生成下一轮学习任务建议
```

交付物：

```text
1. 优化前后匹配分对比
2. 关键词覆盖率
3. 简历风险提示
4. 下一轮学习建议
```

------

## 10. MVP 优先级

建议你先做这 6 个核心能力：

```text
P0:
1. CV 解析
2. JD 解析
3. 差距分析
4. 学习计划生成
5. Evidence Vault
6. JD 定向简历组装

P1:
1. PDF 导出
2. ATS Review
3. 任务看板
4. 简历版本管理

P2:
1. RAG 学习资源推荐
2. GitHub repo 自动分析
3. LangSmith / OpenTelemetry 观测
4. 多模型适配
5. 用户登录和多用户系统
```

------

## 11. 第一个可运行 Demo 应该长什么样？

最小 Demo 流程：

```text
1. 用户粘贴一份 CV 文本
2. 用户粘贴一个 AI 应用开发 JD
3. 系统输出：
   - 当前匹配分：例如 63
   - 缺失技能：LangGraph、Qdrant、Agent Evaluation
   - 弱证据技能：Docker、Rerank
4. 系统生成 4 周学习计划
5. 用户完成一个任务：实现 LangGraph Resume Parser
6. 系统生成一条职业证据
7. 系统基于该证据生成简历 bullet
8. 系统重新组装 JD 定向简历
9. 新匹配分提升到 72
```

这就是你的项目亮点。

------

## 12. 推荐 README 项目介绍

可以这样写：

```text
CV2Offer Agent is an AI-powered career learning system that turns CV-JD gaps into personalized learning plans, tracks learning progress as career evidence, and composes JD-aware resumes based on verified skills and projects.

Unlike traditional resume optimizers, CV2Offer does not fabricate experience. It helps users learn missing skills, build project evidence, and convert real learning outcomes into ATS-friendly resume versions.
```

中文：

```text
CV2Offer Agent 是一个面向求职者的 AI 学习规划与简历组装系统。它根据用户当前简历和目标 JD 分析技能差距，生成个性化学习路线，并将学习过程中的项目、技能和产出沉淀为职业证据，最终组装成面向目标岗位的 ATS 友好简历。

本项目不是让 AI 编造简历，而是帮助用户把真实学习成果转化成可验证、可匹配、可持续进化的简历内容。
```

------

## 13. 你在 Codex 中可以这样下第一条任务

```text
请帮我初始化一个名为 cv2offer-agent 的 monorepo 项目。

技术栈：
- apps/web 使用 Next.js + TypeScript + TailwindCSS
- apps/api 使用 FastAPI + Pydantic + SQLAlchemy
- 数据库使用 PostgreSQL
- 使用 Docker Compose 启动 web、api、postgres、redis
- 创建基础目录：packages/resume-schema、packages/prompts、docs
- FastAPI 提供 GET /health
- Next.js 首页展示项目名 CV2Offer Agent 和简单介绍
- 添加 README.md，说明项目目标、技术栈和启动方式
```

第二条任务：

```text
请在 apps/api 中实现 CV 和 JD 的结构化解析模块。

要求：
1. 创建 Pydantic models：ParsedResume、ResumeSkill、ParsedJobDescription
2. 创建接口 POST /api/resumes/parse，输入 resume_text，输出结构化简历 JSON
3. 创建接口 POST /api/jobs/parse，输入 jd_text，输出结构化 JD JSON
4. 先实现 mock parser，不接 LLM，但保留 llm_parser.py 接口
5. 添加最小单元测试
```

第三条任务：

```text
请实现 CV-JD Gap Analyzer。

输入：
- ParsedResume
- ParsedJobDescription

输出：
- match_score
- strengths
- missing_core_skills
- weak_evidence_skills
- learning_priorities

要求：
1. 先用 rule-based 方式计算技能覆盖率
2. 每个 missing skill 给出 reason
3. 添加 POST /api/gap/analyze 接口
4. 添加测试用例
```

------

## 14. 最终建议

你的项目不要从“简历生成器”开始，也不要从“学习计划生成器”开始。

应该从这个核心闭环开始：

```text
CV + JD
  ↓
差距分析
  ↓
学习计划
  ↓
职业证据
  ↓
JD 定向简历
  ↓
重新评分
```

技术上从 0 做主项目，参考但不 fork 现有大型项目。MVP 先用结构化数据 + Markdown/PDF 简历，不做复杂拖拽编辑器。等闭环跑通后，再增强简历编辑体验、RAG 资源推荐、多模型适配和部署能力。

这个项目如果完成到 MVP，就已经很适合写进你的 AI 应用开发简历；如果再加上 Agent trace、RAG 检索、评估指标和 Docker 一键部署，会是一个非常有说服力的求职项目。
