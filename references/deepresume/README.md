# DeepResume Reference Library

DeepResume Reference Library 是 CV2Offer Agent 的默认参考内容库，保留原先围绕个人简历生成的学习路线、面试准备资料、项目深挖问答、短期冲刺计划和面经复盘。

在新架构中，`cv2offer-agent` 是主项目；本目录只作为参考资料来源。Agent 可以把这里的简历、学习计划和面试准备内容作为默认样例或路线模板，用于初始化 CV-JD 差距分析、学习计划导入和证据沉淀。

## 内容导航

| 方向 | 简历入口 | 面试准备资料 |
| --- | --- | --- |
| 算法工程师 / AI 应用开发 | [algorithm/algorithm.md](algorithm/algorithm.md) | [algorithm/ai_algorithm_interview_guide/](algorithm/ai_algorithm_interview_guide/) |
| 前端开发 / AI 应用型前端 | [frontend/frontend.md](frontend/frontend.md) | [frontend/frontend_interview_guide/](frontend/frontend_interview_guide/) |
| 测试开发 / 游戏测试 | [testdevelop/testdevelop.md](testdevelop/testdevelop.md) | [testdevelop/testdevelop_interview_guide/](testdevelop/testdevelop_interview_guide/) |
| 面试经验 | - | [interview_experience/](interview_experience/) |

## 路线索引

`reference_routes.json` 描述了每条默认参考路线的入口：

- `resume_path`：默认简历 Markdown
- `resume_tex_path`：对应 LaTeX 简历
- `guide_path`：面试准备资料目录
- `learning_plan_path`：默认学习主线
- `target_roles`：适合的岗位方向

后续可以由 CV2Offer Agent 后端读取这个索引，提供“载入默认参考路线”的能力。

## 维护原则

- 这里保存事实材料、学习路线和面试复盘，不直接承担 Web App 运行逻辑。
- 简历内容变化后，同步更新对应方向的项目深挖、学习计划和证据描述。
- 对外投递前检查联系方式、隐私信息、项目数据和公司信息是否适合公开。
- 优先维护可验证事实，不把不熟悉的技术词堆进简历。
