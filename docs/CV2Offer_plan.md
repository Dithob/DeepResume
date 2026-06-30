# CV2Offer Agent 开发方案

## Summary

基于 [CV2Offer_developdocs.md](CV2Offer_developdocs.md) 规划一个独立 Web App：`cv2offer-agent`。第一版聚焦“学习闭环”：导入简历/JD或已有学习计划，生成 CV-JD 差距分析，产出可执行学习计划，管理学习进度，并把完成结果沉淀为职业证据。

默认把 [algorithm.md](../references/deepresume/algorithm/algorithm.md) 当作简历样例，把 [01_learning_mainline.md](../references/deepresume/algorithm/ai_algorithm_interview_guide/01_learning_mainline.md) 当作学习计划导入样例。

## Key Changes

- 新建独立 monorepo：`apps/web` 使用 Next.js + TypeScript + TailwindCSS + shadcn/ui；`apps/api` 使用 FastAPI + Pydantic + SQLAlchemy；PostgreSQL + Redis 用 Docker Compose 启动。
- 后端先实现稳定领域模型和可替换 AI 适配器：`mock/rule-based` 为默认，后续接 OpenAI、Qwen、DeepSeek 或 Claude，不让核心流程强依赖某个模型。
- MVP 核心数据类型：
  - `ResumeProfile`：基础信息、技能、项目、经历、教育，每个技能绑定 evidence。
  - `JobProfile`：岗位名、职责、核心技能、加分技能、关键词、权重。
  - `GapReport`：匹配分、已覆盖技能、缺失技能、弱证据技能、学习优先级。
  - `LearningPlan`：周期、周目标、任务、预计耗时、deliverable、关联技能。
  - `LearningTask`：`todo / doing / blocked / done`，支持 check-in、实际耗时、完成产物。
  - `CareerEvidence`：项目/学习/证书/工作证据，绑定任务、技能、链接、证据强度和 resume bullet 草稿。
- 前端第一屏做工作台，不做营销页：左侧导航，主区域包含 CV/JD 导入、差距分析、学习计划看板、证据库四个核心视图。
- 学习计划导入支持 Markdown：先解析标题、表格、阶段、周次、任务、输出物；解析不确定时进入人工确认编辑界面。

## Development Phases

- Phase 0：项目初始化
  搭建 monorepo、Docker Compose、FastAPI `/health`、Next.js 工作台壳、基础 README。
- Phase 1：数据模型与导入
  实现简历文本/Markdown 导入、JD 文本导入、学习计划 Markdown 导入；先用规则解析和 mock 数据跑通存储与展示。
- Phase 2：CV-JD 差距分析
  实现 rule-based 匹配分、技能覆盖、弱证据识别、学习优先级排序；暴露 `POST /api/gap/analyze`。
- Phase 3：学习计划生成与进度管理
  实现 `POST /api/plans/generate`、`POST /api/plans/import`、`PATCH /api/tasks/{id}`；前端提供周计划、任务看板、check-in 和完成产物录入。
- Phase 4：职业证据库
  任务完成后可生成或手写 evidence；证据按技能、来源任务、强度、链接管理；为后续简历组装保留 `resume_bullets` 字段。
- Phase 5：简历组装与复评，放到 MVP 后半段
  基于 evidence 生成 JD 定向 Markdown 简历草稿，显示 evidence trace 和 unsupported claims；PDF 导出与复杂 ATS Review 放到 P1。

## Public APIs

- `POST /api/resumes/parse`：输入 `resume_text | file`，输出 `ResumeProfile`。
- `POST /api/jobs/parse`：输入 `jd_text`，输出 `JobProfile`。
- `POST /api/gap/analyze`：输入 `resume_id`、`job_id`，输出 `GapReport`。
- `POST /api/plans/generate`：输入 `gap_report_id`、`weekly_hours`、`duration_weeks`，输出 `LearningPlan`。
- `POST /api/plans/import`：输入 Markdown 文本，输出可编辑的 `LearningPlan`。
- `PATCH /api/tasks/{id}`：更新状态、check-in、完成产物。
- `POST /api/evidence`：从任务或手动录入创建职业证据。
- `GET /api/evidence`：按技能、任务、证据强度筛选证据。

## Test Plan

- 单元测试：Markdown 学习计划解析、技能标准化、gap score 计算、任务状态流转、evidence 强度判断。
- API 测试：CV/JD parse、gap analyze、plan import/generate、task patch、evidence create/list。
- 前端冒烟测试：导入 `01_learning_mainline.md` 后能看到 12 周计划；完成任务后能生成 evidence；刷新页面数据保留。
- 样例验收：用 `algorithm.md` + 一份 AI 应用开发 JD，能输出缺失技能、弱证据技能和 4-8 周学习计划。

## Assumptions

- 第一版选择“独立 Web App + 学习闭环优先 + 可替换 AI 适配器”。
- 不直接 fork Reactive Resume 或 Resume Matcher，只参考 schema、评分和导出思路。
- 多用户登录、RAG 学习资源推荐、GitHub 自动分析、PDF 精排、LangSmith/OpenTelemetry 观测放到 P1/P2。
- ChatGPT 分享链接当前未能直接读取，方案以本地开发文档和现有笔记库为准。
