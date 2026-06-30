# 常考知识点清单

## 用法

每个知识点按三级掌握：

- A：能写代码或画流程图，能解释复杂度/原理/边界。
- B：能口头解释，能回答常见追问。
- C：只知道名词，需要补。

面试前把所有 C 降到 B，简历中出现的技术必须达到 A 或接近 A。

## JavaScript 与 TypeScript

| 模块 | 必会内容 | 面试要求 | 推荐练习 |
|---|---|---|---|
| 作用域/闭包 | 词法作用域、闭包用途、内存释放 | 能解释输出题和防抖节流 | 闭包计数器、防抖、节流 |
| 原型链 | `prototype`、`__proto__`、class | 能画对象查找链路 | 手写 `new`、继承 |
| `this` | 默认/隐式/显式/new 绑定 | 能判断箭头函数和普通函数差异 | 输出题、手写 `bind` |
| 异步 | Promise、async/await、事件循环 | 能解释宏任务/微任务顺序 | `Promise.all`、并发控制 |
| 数据结构 | Array、Object、Map、Set | 能说明适用场景 | 去重、计数、LRU |
| TypeScript | 泛型、联合类型、类型收窄、工具类型 | 能用于组件 props 和接口类型 | 写泛型请求函数、组件类型 |
| 模块化 | ESM、CommonJS、Tree Shaking | 能解释构建优化基础 | 分析按需引入 |

## HTML / CSS

| 模块 | 必会内容 | 高频追问 |
|---|---|---|
| 语义化 | 表单、列表、标题、可访问性 | 为什么不用全 `div`？ |
| 盒模型 | 标准盒、怪异盒、margin 合并 | `box-sizing` 有什么作用？ |
| BFC | 浮动、margin、独立布局上下文 | BFC 能解决哪些问题？ |
| Flex | 主轴、交叉轴、换行、对齐 | 如何做左右布局和居中？ |
| Grid | 网格轨道、自适应列 | 商品卡片列表如何布局？ |
| 定位 | relative、absolute、fixed、sticky | 弹窗、吸顶、角标怎么做？ |
| 层叠上下文 | z-index、transform、opacity | 为什么 z-index 不生效？ |
| 响应式 | 媒体查询、百分比、min/max | 移动端如何适配？ |
| 动画 | transform、transition、animation | 如何减少动画卡顿？ |

## Vue3 生态

| 模块 | 必会内容 | 和简历的关系 |
|---|---|---|
| 响应式 | `ref`、`reactive`、依赖收集 | ECharts 动态更新、表单状态 |
| `computed/watch` | 缓存、依赖、监听副作用 | 搜索筛选、图表配置更新 |
| 生命周期 | mount/update/unmount | 初始化图表、清理监听器 |
| 组件通信 | `props`、`emits`、插槽、`provide/inject` | 智能应用平台组件封装 |
| 自定义 hooks | 逻辑复用、状态隔离 | `useSSE`、`useTaskPolling` |
| Router | 动态路由、导航守卫、`meta` | 云端图像系统权限控制 |
| Pinia/Vuex | 全局状态、异步 action、持久化 | 用户信息、权限、会话状态 |
| 组件库 | Ant Design Vue、Element Plus | 表单、表格、弹窗、业务组件 |

## 浏览器与网络

| 模块 | 必会内容 | 高频追问 |
|---|---|---|
| 渲染流程 | DOM、CSSOM、布局、绘制、合成 | 重排和重绘区别？ |
| 事件机制 | 捕获、目标、冒泡、事件委托 | DOM 注入脚本如何监听点击？ |
| HTTP | 方法、状态码、Header、缓存 | 304、强缓存、协商缓存 |
| HTTPS | TLS、证书、加密 | 为什么 HTTPS 安全？ |
| 跨域 | 同源策略、CORS、代理 | 为什么浏览器限制跨域？ |
| Cookie/Token | 登录态、过期、安全属性 | Token 放哪里更安全？ |
| SSE | `EventSource`、单向推送、自动重连 | AI 流式输出为什么用 SSE？ |
| WebSocket | 握手、双向通信、心跳、重连 | 协同编辑如何保持连接？ |
| `postMessage` | 跨窗口通信、origin 校验 | iframe 通信安全边界 |
| 存储 | localStorage、sessionStorage、IndexedDB | 大量草稿数据放哪里？ |

## 工程化与测试

| 模块 | 必会内容 | 面试重点 |
|---|---|---|
| Vite | HMR、依赖预构建、生产构建 | 为什么开发快？ |
| 包管理 | npm/pnpm、lockfile、版本范围 | 依赖冲突怎么办？ |
| 代码规范 | ESLint、Prettier、提交规范 | 团队如何保持代码一致？ |
| 构建优化 | 代码分割、路由懒加载、按需引入 | 首屏体积如何降低？ |
| Mock/联调 | 代理、错误码、接口文档 | 前后端如何并行开发？ |
| 单元测试 | Vitest、纯函数、hook 测试 | 哪些逻辑适合单测？ |
| E2E 测试 | Playwright、关键流程 | 登录、发布、编辑如何测？ |
| Git | 分支、rebase/merge、冲突处理 | 多人协作如何管理？ |
| Docker | 镜像、容器、端口、环境变量 | 前端部署和环境一致性 |

## 性能优化

| 模块 | 必会内容 | 简历关联 |
|---|---|---|
| Core Web Vitals | LCP、INP、CLS | 性能指标表达 |
| 首屏优化 | 懒加载、预加载、图片压缩、缓存 | B 端系统首屏 |
| 运行时优化 | 防抖节流、虚拟列表、Web Worker | 列表、搜索、流式输出 |
| 图表优化 | 数据抽样、按需渲染、resize 防抖 | ECharts 看板 |
| 资源优化 | Tree Shaking、代码分割、CDN | Vite 构建 |
| 调试工具 | Performance、Network、Lighthouse | 卡顿定位 |

## 安全

| 模块 | 必会内容 | 高频追问 |
|---|---|---|
| XSS | 存储型、反射型、DOM 型 | 如何防止脚本注入？ |
| CSRF | Cookie 自动携带、Token 防护 | 为什么 SameSite 有用？ |
| 点击劫持 | iframe 覆盖、X-Frame-Options | 如何防止被嵌套？ |
| CSP | 资源白名单、脚本限制 | 如何限制不可信脚本？ |
| iframe sandbox | 权限限制、同源、脚本执行 | 预览站点如何隔离？ |
| `postMessage` | origin、消息 schema | 如何防止伪造消息？ |
| 权限控制 | 前端路由、后端接口 | 为什么前端权限不等于安全？ |

## 数据结构与算法

| 模块 | 必会内容 | 推荐练习 |
|---|---|---|
| 数组/字符串 | 双指针、滑窗、前缀和 | 两数之和、三数之和、最长无重复子串 |
| 哈希表 | 计数、去重、映射 | 前 K 个高频元素、LRU |
| 栈/队列 | 括号匹配、单调栈、BFS | 有效括号、每日温度、层序遍历 |
| 链表 | 反转、合并、快慢指针 | 反转链表、环形链表 |
| 二叉树 | 遍历、递归、路径 | 层序遍历、最近公共祖先 |
| 动态规划 | 状态定义、状态转移 | 爬楼梯、打家劫舍、LIS |
| 图 | BFS/DFS、拓扑 | 岛屿数量、课程表 |

## AI 应用型前端

| 模块 | 必会内容 | 和简历的关系 |
|---|---|---|
| 流式对话 | SSE、增量渲染、取消、重试 | 智能应用生成平台 |
| 工具调用轨迹 | 事件类型、步骤展示、错误状态 | AI 对话可解释性 |
| 实时预览 | iframe、沙箱、消息协议 | 网站生成预览 |
| 可视化编辑 | DOM 监听、选中态、样式编辑 | 点击即修改 |
| 异步任务 | 任务派发、轮询、状态机 | AI 扩图任务 |
| 协同编辑 | WebSocket、锁、冲突检测 | 云端图像协同 |
| 结构化输出 | JSON schema、低置信字段 | AI 实习接口联调 |

## 简历关键词自查

下面这些词已经出现在你的简历中，必须能回答到 B+ 以上：

- HTML5 / CSS3 / JavaScript / TypeScript
- Vue3 / Vue Router / Vuex / Pinia
- Ant Design Vue / Element / ECharts
- Git / Docker / Postman / JMeter / FoxAPI
- Django / Spring Boot / MyBatis / MySQL / SQLite / Redis
- SSE / EventSource / WebSocket / postMessage / iframe
- DOM 监听脚本 / 可视化编辑 / 实时预览
- 路由权限 / 全局守卫 / `meta.access`
- AI 辅助开发 / Claude Code / Codex / GitHub Copilot

## 反向检查：哪些词容易被问倒

优先补这些：

- `iframe`：不要只说能嵌页面，要能讲同源策略、sandbox、通信和安全。
- `postMessage`：必须讲 origin 校验和消息 schema。
- SSE：要知道它是单向推送，和 WebSocket 的场景不同。
- WebSocket：不能只说实时通信，要能讲心跳、重连、冲突和状态恢复。
- ECharts：要会讲实例生命周期、resize、销毁和大数据优化。
- Docker/JMeter：如果没深用，不要主动夸大；准备“前端如何参与环境部署/压测”的稳妥说法。
