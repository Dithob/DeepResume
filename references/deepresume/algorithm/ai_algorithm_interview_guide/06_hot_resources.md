# 热门视频、博客与文档资源地图

## 使用原则

资源不需要全看。按你的目标岗位，优先级是：

1. 先看能直接服务面试的问题：算法题、Transformer、RAG、Text-to-SQL、LoRA、vLLM。
2. 再看能支撑项目深挖的官方文档：LangChain、Dify、Milvus、Ragas、Qwen、vLLM。
3. 最后看扩展课程和博客，用来补系统性和表达深度。

## 算法刷题

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [代码随想录](https://programmercarl.com/) | 中文刷题路线 | 短期冲刺、校招笔试 | 按数组、链表、树、回溯、DP、图顺序刷；每题写复杂度和错因 |
| [Hello 算法](https://www.hello-algo.com/) | 图解教程 | 基础补弱 | 用来理解数据结构和算法原理，不替代刷题 |
| [LeetCode 热题 100](https://leetcode.cn/studyplan/top-100-liked/) | 题单 | 面试前 2-4 周 | 按题型复盘高频题，重点中等题 |

## 计算机基础

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [小林 Coding](https://www.xiaolincoding.com/) | 中文博客/图解 | 一面八股、工程追问 | 重点看 MySQL、Redis、网络；和你的 FastAPI/MySQL 项目结合 |
| [MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/) | 官方文档 | 遇到细节争议时查 | 查事务、索引、Explain、权限 |
| [Redis Docs](https://redis.io/docs/latest/) | 官方文档 | 缓存追问 | 查数据结构、过期策略、持久化、分布式锁边界 |

## 机器学习与深度学习

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [动手学深度学习](https://zh.d2l.ai/) | 中文书 + 课程 | 系统补 DL | 看优化器、CNN/RNN、Attention、Transformer |
| [跟李沐学 AI B站空间](https://space.bilibili.com/1567748478) | 中文视频 | 碎片时间补课 | 搜索“动手学深度学习”“Transformer 论文精读” |
| [Stanford CS224N](https://web.stanford.edu/class/cs224n/) | 课程 | NLP 系统补强 | 看 word vectors、RNN、Attention、Transformers |
| [Karpathy Zero to Hero](https://karpathy.ai/zero-to-hero.html) | 英文视频课 | 深度学习底层理解 | 看 micrograd、makemore、GPT from scratch、Tokenizer |

## 大模型原理

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [Stanford CS336](https://stanford-cs336.github.io/spring2025/) | 课程 | LLM 训练/推理系统 | 看 tokenization、architecture、training、inference |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | 教程 | 模型生态和工程实践 | 看 Transformers、datasets、fine-tuning、sharing |
| [Qwen Docs](https://qwen.readthedocs.io/en/latest/) | 官方文档 | 简历 Qwen 追问 | 查模型使用、部署、微调、推理方式 |

## RAG / Agent / Text-to-SQL

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [Datawhale LLM Universe](https://github.com/datawhalechina/llm-universe) | 中文实践教程 | RAG 入门到项目 | 按知识库问答、LangChain、向量数据库实践 |
| [LangChain RAG Tutorial](https://docs.langchain.com/oss/python/langchain/rag) | 官方文档 | RAG 项目复盘 | 对照你的医药项目补链路术语 |
| [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview) | 官方文档 | Agent 状态图 | 准备多 Agent、状态机、工具调用问题 |
| [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) | 课程 | Agent 基础 | 学工具调用、规划、观察、执行循环 |
| [Lilian Weng: LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) | 经典博客 | Agent 深挖 | 总结 Planning、Memory、Tool Use 三块 |
| [DeepLearning.AI Building and Evaluating Advanced RAG](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag) | 视频短课 | RAG 评估与进阶 | 看 RAG triad、sentence-window retrieval、auto-merging retrieval |
| [Milvus Docs](https://milvus.io/docs) | 官方文档 | 向量检索 | 查索引、相似度、集合、查询参数 |
| [Ragas Docs](https://docs.ragas.io/en/stable/) | 官方文档 | RAG 评估 | 查 faithfulness、context precision、answer relevancy 等指标 |

## 推理部署与工程化

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [vLLM Docs](https://docs.vllm.ai/en/latest/) | 官方文档 | 推理部署追问 | 重点看 serving、parallelism、KV cache、PagedAttention 相关说明 |
| [Dify Docs](https://docs.dify.ai/) | 官方文档 | 简历 Dify 追问 | 看 workflow、knowledge、tools、agent、API |
| [FastAPI Docs](https://fastapi.tiangolo.com/) | 官方文档 | 接口封装 | 看 Pydantic、异步、异常处理、依赖注入、流式响应 |
| [Docker Docs](https://docs.docker.com/) | 官方文档 | 部署基础 | 看 Dockerfile、compose、volumes、network |
| [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling) | 官方文档 | 工具调用 | 准备 tool schema、参数校验、结构化输出问题 |
| [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals) | 官方文档 | 评估体系 | 学会把模型输出评估做成可复现流程 |

## 面试与求职资料

| 资源 | 类型 | 适合阶段 | 怎么用 |
|---|---|---|---|
| [AI-Job-Notes](https://github.com/amusi/AI-Job-Notes) | 求职资料汇总 | 算法岗投递前 | 看算法岗常见准备模块，反推自己薄弱项 |
| [NLP-LOVE/ML-NLP](https://github.com/NLP-LOVE/ML-NLP) | ML/NLP 面试知识库 | 一面前 | 按 ML、DL、NLP 高频题查漏补缺 |
| [牛客网讨论区](https://www.nowcoder.com/discuss) | 面经社区 | 投递具体公司前 | 搜索“公司名 + 大模型算法 + 面经”或“AI 应用开发 面经” |

## 最推荐的精读组合

如果只选 10 个资源：

1. [代码随想录](https://programmercarl.com/)
2. [小林 Coding](https://www.xiaolincoding.com/)
3. [动手学深度学习](https://zh.d2l.ai/)
4. [Stanford CS224N](https://web.stanford.edu/class/cs224n/)
5. [Stanford CS336](https://stanford-cs336.github.io/spring2025/)
6. [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)
7. [LangChain RAG Tutorial](https://docs.langchain.com/oss/python/langchain/rag)
8. [DeepLearning.AI Advanced RAG](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag)
9. [vLLM Docs](https://docs.vllm.ai/en/latest/)
10. [NLP-LOVE/ML-NLP](https://github.com/NLP-LOVE/ML-NLP)

## 按岗位选择资源

AI 应用开发优先：

- LangChain RAG、Dify Docs、LangGraph、Ragas、vLLM、FastAPI。

算法工程师优先：

- 代码随想录、动手学深度学习、CS224N、CS336、NLP-LOVE/ML-NLP。

大模型应用算法优先：

- Hugging Face LLM Course、Advanced RAG、Lilian Weng Agent Blog、Qwen Docs、vLLM Docs。

