# 学习主线与阶段规划

## 目标画像

这份规划服务于两个岗位画像：

- 算法工程师：要求算法题、机器学习、深度学习、NLP/LLM 原理、实验评估都能讲清楚。
- AI 应用开发工程师：要求 RAG、Agent、Text-to-SQL、工具调用、服务封装、部署压测、业务闭环能落地。

你的简历不是“从零找方向”，而是已经有 LLM 应用项目。学习重点应放在三件事上：

- 把项目关键词背后的原理补实，例如 RRF、Rerank、LoRA、KV Cache、RAGAS、Text-to-SQL。
- 把算法与机器学习基础补到能过校招筛选。
- 把项目讲述从“我用了工具”升级为“我做了选择、验证了效果、处理了失败案例”。

## 12 周学习路线

| 阶段 | 时间 | 目标 | 主要内容 | 输出物 |
|---|---:|---|---|---|
| 快速补基础 | 第 1-2 周 | 守住算法题和 CS 基础 | 数据结构、常见算法、Python、MySQL、Redis、网络、Linux | 每天 2-3 题；整理错题；写一页 CS 八股速记 |
| ML/DL 基础 | 第 3-4 周 | 能回答传统算法和深度学习基础 | 监督学习、评估指标、过拟合、优化器、CNN/RNN/Transformer | 每类模型准备 3 个高频问答 |
| LLM 原理 | 第 5-6 周 | 能解释简历里的 Transformer、SFT、LoRA、PPO、vLLM | Attention、Tokenizer、预训练、微调、对齐、推理优化 | 写出 LoRA 与 KV Cache 的白板解释 |
| RAG / Agent 应用 | 第 7-8 周 | 把你的项目深挖到可面试 | RAG 流程、混合检索、Rerank、Agent Memory、Tool Calling、Text-to-SQL | 每个项目准备 10 个追问答案 |
| 工程部署 | 第 9-10 周 | 证明不是只会搭 demo | FastAPI、Docker、vLLM、并发、缓存、日志、压测、安全 | 准备项目架构图和接口链路图 |
| 面试冲刺 | 第 11-12 周 | 形成稳定输出 | 自我介绍、项目讲述、手撕题、模拟面试、复盘 | 录制 3 分钟项目讲解；完成 3 轮模拟面试 |

## 阶段一：快速补基础

### 数据结构与算法

必须掌握：

- 数组与字符串：双指针、滑动窗口、前缀和、差分。
- 哈希表：去重、计数、两数之和、最长连续序列。
- 栈与队列：单调栈、有效括号、表达式求值、滑动窗口最大值。
- 链表：反转链表、快慢指针、环检测、合并链表。
- 二叉树：递归/迭代遍历、层序遍历、最近公共祖先、路径和。
- 回溯：子集、排列、组合、括号生成、N 皇后。
- 动态规划：背包、打家劫舍、最长递增子序列、编辑距离。
- 图：BFS/DFS、拓扑排序、并查集、最短路。

面试要能讲：

- 时间复杂度和空间复杂度。
- 为什么选择 BFS 而不是 DFS。
- DP 的状态定义、转移方程、初始化和遍历顺序。
- 哈希、排序、堆、二分分别适合什么题型。

推荐资源：

- [代码随想录](https://programmercarl.com/)：按题型刷，适合校招冲刺。
- [Hello 算法](https://www.hello-algo.com/)：图解清楚，适合快速补结构化知识。

### 计算机基础

必须掌握：

- MySQL：索引、B+ 树、事务、隔离级别、MVCC、Explain、慢查询优化。
- Redis：String/List/Hash/Set/ZSet、过期策略、缓存穿透/击穿/雪崩、分布式锁基本思路。
- 网络：HTTP/HTTPS、TCP 三次握手四次挥手、拥塞控制、状态码、长连接。
- Linux/Docker：常用命令、镜像/容器/挂载/端口映射、日志查看、环境隔离。
- Python：装饰器、生成器、协程、GIL、常用数据结构、类型标注、异常处理。

简历关联：

- 你写了 FastAPI、Docker、MySQL、Redis、JMeter。面试官可能会从项目接口、部署、压测切入工程基础。
- 医药 Text-to-SQL 项目很容易追问 MySQL 执行计划、SQL 安全和索引。

推荐资源：

- [小林 Coding](https://www.xiaolincoding.com/)：网络、MySQL、Redis 的面试友好型资料。

## 阶段二：机器学习与深度学习基础

### 机器学习

必须掌握：

- 监督学习：线性回归、逻辑回归、SVM、决策树、随机森林、GBDT/XGBoost。
- 评估指标：Accuracy、Precision、Recall、F1、AUC、ROC、PR 曲线、混淆矩阵。
- 数据问题：样本不均衡、缺失值、异常值、数据泄漏、训练/验证/测试划分。
- 优化问题：梯度下降、学习率、正则化、早停、交叉验证。

面试常见问法：

- AUC 为什么对阈值不敏感？
- 过拟合如何判断和缓解？
- GBDT 和随机森林有什么区别？
- 分类任务中为什么只看 Accuracy 不够？

简历关联：

- 你的 RAG 项目用了 Hit Rate、执行成功率、RAGAS；客服项目用了业务采纳率。需要能解释这些指标和传统 ML 指标的区别。

推荐资源：

- [NLP-LOVE/ML-NLP](https://github.com/NLP-LOVE/ML-NLP)：适合面试前查 ML/NLP 高频题。

### 深度学习

必须掌握：

- 神经网络基础：前向传播、反向传播、激活函数、损失函数、优化器。
- 正则化：Dropout、Weight Decay、BatchNorm、LayerNorm。
- 序列模型：RNN、LSTM、GRU、Seq2Seq、Attention。
- Transformer：Self-Attention、Multi-Head Attention、FFN、残差连接、位置编码。

面试常见问法：

- Attention 的 Q/K/V 分别是什么？
- Transformer 为什么比 RNN 更适合并行训练？
- LayerNorm 和 BatchNorm 的区别是什么？
- Softmax 前为什么除以 `sqrt(d_k)`？

推荐资源：

- [动手学深度学习](https://zh.d2l.ai/)：建议看 Transformer、注意力机制、优化器章节。
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/)：适合补 NLP 系统知识。

## 阶段三：LLM 原理

必须掌握：

- Tokenizer：BPE、WordPiece、SentencePiece、词表、上下文长度。
- 预训练：Causal LM、Masked LM、Next Token Prediction。
- 微调：SFT、LoRA、QLoRA、Adapter、Prompt Tuning。
- 对齐：RLHF、PPO、DPO、Reward Model 的基本思想。
- 推理：KV Cache、连续批处理、PagedAttention、量化、吞吐和延迟。

简历关联：

- 你写了 Qwen 微调、SFT/PPO、LoRA、vLLM、KV Cache。任何一个都可能被追问到原理。

重点回答模板：

- LoRA：冻结原模型权重，只训练低秩矩阵近似权重增量，降低显存和训练成本；适合领域话术、风格、格式和轻量知识注入，但不适合大规模事实知识更新。
- KV Cache：自回归解码时缓存历史 token 的 K/V，避免每生成一个 token 都重复计算前文注意力；能降低解码阶段计算量，但占用显存并受上下文长度影响。
- 连续批处理：动态把不同请求的解码步骤合并执行，提高 GPU 利用率；挑战是请求长度不同、缓存管理复杂。

推荐资源：

- [Stanford CS336](https://stanford-cs336.github.io/spring2025/)：系统理解语言模型训练和推理。
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)：适合工程实践和模型生态。
- [Qwen Docs](https://qwen.readthedocs.io/en/latest/)：准备 Qwen 相关微调、部署和推理问题。
- [vLLM Docs](https://docs.vllm.ai/en/latest/)：准备 vLLM、PagedAttention、服务部署问题。

## 阶段四：RAG / Agent / Text-to-SQL

### RAG

必须掌握：

- 数据处理：清洗、分块、元数据、去重、版本管理。
- 召回：BM25、Embedding、混合检索、向量索引、TopK。
- 融合：RRF、加权融合、规则过滤。
- 精排：Cross-Encoder Rerank、LLM Rerank。
- 生成：Prompt 模板、引用约束、结构化输出、拒答策略。
- 评估：Recall@K、MRR、NDCG、Faithfulness、Context Precision、人工 Bad Case。

简历关联：

- 医药问答项目：Schema 检索、SQL 生成、RAGAS、Golden Dataset。
- 客服项目：Dense/BM25 双路召回、RRF 融合、Rerank 精排。

推荐资源：

- [LangChain RAG](https://docs.langchain.com/oss/python/langchain/rag)
- [Milvus Docs](https://milvus.io/docs)
- [Ragas Docs](https://docs.ragas.io/en/stable/)
- [Datawhale LLM Universe](https://github.com/datawhalechina/llm-universe)

### Agent

必须掌握：

- Planning：任务分解、步骤选择、ReAct。
- Tool Calling：工具 schema、参数校验、错误重试。
- Memory：短期上下文、长期摘要、结构化状态、向量记忆。
- Guardrails：权限、安全、拒答、工具调用白名单。
- 多 Agent：角色分工、消息协议、冲突解决、成本控制。

简历关联：

- 客服项目中的“短期记忆 + 长期摘要 + 结构化状态”。
- 多模态家电项目中的“图片识别--联网搜索--字段抽取--置信度校验”多 Agent 流程。

推荐资源：

- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction)
- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- [Lilian Weng: LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)

### Text-to-SQL

必须掌握：

- Schema Linking：问题中的实体、指标、时间、枚举值映射到表和字段。
- SQL 生成：Prompt、Few-shot、CoT、语法约束、方言差异。
- 执行验证：预执行、错误回传、自修正、结果校验。
- 安全：只读账号、SQL 白名单、表/字段权限、敏感字段脱敏、超时限制。
- 评估：执行准确率、语法正确率、结果一致性、人工验收。

简历关联：

- 你的医药项目是最容易被深挖的 Text-to-SQL 项目，建议准备一张链路图。

## 阶段五：工程部署与交付

必须掌握：

- FastAPI：路由、Pydantic、依赖注入、异常处理、流式响应、异步。
- Docker：镜像构建、环境变量、卷挂载、GPU 容器基础。
- 服务稳定性：超时、重试、限流、熔断、日志、监控、告警。
- 性能压测：QPS、TP50/TP95/TP99、吞吐、并发数、JMeter 压测口径。
- 数据安全：API 鉴权、数据库只读、Prompt Injection 防护、工具调用边界。

简历关联：

- 你写了 FastAPI 封装、JMeter 压测、Docker 部署、vLLM 推理服务。面试官会用这些判断你是否具备交付能力。

推荐资源：

- [Dify Docs](https://docs.dify.ai/)
- [vLLM Docs](https://docs.vllm.ai/en/latest/)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals)

## 每周复盘模板

每周末用下面问题检查自己：

- 本周我能不能独立讲清 3 个核心概念？
- 本周是否至少完成 10 道算法题并复盘错题？
- 简历里是否有 1 个项目点被我讲得更深？
- 有没有把一个“工具名”升级为“原理 + 选择理由 + 效果验证”？
- 有没有形成可面试输出，例如一段 3 分钟项目讲述或一页白板图？

