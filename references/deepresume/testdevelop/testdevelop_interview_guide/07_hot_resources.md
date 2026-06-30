# 热门视频、博客与文档资源地图

## 使用原则

资源不需要全看。按你的目标岗位，优先级是：

1. 先看能直接服务面试的问题：测试理论、接口测试、Pytest、Playwright、JMeter/Locust、MySQL/Redis/Linux。
2. 再看能支撑简历项目深挖的官方文档：pytest、Requests、Postman、Playwright、JMeter、Locust、Allure、FastAPI、Docker。
3. 游戏测试资源以“专项能力补齐”为主：游戏模块测试、弱网、兼容、崩溃、性能、Unity/Unreal 自动化。
4. 视频适合快速建立直觉，官方文档适合准备追问，面经社区适合观察真实问法。

## 测试理论与面试基础

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [ISTQB 官方认证与大纲入口](https://www.istqb.org/certifications) | 官方体系 | 测试理论补框架 | 看测试流程、测试级别、测试设计方法和缺陷管理术语 |
| [TesterHome](https://testerhome.com/) | 中文测试社区 | 面试与实践 | 搜索“测试开发”“自动化测试”“性能测试”“质量平台” |
| [牛客讨论区](https://www.nowcoder.com/discuss) | 面经社区 | 投递前 | 搜索“测试开发 面经”“游戏测试 面经”“性能测试 面经” |
| [代码随想录](https://programmercarl.com/) | 刷题路线 | 笔试/一面 | 按数组、链表、栈队列、树、哈希、DP 顺序刷 |
| [LeetCode 热题 100](https://leetcode.cn/studyplan/top-100-liked/) | 高频题单 | 短期冲刺 | 重点刷简单和中等题，准备复杂度说明 |

## 接口测试与 Pytest

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [pytest 官方文档](https://docs.pytest.org/en/stable/) | 官方文档 | Pytest 深挖 | 重点看 Fixture、parametrize、mark、插件 |
| [Requests 官方文档](https://requests.readthedocs.io/en/latest/) | 官方文档 | 接口客户端封装 | 看 Session、headers、timeout、响应处理 |
| [Postman Learning Center](https://learning.postman.com/docs/getting-started/overview/) | 官方教程 | 接口测试入门 | 看集合、环境变量、脚本、断言和 CI |
| [Allure Report 文档](https://allurereport.org/docs/) | 官方文档 | 报告体系 | 看 Pytest 集成、步骤、附件、报告生成 |
| [Schemathesis 文档](https://schemathesis.readthedocs.io/) | 官方文档 | 契约测试进阶 | 结合 OpenAPI/Swagger 做接口契约和异常测试 |
| [B站检索：Python 自动化测试 pytest](https://search.bilibili.com/all?keyword=Python%20%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%20pytest) | 视频检索 | 快速补课 | 挑播放量高、目录完整、近两年更新的课程 |
| [B站检索：接口自动化测试 Requests Pytest](https://search.bilibili.com/all?keyword=%E6%8E%A5%E5%8F%A3%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%20Requests%20Pytest) | 视频检索 | 项目复盘 | 对照你的接口框架补代码结构和报告演示 |

## Web UI 自动化

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [Playwright Python 文档](https://playwright.dev/python/) | 官方文档 | UI 自动化主线 | 看定位器、自动等待、Trace、截图、视频 |
| [Selenium 文档](https://www.selenium.dev/documentation/) | 官方文档 | Selenium 基础 | 看 WebDriver、定位器、等待和 Grid |
| [B站检索：Playwright 自动化测试 Python](https://search.bilibili.com/all?keyword=Playwright%20%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%20Python) | 视频检索 | 快速实操 | 重点看 PO 模式、Trace 和 CI 集成 |
| [B站检索：Selenium 自动化测试 Python](https://search.bilibili.com/all?keyword=Selenium%20%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%20Python) | 视频检索 | 补传统工具 | 准备面试中 Selenium 与 Playwright 对比 |

## 性能测试

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [Apache JMeter User Manual](https://jmeter.apache.org/usermanual/get-started.html) | 官方文档 | JMeter 基础 | 看线程组、取样器、断言、命令行执行 |
| [Locust 文档](https://docs.locust.io/en/stable/) | 官方文档 | Python 压测 | 看用户行为建模、任务权重、分布式运行 |
| [Grafana k6 Docs](https://grafana.com/docs/k6/latest/) | 官方文档 | 性能工具扩展 | 了解现代脚本化压测和指标输出 |
| [B站检索：JMeter 性能测试](https://search.bilibili.com/all?keyword=JMeter%20%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95) | 视频检索 | 快速补工具 | 重点看参数化、关联、断言、报告 |
| [B站检索：Locust 性能测试 Python](https://search.bilibili.com/all?keyword=Locust%20%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95%20Python) | 视频检索 | 项目补强 | 对照你的持续测试平台准备 Locust 讲述 |

## 工程基础

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [小林 Coding](https://www.xiaolincoding.com/) | 中文博客 | CS 八股 | 重点看 MySQL、Redis、网络 |
| [MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/) | 官方文档 | 细节查证 | 查索引、事务、Explain、权限 |
| [Redis Docs](https://redis.io/docs/latest/) | 官方文档 | 缓存/队列追问 | 查数据结构、过期策略、持久化、命令 |
| [FastAPI 文档](https://fastapi.tiangolo.com/) | 官方文档 | 测试平台后端 | 看 Pydantic、依赖注入、异常处理、异步 |
| [Docker 文档](https://docs.docker.com/) | 官方文档 | 部署基础 | 看 Dockerfile、Compose、volumes、network |
| [GitHub Actions 文档](https://docs.github.com/actions) | 官方文档 | CI/CD | 看 workflow、job、artifact、secrets |

## 游戏测试专项

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest) | 官方文档 | Unity 自动化基础 | 了解 EditMode、PlayMode、测试运行器 |
| [Unreal Engine Automation System](https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-system-in-unreal-engine) | 官方文档 | Unreal 自动化基础 | 了解自动化测试、功能测试和编辑器测试 |
| [Android Games 文档](https://developer.android.com/games) | 官方文档 | 移动游戏基础 | 看性能、帧率、兼容、发布质量 |
| [Android Performance 文档](https://developer.android.com/topic/performance) | 官方文档 | 卡顿/性能定位 | 补 CPU、内存、启动、渲染和电量基础 |
| [Android Debug Bridge 文档](https://developer.android.com/tools/adb) | 官方文档 | 日志与设备调试 | 准备 logcat、安装包、设备信息和调试 |
| [B站检索：游戏测试 面试](https://search.bilibili.com/all?keyword=%E6%B8%B8%E6%88%8F%E6%B5%8B%E8%AF%95%20%E9%9D%A2%E8%AF%95) | 视频检索 | 游戏面试准备 | 重点看用例设计、弱网、兼容、崩溃定位 |
| [B站检索：Unity 自动化测试](https://search.bilibili.com/all?keyword=Unity%20%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95) | 视频检索 | 游戏自动化扩展 | 了解 Unity Test Framework 和简单脚本 |

## AI 应用质量保障

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [Ragas 文档](https://docs.ragas.io/en/stable/) | 官方文档 | RAG 评估 | 看 faithfulness、context precision、answer relevancy |
| [LangChain RAG 教程](https://docs.langchain.com/oss/python/langchain/rag) | 官方文档 | RAG 链路复盘 | 对照 Prompt/RAG 流程测试准备术语 |
| [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals) | 官方文档 | 模型评估 | 学如何把评估集和打分流程产品化 |
| [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling) | 官方文档 | 工具调用测试 | 准备 tool schema、参数校验和结构化输出问题 |
| [Datawhale LLM Universe](https://github.com/datawhalechina/llm-universe) | 中文教程 | RAG 实战 | 补知识库问答、LangChain、向量数据库实践 |

## 面经与求职检索入口

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [牛客搜索：测试开发 面经](https://www.nowcoder.com/search/all?query=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91%20%E9%9D%A2%E7%BB%8F&type=all) | 面经搜索 | 投递前 | 看公司真实问法，整理项目追问 |
| [牛客搜索：游戏测试 面经](https://www.nowcoder.com/search/all?query=%E6%B8%B8%E6%88%8F%E6%B5%8B%E8%AF%95%20%E9%9D%A2%E7%BB%8F&type=all) | 面经搜索 | 游戏岗准备 | 看游戏模块测试点和 HR 问法 |
| [牛客搜索：自动化测试 面经](https://www.nowcoder.com/search/all?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%20%E9%9D%A2%E7%BB%8F&type=all) | 面经搜索 | 自动化岗准备 | 聚焦 Pytest、Selenium/Playwright、接口测试 |
| [TesterHome 搜索页](https://testerhome.com/search) | 测试社区 | 项目补强 | 搜索“测试平台”“pytest”“playwright”“jmeter”“游戏测试” |

## 最推荐的精读组合

如果只选 12 个资源：

1. [pytest 官方文档](https://docs.pytest.org/en/stable/)
2. [Requests 官方文档](https://requests.readthedocs.io/en/latest/)
3. [Postman Learning Center](https://learning.postman.com/docs/getting-started/overview/)
4. [Playwright Python 文档](https://playwright.dev/python/)
5. [Apache JMeter User Manual](https://jmeter.apache.org/usermanual/get-started.html)
6. [Locust 文档](https://docs.locust.io/en/stable/)
7. [Allure Report 文档](https://allurereport.org/docs/)
8. [FastAPI 文档](https://fastapi.tiangolo.com/)
9. [小林 Coding](https://www.xiaolincoding.com/)
10. [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)
11. [Android Debug Bridge 文档](https://developer.android.com/tools/adb)
12. [牛客讨论区](https://www.nowcoder.com/discuss)

## 按岗位选择资源

测试开发优先：

- pytest、Requests、Postman、Playwright、JMeter、Locust、Allure、FastAPI、Docker、GitHub Actions。

游戏测试优先：

- 游戏模块测试点、弱网、兼容性、性能、崩溃日志、Unity Test Framework、Unreal Automation、Android ADB。

AI 应用测试优先：

- Ragas、LangChain RAG、OpenAI Evals、Function Calling、Datawhale LLM Universe。

