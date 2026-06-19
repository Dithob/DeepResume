# DeepResume

DeepResume 是一个围绕个人简历展开的求职准备资料库，面向算法 / AI 应用开发、前端开发、测试开发三类方向，整理简历版本、学习路线、短期冲刺计划、项目深挖问答、常考知识清单、面经策略和资源索引。

仓库地址：[github.com/Dithob/DeepResume](https://github.com/Dithob/DeepResume)

## 项目定位

这个仓库不是通用八股文合集，而是以简历内容为中心，把“我做过什么”拆成“面试官可能怎么问、我应该怎么补、投递时怎么定位”。

核心目标：

- 为不同岗位方向准备可投递的简历版本。
- 把简历项目拆解成可复盘、可追问、可量化的面试叙事。
- 建立 12 周学习主线和 7 天面试冲刺计划。
- 沉淀常考知识点、公开面经分析和高质量学习资源。
- 帮助 AI 应用、前端、测试开发等方向形成更清晰的岗位匹配策略。

## 内容导航

| 方向 | 简历入口 | 面试准备资料 |
| --- | --- | --- |
| 算法工程师 / AI 应用开发 | [algorithm/algorithm.md](algorithm/algorithm.md) | [algorithm/ai_algorithm_interview_guide/](algorithm/ai_algorithm_interview_guide/) |
| 前端开发 / AI 应用型前端 | [frontend/frontend.md](frontend/frontend.md) | [frontend/frontend_interview_guide/](frontend/frontend_interview_guide/) |
| 测试开发 / 游戏测试 | [testdevelop/testdevelop.md](testdevelop/testdevelop.md) | [testdevelop/testdevelop_interview_guide/](testdevelop/testdevelop_interview_guide/) |
| 面试经验 | - | [interview_experience/](interview_experience/) |

各方向目录中同时保留了 Markdown 与 LaTeX 文件，便于在内容维护和简历排版之间切换。

## 目录结构

```text
.
├── algorithm/
│   ├── algorithm.md
│   ├── algorithm.tex
│   └── ai_algorithm_interview_guide/
├── frontend/
│   ├── frontend.md
│   ├── frontend.tex
│   └── frontend_interview_guide/
├── testdevelop/
│   ├── testdevelop.md
│   ├── testdevelop.tex
│   └── testdevelop_interview_guide/
└── interview_experience/
```

## 使用方式

1. 先选择目标方向，阅读对应的简历 Markdown，确认岗位定位和项目主线。
2. 进入对应的 `*_interview_guide/` 目录，从 `README.md` 开始按顺序阅读。
3. 用 12 周学习主线补齐长期短板，用 7 天冲刺计划准备临近面试。
4. 对照项目深挖 QA，把每个项目准备到能讲清背景、方案、指标、失败案例和替代方案。
5. 使用常考知识清单做查漏补缺，再结合面经策略调整自我介绍、项目讲述和反问问题。

## 三条准备路线

### 算法 / AI 应用开发

重点围绕 RAG、Text-to-SQL、LLM 应用工程、Agent、模型微调、vLLM 推理部署和工程交付闭环展开。适合投递 AI 应用开发工程师、LLM 应用工程师、RAG 工程师、Agent 应用工程师等方向。

### 前端开发

重点围绕 Vue3、TypeScript、工程化、SSE 流式交互、`iframe` 实时预览、`postMessage` 跨域通信、协同编辑和数据可视化展开。适合投递 Vue 前端、B 端前端、AI 应用型前端、低代码 / 可视化搭建平台等方向。

### 测试开发

重点围绕接口自动化、Web UI 自动化、性能测试、持续测试平台、AI 应用质量保障和游戏测试专项展开。适合投递测试开发工程师、自动化测试工程师、测试平台开发、AI 应用测试开发和游戏 QA 自动化方向。

## 本地查看

```bash
git clone https://github.com/Dithob/DeepResume.git
cd DeepResume
```

直接使用 Markdown 编辑器或 GitHub 页面阅读即可。若需要生成 PDF，可基于各方向目录中的 `.tex` 文件使用本地 LaTeX 环境排版。

## 维护建议

- 简历内容发生变化后，同步更新对应方向的项目深挖 QA 和知识清单。
- 每次面试后，把真实追问、答得不好的点和复盘结论沉淀到对应目录。
- 对外投递前检查联系方式、个人隐私、项目数据和公司信息是否适合公开。
- 优先维护可验证事实，避免把不熟悉的技术词堆进简历。

## 说明

本仓库内容以个人求职准备为主，部分方法论和资料结构可以复用到其他简历。使用时建议结合自己的经历重新改写项目描述、指标数据和面试回答，不要直接套用未经验证的内容。
