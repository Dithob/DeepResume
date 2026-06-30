# 常考知识点清单

## 用法

每个知识点按三级掌握：

- A：能写代码或公式，能解释复杂度/原理。
- B：能口头解释，能回答常见追问。
- C：只知道名词，需要补。

面试前把所有 C 降到 B，简历中出现的技术必须达到 A 或接近 A。

## 算法与数据结构

| 模块 | 必会内容 | 面试要求 | 推荐练习 |
|---|---|---|---|
| 数组/字符串 | 双指针、滑窗、前缀和、差分 | 能判断窗口维护什么状态 | 最长无重复子串、最小覆盖子串、和为 K 的子数组 |
| 哈希表 | 计数、去重、映射、缓存 | 能解释空间换时间 | 两数之和、最长连续序列、LRU |
| 链表 | 反转、合并、快慢指针、环 | 能画指针变化 | 反转链表、环形链表、合并 K 个链表 |
| 栈/队列 | 单调栈、括号匹配、BFS | 能解释单调性和队列层次 | 有效括号、滑动窗口最大值、每日温度 |
| 二叉树 | 遍历、递归、路径、LCA | 能定义递归返回值 | 层序遍历、路径总和、最近公共祖先 |
| 回溯 | 选择、撤销、剪枝 | 能说明搜索树 | 全排列、子集、组合总和 |
| 动态规划 | 状态定义、转移、初始化 | 能从暴力递归推 DP | 背包、LIS、编辑距离、最长公共子序列 |
| 图 | BFS/DFS、拓扑、并查集、最短路 | 能建图并说明 visited/入度 | 岛屿数量、课程表、冗余连接 |
| 堆 | TopK、优先队列 | 能分析 O(n log k) | 前 K 个高频元素、合并 K 个链表 |

## 机器学习

| 模块 | 必会内容 | 高频追问 |
|---|---|---|
| 线性回归 | MSE、最小二乘、梯度下降 | 为什么对异常值敏感？ |
| 逻辑回归 | Sigmoid、交叉熵、决策边界 | LR 是线性还是非线性模型？ |
| SVM | 间隔最大化、核函数、软间隔 | 核函数解决什么问题？ |
| 决策树 | 信息增益、基尼系数、剪枝 | ID3/C4.5/CART 区别？ |
| 随机森林 | Bagging、特征采样、投票 | 为什么能降低方差？ |
| GBDT/XGBoost | Boosting、残差、二阶梯度 | 和随机森林区别？ |
| 聚类 | KMeans、层次聚类、DBSCAN | K 如何选？对异常点敏感吗？ |
| 评估指标 | Precision、Recall、F1、AUC、PR | 样本不均衡看什么指标？ |
| 数据处理 | 缺失值、异常值、归一化、数据泄漏 | 如何发现数据泄漏？ |
| 过拟合 | 正则化、Dropout、早停、交叉验证 | 训练好验证差怎么办？ |

## 深度学习与 NLP

| 模块 | 必会内容 | 高频追问 |
|---|---|---|
| 反向传播 | 链式法则、梯度、参数更新 | 梯度消失/爆炸怎么处理？ |
| 优化器 | SGD、Momentum、Adam | Adam 为什么常用？ |
| 激活函数 | ReLU、Sigmoid、Tanh、GELU | ReLU 死亡问题是什么？ |
| 正则化 | Dropout、Weight Decay、LayerNorm | LayerNorm 和 BatchNorm 区别？ |
| RNN/LSTM/GRU | 门控、长程依赖 | LSTM 如何缓解梯度消失？ |
| Attention | Q/K/V、缩放点积注意力 | 为什么除以 `sqrt(d_k)`？ |
| Transformer | MHA、FFN、残差、位置编码 | 为什么并行能力强？ |
| Tokenizer | BPE、WordPiece、SentencePiece | 中文 tokenization 有什么问题？ |
| BERT/GPT | MLM、Causal LM、Encoder/Decoder | BERT 和 GPT 架构差异？ |

## 大模型训练、微调与对齐

| 模块 | 必会内容 | 和简历的关系 |
|---|---|---|
| 预训练 | Next Token Prediction、语料、损失 | 理解 Qwen 等大模型基础 |
| SFT | 指令数据、格式学习、领域适配 | 客服话术微调 |
| LoRA | 低秩矩阵、冻结基座、target modules | 简历写了 LoRA 和 Qwen 微调 |
| QLoRA | 量化基座、低显存训练 | 可以作为扩展追问 |
| RLHF | Reward Model、PPO | 简历写了解 PPO，至少能讲思想 |
| DPO | 偏好对直接优化 | PPO 替代方案，了解即可 |
| Prompt | Few-shot、CoT、结构化输出 | RAG、Text-to-SQL 都依赖 |
| 幻觉抑制 | RAG、引用、拒答、校验、微调 | 客服项目和医药项目高频追问 |

## RAG

| 模块 | 必会内容 | 面试重点 |
|---|---|---|
| 文档清洗 | 去噪、去重、格式统一、版本管理 | 数据质量决定上限 |
| Chunk | 固定长度、语义切分、overlap | overlap 过大/过小的影响 |
| Embedding | 向量化、语义相似、归一化 | 为什么向量能检索语义？ |
| 向量索引 | Flat、IVF、HNSW | 召回率和速度权衡 |
| BM25 | 词频、逆文档频率、长度归一化 | 适合关键词和型号检索 |
| 混合检索 | Dense + Sparse | 简历客服项目核心 |
| RRF | 排名融合 | 为什么不用直接加分？ |
| Rerank | Cross-Encoder、重排 TopK | 精度和延迟权衡 |
| Query Rewrite | 上下文补全、同义改写 | 长轮对话和长尾 Query |
| 评估 | Recall@K、MRR、NDCG、RAGAS | 指标口径必须清晰 |

## Agent 与工具调用

| 模块 | 必会内容 | 和简历的关系 |
|---|---|---|
| ReAct | Reason + Act + Observation | Agent 基本工作范式 |
| Planning | 任务拆解、步骤控制 | 多 Agent 流程 |
| Tool Calling | schema、参数、错误处理 | AI 应用开发高频 |
| Memory | 短期上下文、长期摘要、结构化状态 | 客服项目核心 |
| 状态机 | 槽位、状态转移、终止条件 | 多轮客服流程控制 |
| 多 Agent | 角色分工、消息传递、冲突处理 | 家电识别项目 |
| Guardrails | 权限、白名单、拒答、审计 | Text-to-SQL 和联网搜索安全 |

## Text-to-SQL

| 模块 | 必会内容 | 高频追问 |
|---|---|---|
| Schema Linking | 实体、字段、表、枚举值映射 | 800 张表如何召回？ |
| SQL Prompt | Few-shot、CoT、方言约束 | 如何减少语法错误？ |
| Join 路径 | 外键、表关系图、业务规则 | 多表查询怎么处理？ |
| 预执行 | Explain、错误捕获、超时限制 | 自纠错怎么做？ |
| 自修正 | 错误回传、重试次数、差异记录 | 如何避免无限循环？ |
| 安全 | 只读账号、SQL 白名单、敏感字段 | 如何防止危险 SQL？ |
| 评估 | 执行成功率、结果准确率、人工验收 | 70% 到 90%+ 怎么算？ |

## 推理部署与工程

| 模块 | 必会内容 | 高频追问 |
|---|---|---|
| FastAPI | Pydantic、异步、异常、流式响应 | 如何封装模型服务？ |
| Docker | 镜像、容器、网络、卷、GPU | 如何保证环境一致？ |
| vLLM | KV Cache、连续批处理、PagedAttention | 为什么吞吐更高？ |
| 量化 | INT8/INT4、精度损失、显存节省 | 如何权衡性能和效果？ |
| 压测 | QPS、TP95、TP99、并发、错误率 | JMeter 怎么测？ |
| 日志 | trace id、请求日志、错误日志 | 如何定位线上问题？ |
| 缓存 | Redis、结果缓存、embedding 缓存 | 如何降低延迟和成本？ |
| 安全 | 鉴权、限流、Prompt Injection | 工具调用边界如何做？ |

## 简历关键词自查

下面这些词已经出现在你的简历中，必须能回答到 B+ 以上：

- Dify
- LangChain
- RAG
- Tool Calling
- Multi-Agent
- Agent Memory
- FastAPI
- Transformer
- Self-Attention
- SFT
- PPO
- LoRA
- Qwen 微调
- vLLM
- KV Cache
- 连续批处理
- MySQL
- Redis
- Docker
- Postman/JMeter
- Dense/BM25
- RRF
- Rerank
- RAGAS
- Golden Dataset
- Text-to-SQL
- OCR
- 视觉大模型
- Query Rewrite

## 反向检查：哪些词容易被问倒

优先补这些：

- PPO：如果只了解概念，不要装作做过 RLHF；能讲 PPO 在 RLHF 中的角色即可。
- Harness Engineering：这个表达不如 Prompt Engineering 常见，面试时要准备解释你具体指什么，否则可能被质疑。
- Open Claw、Hermes：如果不是主流 JD 高频工具，建议只作为了解，不要主动展开。
- RAGAS：要知道它适合评估什么，不适合单独证明 Text-to-SQL 正确性。
- vLLM：不能只说“优化推理”，要能讲连续批处理、KV Cache、PagedAttention 的作用。

