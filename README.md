# CV2Offer Agent

CV2Offer Agent 是一个面向求职学习闭环的 Web App。它把简历、目标 JD、学习计划和职业证据放到同一个工作台里：先解析简历和岗位需求，再分析 CV-JD 差距，生成或导入学习计划，管理任务进度，最后把完成产物沉淀成可复用的职业证据，并生成 JD 定向 Markdown 简历草稿。

当前版本是 MVP，核心目标不是做一个完整 ATS 或精排简历工具，而是先跑通“差距分析 -> 学习计划 -> 任务执行 -> 证据沉淀 -> 简历草稿”的最小闭环。

原先由 AI 根据简历内容生成的 DeepResume 学习路线已经合并为默认参考内容库，位于 `references/deepresume/`。它为 Agent 提供默认简历、默认学习路线、面试准备资料和复盘素材。

## 功能概览

- 简历导入
  - 支持直接粘贴 Markdown / 文本简历。
  - 支持上传 UTF-8 / GBK 的 `.md`、`.txt` 简历文件。
  - 规则解析简历中的技能、项目证据和原始文本。
- JD 解析
  - 支持常见中文 JD 结构，如“岗位职责 / 岗位要求 / 加分项”。
  - 支持编号列表，例如 `1、2、3、4、`。
  - 已覆盖 AI 应用、Java 后端、微服务、分布式、中间件、数据库等常见技能词。
- CV-JD 差距分析
  - 输出匹配分、已覆盖技能、缺失核心技能、弱证据技能。
  - 为缺失或弱证据技能生成学习优先级和建议任务。
- 学习计划
  - 可根据 gap report 生成 4 周学习计划。
  - 可导入 Markdown 表格学习计划，并把 `第 1-2 周` 这种范围展开为逐周任务。
- 进度管理
  - 任务支持 `todo / doing / blocked / done` 状态。
  - 支持 check-in、实际耗时、完成备注、产物链接。
  - 完成任务后可自动生成职业证据。
- 职业证据库
  - 支持从任务生成 evidence。
  - 支持手动录入 evidence，包括类型、技能、来源任务、产物链接、resume bullet。
  - 支持按技能、来源任务、证据强度、是否有链接筛选。
- JD 定向简历草稿
  - 基于当前简历、JD 和 evidence 生成 Markdown 草稿。
  - 展示 evidence trace。
  - 标出 unsupported claims，提醒哪些 JD 核心技能还缺少证据支持。

## 当前架构

```text
.
├── apps/
│   ├── api/                         # FastAPI 后端
│   └── web/                         # Next.js 前端工作台
├── docs/                            # CV2Offer 产品与开发文档
├── packages/                        # schema / prompts / evals 预留包
├── references/
│   └── deepresume/                  # 默认参考内容库
│       ├── algorithm/               # 算法 / AI 应用开发路线
│       ├── frontend/                # 前端 / AI 应用型前端路线
│       ├── testdevelop/             # 测试开发 / 游戏测试路线
│       ├── interview_experience/    # 面试经验复盘
│       ├── README.md
│       └── reference_routes.json    # 默认参考路线索引
├── docker-compose.yml
├── package.json
└── README.md
```

## 技术栈

- `apps/web`
  - Next.js 16
  - React 18
  - TypeScript
  - TailwindCSS
  - lucide-react
- `apps/api`
  - FastAPI
  - Pydantic
  - rule-based parser / analyzer / planner
  - in-memory repository
- Infra
  - Docker Compose
  - PostgreSQL
  - Redis

说明：MVP 后端目前使用内存存储，Docker Compose 中的 PostgreSQL 和 Redis 已预留，但核心数据还没有持久化到数据库。重启 API 后，已解析的数据、计划和证据会丢失。

## 环境要求

- Python 3.11+
- Node.js 20+，当前开发环境使用 Node 24 也可以运行
- npm
- 可选：Docker Desktop

## 本地启动

### 1. 安装前端依赖

在项目根目录执行：

```bash
npm install
```

### 2. 安装后端依赖

进入 API 目录：

```bash
cd apps/api
pip install -r requirements.txt
```

### 3. 启动 API

建议在项目根目录执行：

```bash
npm run api:dev
```

等价的手动命令是：

```bash
cd apps/api
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

API 默认地址：

```text
http://127.0.0.1:8000
```

健康检查：

```text
http://127.0.0.1:8000/health
```

### 4. 启动前端

回到项目根目录：

```bash
npm --workspace apps/web run dev
```

前端默认地址：

```text
http://localhost:3000
```

也可以使用根目录脚本：

```bash
npm run web:dev
```

## Docker 启动

```bash
docker compose up --build
```

服务端口：

- Web: `http://localhost:3000`
- API: `http://localhost:8000`
- PostgreSQL: `localhost:5432`
- Redis: `localhost:6379`

## 使用流程

### 1. 导入简历和 JD

打开工作台后，在“导入简历与 JD”区域：

- 把简历文本粘贴到 `Resume / Markdown`。
- 或在 `CV file` 选择 `.md` / `.txt` 简历文件，然后点击 `Parse CV file`。
- 把目标岗位 JD 粘贴到 `Target JD`。
- 点击 `Parse resume` 和 `Parse JD`。

解析成功后，下方会显示简历 ID、岗位名称、核心技能和加分技能。

### 2. 生成差距分析

简历和 JD 都解析后，点击：

```text
Generate gap report
```

系统会输出已覆盖技能、缺失核心技能、弱证据技能，以及每个技能的状态、优先级、建议任务和建议产物。

### 3. 生成或导入学习计划

有两种方式：

- 在 Gap Report 中点击 `Generate 4-week plan`。
- 在“学习计划导入”中粘贴 Markdown 表格，然后点击 `Import Markdown plan`。

Markdown 表格推荐格式：

```markdown
| 阶段 | 时间 | 目标 | 主要内容 | 输出物 |
|---|---:|---|---|---|
| 快速补基础 | 第 1-2 周 | 守住算法题和 CS 基础 | 数据结构、Python、MySQL、Redis | 每天 2-3 题；整理错题 |
| RAG / Agent 应用 | 第 3-4 周 | 把项目深挖到可面试 | RAG、Agent、Text-to-SQL | 每个项目准备 10 个追问答案 |
```

导入后会在“周计划看板”中生成逐周任务。

### 4. 管理任务进度

在“周计划看板”里，每个任务可以填写状态、实际耗时、check-in、完成备注和产物链接。

操作按钮：

- `保存进度`：只更新任务状态和 check-in。
- `完成并生成证据`：把任务标记为完成，并创建 career evidence。

注意：任务标记为 `done` 时，必须填写完成备注或至少一个产物链接。

### 5. 管理职业证据

在 `Evidence Vault` 中可以按技能、来源任务、证据强度和是否有链接筛选，也可以手动创建 evidence。

手动 evidence 支持字段：

- Evidence title
- Type：`learning / project / work / certificate`
- Skills
- Source task
- Artifact link
- Resume bullet

证据强度规则：

- 没有链接：`weak`
- 1 个有效链接：`medium`
- 2 个及以上有效链接：`strong`

### 6. 生成 JD 定向简历草稿

在“定向简历草稿”区域点击：

```text
Assemble resume
```

系统会基于当前 `ResumeProfile`、`JobProfile` 和 `CareerEvidence` 生成 Markdown 简历草稿，并展示：

- Evidence trace：每条证据支撑了哪些 JD 技能。
- Unsupported claims：JD 核心技能中目前没有 evidence 支撑的技能。

## DeepResume 默认参考内容库

参考内容库位于：

- [references/deepresume/](references/deepresume/)

包含三条默认路线：

| 路线 | 简历入口 | 学习与面试资料 |
| --- | --- | --- |
| 算法 / AI 应用开发 | [algorithm/algorithm.md](references/deepresume/algorithm/algorithm.md) | [algorithm/ai_algorithm_interview_guide/](references/deepresume/algorithm/ai_algorithm_interview_guide/) |
| 前端 / AI 应用型前端 | [frontend/frontend.md](references/deepresume/frontend/frontend.md) | [frontend/frontend_interview_guide/](references/deepresume/frontend/frontend_interview_guide/) |
| 测试开发 / 游戏测试 | [testdevelop/testdevelop.md](references/deepresume/testdevelop/testdevelop.md) | [testdevelop/testdevelop_interview_guide/](references/deepresume/testdevelop/testdevelop_interview_guide/) |

路线索引：

- [references/deepresume/reference_routes.json](references/deepresume/reference_routes.json)

后续可以读取这个索引，在前端提供“载入默认参考路线”的能力，例如一键载入算法 / AI 应用开发方向的默认简历和 12 周学习计划。

## API 列表

### Health

```http
GET /health
```

### Resume

```http
POST /api/resumes/parse
POST /api/resumes/parse-file
GET /api/resumes
POST /api/resumes/assemble
```

### Job

```http
POST /api/jobs/parse
GET /api/jobs
```

### Gap

```http
POST /api/gap/analyze
```

### Learning Plan

```http
POST /api/plans/generate
POST /api/plans/import
GET /api/plans
GET /api/plans/{plan_id}
```

### Task

```http
PATCH /api/tasks/{task_id}
```

### Evidence

```http
POST /api/evidence
GET /api/evidence
```

## 测试与验证

后端测试：

```bash
npm run api:test
```

或：

```bash
cd apps/api
python -m pytest
```

前端类型检查：

```bash
npm --workspace apps/web run typecheck
```

前端生产构建：

```bash
npm --workspace apps/web run build
```

说明：在 Windows 上，Next.js 构建时可能出现 `@next/swc-win32-x64-msvc ... is not a valid Win32 application` 警告。当前项目使用 `next build --webpack`，Next 会回退到 WASM bindings，构建仍可成功完成。

## 当前限制

- 暂未接入真实 LLM，解析、评分、计划和简历组装均为 rule-based。
- 暂未把数据持久化到 PostgreSQL，API 重启后内存数据会清空。
- CV 文件上传当前支持 `.md` / `.txt` 文本文件，不支持 PDF / DOCX 精准抽取。
- 没有用户登录和多用户隔离。
- 简历草稿是 Markdown 草稿，不包含 PDF 导出和复杂版式排版。
- Evidence trace 只基于技能匹配，不做深层事实核验。

## 后续方向

- 新增 `GET /api/references`，读取 `references/deepresume/reference_routes.json`。
- 在前端导入区新增“默认参考路线”下拉框。
- 支持一键载入参考路线中的简历和学习计划。
- 将参考路线中的项目深挖 QA 转成 evidence template。
- 接入 PostgreSQL + SQLAlchemy 持久化。
- 接入可替换 AI adapter：OpenAI、Qwen、DeepSeek、Claude 等。
- 支持 PDF / DOCX 简历解析。
- 增加 JD 定向简历导出、PDF 生成和更细粒度 ATS Review。
