# 学习主线与阶段规划

## 目标画像

这份规划服务于两个岗位画像：

- 测试开发工程师：要求测试理论、Python 编程、接口自动化、UI 自动化、性能测试、CI/CD、测试平台和工程问题定位都能讲清楚。
- 游戏测试工程师 / 游戏 QA 自动化：要求在通用测试能力之外，理解游戏玩法、客户端性能、兼容性、弱网、崩溃日志、资源更新、账号资产和游戏生命周期。

你的简历不是从零开始。你已经有测试开发相关项目，学习重点应放在三件事上：

- 把 Pytest、Requests、Playwright、JMeter、Locust、Allure、CI 等工具背后的设计能力补实。
- 把游戏测试专项补成可迁移能力，而不是只说“我愿意做游戏测试”。
- 把 AI 应用测试作为差异化卖点，解释模型输出不可控时如何做评估、断言、回归和 Bad Case 管理。

## 12 周学习路线

| 阶段 | 时间 | 目标 | 主要内容 | 输出物 |
|---|---:|---|---|---|
| 测试基础与用例设计 | 第 1 周 | 建立测试语言体系 | 测试流程、等价类、边界值、场景法、判定表、状态迁移、缺陷生命周期 | 30 条高质量测试用例；缺陷报告模板 |
| HTTP 与接口测试 | 第 2 周 | 能独立测接口 | HTTP、REST、鉴权、状态码、幂等、JSON Schema、Postman、Requests | 登录/用户/订单接口测试集合 |
| Pytest 自动化框架 | 第 3-4 周 | 能解释框架设计 | Fixture、参数化、mark、插件、日志、Allure、数据驱动、失败重试、环境切换 | 一个可运行接口自动化框架 |
| Web UI 自动化 | 第 5 周 | 能写稳定脚本 | Playwright/Selenium、定位器、等待、PO 模式、截图、Trace、视频 | 一个登录/表单/文件上传 UI 案例 |
| 性能测试 | 第 6 周 | 能设计压测并分析 | JMeter、Locust、并发、QPS、TP95、错误率、瓶颈定位、稳定性测试 | 一份接口压测报告 |
| 工程与平台能力 | 第 7 周 | 能讲测试平台落地 | Linux、Git、Docker、MySQL、Redis、FastAPI、Vue、Jenkins/GitHub Actions | 测试任务调度和报告聚合设计图 |
| AI 应用质量保障 | 第 8 周 | 形成差异化能力 | Prompt/RAG 测试、Golden Dataset、Bad Case、JSON Schema、幻觉/拒答/格式校验 | AI 回复回归样例表 |
| 游戏测试基础 | 第 9 周 | 理解游戏 QA 场景 | 玩法规则、账号、背包、商城、抽卡、任务、战斗、匹配、支付、存档 | 游戏模块测试点清单 |
| 游戏专项测试 | 第 10 周 | 能回答游戏面试高频题 | 弱网、兼容性、帧率、卡顿、崩溃、热更新、资源加载、Android logcat、Unity/Unreal 测试 | 游戏缺陷定位流程图 |
| 简历深挖与项目包装 | 第 11 周 | 项目能被追问 | 实习、接口自动化框架、持续测试平台、性能压测、AI 测试、游戏迁移 | 每个项目 10 个追问答案 |
| 面试冲刺 | 第 12 周 | 形成稳定输出 | 自我介绍、项目讲述、手撕代码、八股快问快答、模拟面试 | 3 轮模拟面试复盘 |

## 阶段一：测试基础与用例设计

必须掌握：

- 测试流程：需求评审、测试计划、用例设计、用例评审、测试执行、缺陷跟踪、回归、上线验收。
- 测试类型：功能测试、接口测试、UI 自动化、性能测试、兼容性测试、安全测试、稳定性测试、探索式测试。
- 用例方法：等价类、边界值、场景法、判定表、因果图、正交实验、状态迁移。
- 缺陷生命周期：New、Assigned、Open、Fixed、Rejected、Reopen、Closed。
- 缺陷报告：标题、环境、版本、前置条件、复现步骤、实际结果、期望结果、日志/截图/视频、严重级别、优先级。

面试要能讲：

- 测试用例不是“点点点”，而是覆盖风险、输入空间、状态流转和业务链路。
- 冒烟测试关注主链路是否可用，回归测试关注修复是否引入新问题。
- 严重级别描述影响范围，优先级描述修复顺序，两者不完全一致。

## 阶段二：接口自动化与 Pytest

必须掌握：

- HTTP：方法、状态码、请求头、Cookie、Session、Token、幂等性、缓存、超时、重试。
- 接口测试点：参数校验、鉴权、权限、边界值、异常值、字段缺失、重复提交、并发、幂等、错误码、响应 Schema。
- Pytest：Fixture、scope、autouse、yield、parametrize、mark、conftest.py、插件机制。
- Requests：Session、headers、cookies、timeout、json/data/files、响应解析。
- 自动化框架：配置层、客户端层、业务关键字层、用例层、数据层、报告层。

简历关联：

- 你的“接口自动化测试框架”会被问到分层设计、Token 自动刷新、数据驱动、公共断言、数据库校验和 CI 集成。
- “契约与异常测试”会被问 OpenAPI/Swagger、Schema 校验、异常数据构造和可复现 curl。

推荐资源：

- [pytest 官方文档](https://docs.pytest.org/en/stable/)
- [Requests 官方文档](https://requests.readthedocs.io/en/latest/)
- [Postman Learning Center](https://learning.postman.com/docs/getting-started/overview/)
- [Allure Report 文档](https://allurereport.org/docs/)

## 阶段三：UI 自动化

必须掌握：

- 定位器：CSS、XPath、text、role、label、test id。
- 等待机制：隐式等待、显式等待、自动等待、网络等待、元素状态等待。
- PO 模式：页面对象、业务动作、断言分离、复用和维护。
- 稳定性：截图、Trace、视频、失败重试、隔离测试数据、减少对动态样式和绝对路径依赖。
- 常见场景：登录、搜索、表单提交、弹窗、文件上传、分页、列表筛选。

简历关联：

- 你在持续测试平台里写了 Playwright PO 模式、智能等待、语义化定位器、Trace、截图和视频录制。
- 面试官会问为什么脚本不稳定、如何定位失败、如何降低维护成本。

推荐资源：

- [Playwright Python 文档](https://playwright.dev/python/)
- [Selenium 文档](https://www.selenium.dev/documentation/)

## 阶段四：性能测试

必须掌握：

- 指标：并发用户数、吞吐量、QPS/TPS、平均响应时间、TP95/TP99、错误率、资源利用率。
- 场景：阶梯加压、稳定性运行、峰值压力、容量评估、接口瓶颈定位。
- 工具：JMeter 适合图形化和协议级压测，Locust 适合 Python 代码化场景和复杂用户行为。
- 分析：慢接口、数据库慢查询、缓存命中、连接池、网络超时、服务限流、资源耗尽。

简历关联：

- 你写了 JMeter/Locust、QPS、平均响应时间、P95、错误率和慢接口列表。
- 游戏测试也会关注帧率、帧时间、卡顿、内存、CPU/GPU、发热、耗电和弱网表现。

推荐资源：

- [Apache JMeter User Manual](https://jmeter.apache.org/usermanual/get-started.html)
- [Locust 文档](https://docs.locust.io/en/stable/)

## 阶段五：工程与平台能力

必须掌握：

- Linux：进程、端口、日志、文件、权限、grep/awk/sed、top/free/df/netstat/ss。
- Git：分支、merge、rebase、冲突处理、回滚、CI 触发。
- Docker：镜像、容器、Dockerfile、Compose、端口映射、volume、网络。
- MySQL：索引、事务、隔离级别、Explain、慢查询、连接池。
- Redis：常见数据结构、过期策略、缓存穿透/击穿/雪崩、队列、分布式锁边界。
- CI/CD：Jenkins/GitHub Actions、流水线、测试报告、质量门禁、失败通知。

简历关联：

- 你的持续测试平台使用 FastAPI、Vue.js、MySQL、Redis、Docker。
- 面试官可能会问 Redis 队列如何调度任务、任务失败如何重试、报告数据如何落库、并发任务如何限制。

推荐资源：

- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [Docker 文档](https://docs.docker.com/)
- [GitHub Actions 文档](https://docs.github.com/actions)
- [小林 Coding](https://www.xiaolincoding.com/)

## 阶段六：AI 应用质量保障

必须掌握：

- 测试对象：Prompt、RAG 检索、模型接口、工具调用、结构化输出、多轮对话状态。
- 断言方式：关键词、规则、JSON Schema、相似度、人工标注、业务规则、拒答策略。
- 评估集：Golden Dataset、Bad Case 回流、分层采样、版本对比、稳定性回归。
- 风险：幻觉、上下文丢失、知识召回错误、格式漂移、敏感信息泄露、工具误调用。

简历关联：

- 你的实习经历中沉淀了 100+ 条对话回归样例，这是非常适合深挖的亮点。
- 你可以把 AI 测试讲成“传统自动化测试 + 非确定性输出评估”的结合。

推荐资源：

- [Ragas 文档](https://docs.ragas.io/en/stable/)
- [LangChain RAG 教程](https://docs.langchain.com/oss/python/langchain/rag)
- [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals)

## 阶段七：游戏测试专项

必须掌握：

- 游戏模块：登录、角色创建、任务、背包、装备、商城、抽卡、邮件、好友、匹配、战斗、结算、排行榜、充值、活动。
- 游戏专项：兼容性、弱网、断线重连、热更新、资源加载、崩溃、卡顿、帧率、内存泄漏、存档、反作弊、时区、本地化。
- 客户端定位：日志、崩溃堆栈、Android logcat、设备信息、包体版本、资源版本、复现视频。
- 引擎基础：Unity 的 EditMode/PlayMode Test、Unreal 的 Automation System、基础场景/Prefab/Actor/组件概念。

简历迁移：

- 接口自动化可迁移到游戏服务端接口、账号、背包、商城、活动和支付回调测试。
- UI 自动化可迁移到登录流程、设置页面、商城购买、邮件领取等稳定界面。
- 性能压测可迁移到登录洪峰、匹配队列、战斗结算、排行榜刷新等服务端场景。
- AI 测试可迁移到智能 NPC、客服、UGC 审核、文本生成和玩家反馈分析。

推荐资源：

- [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)
- [Unreal Engine Automation System](https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-system-in-unreal-engine)
- [Android 游戏开发与性能文档](https://developer.android.com/games)

## 每周复盘模板

| 问题 | 记录 |
|---|---|
| 本周补齐了哪 3 个核心知识点？ |  |
| 本周是否完成至少 1 个可展示小案例？ |  |
| 本周哪个简历项目被讲得更深？ |  |
| 是否新增 3 个 Bad Case 或缺陷定位故事？ |  |
| 游戏测试专项是否产出测试用例或复盘文档？ |  |
| 下周最需要补的短板是什么？ |  |

