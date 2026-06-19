# 学习主线与阶段规划

## 目标画像

这份规划服务于三个岗位画像：

- Vue 前端开发：要求 HTML/CSS/JavaScript/TypeScript 基础扎实，能熟练使用 Vue3、Vue Router、Pinia、Vite 完成业务开发。
- B 端 / 可视化前端：要求组件抽象、表单表格、权限路由、接口联调、ECharts、复杂状态和工程化能力。
- AI 应用型前端：要求能开发流式对话、实时预览、`iframe` 沙箱、`postMessage` 通信、WebSocket 协同和模型任务状态追踪。

你的简历不是“从零找前端方向”，而是已经有 AI 应用前端、协同编辑、可视化和前后端联调项目。学习重点应放在三件事上：

- 把简历关键词背后的原理补实，例如 Vue 响应式、路由守卫、SSE、WebSocket、`postMessage`、`iframe`、DOM 事件、安全边界和渲染性能。
- 把前端基础补到能过校招筛选，尤其是 JS 输出题、手写题、浏览器、网络、CSS 布局和算法题。
- 把项目讲述从“我做了页面”升级为“我设计了状态流、处理了并发与异常、保证了体验和工程质量”。

## 12 周学习路线

| 阶段 | 时间 | 目标 | 主要内容 | 输出物 |
|---|---:|---|---|---|
| 前端基础夯实 | 第 1-2 周 | 守住 JS/CSS/浏览器基本盘 | JS 执行机制、闭包、原型、Promise、事件循环、CSS 布局、响应式 | 每天 1 组 JS 输出题；整理 CSS 布局速查 |
| Vue3 与组件化 | 第 3-4 周 | 能讲清 Vue 项目核心机制 | Composition API、响应式、组件通信、生命周期、Router、Pinia | 重构一个项目模块；画路由权限流程图 |
| 工程化与质量 | 第 5-6 周 | 证明能交付可维护项目 | Vite、模块化、ESLint、构建优化、Git、接口联调、Vitest/Playwright | 写一份项目工程化说明；补 3 个测试样例 |
| 浏览器、网络与安全 | 第 7-8 周 | 能回答一面八股和项目追问 | HTTP/HTTPS、缓存、跨域、Cookie/Token、XSS/CSRF、CSP、Web Storage | 整理一页网络与安全问答 |
| 性能与复杂交互 | 第 9-10 周 | 深挖简历亮点 | Core Web Vitals、懒加载、虚拟列表、WebSocket、SSE、`iframe`、`postMessage`、ECharts | 每个项目准备 10 个追问答案 |
| 面试冲刺 | 第 11-12 周 | 形成稳定输出 | 自我介绍、项目讲述、手撕题、模拟面试、复盘 | 录制 3 分钟项目讲解；完成 3 轮模拟面试 |

## 阶段一：前端基础夯实

### JavaScript / TypeScript

必须掌握：

- 作用域、闭包、原型链、继承、`this`、`call/apply/bind`。
- 事件循环、宏任务、微任务、Promise、async/await。
- 数组、对象、Map/Set、WeakMap/WeakSet、迭代器、生成器。
- 模块化：ESM、CommonJS、Tree Shaking 的基本思路。
- TypeScript：基础类型、联合类型、泛型、类型收窄、接口、工具类型、组件 props 类型。

面试要能讲：

- Promise 链式调用和异常传播。
- 为什么 `setTimeout`、Promise、`async/await` 输出顺序不同。
- 原型链和 class 的关系。
- TypeScript 如何提升组件接口稳定性。

推荐输出：

- 整理 30 道 JS 输出题，每题写执行顺序原因。
- 手写 `debounce`、`throttle`、`deepClone`、`Promise.all`、`LRU Cache`。

### CSS 与页面基础

必须掌握：

- 盒模型、BFC、层叠上下文、选择器优先级。
- Flex、Grid、定位、响应式布局、移动端适配。
- 常见布局：两栏/三栏、水平垂直居中、等高布局、瀑布流思路。
- 动画与过渡：`transition`、`animation`、`transform`，理解触发布局和合成的差异。

简历关联：

- 校园二手交易平台写了响应式布局，面试官可能问如何适配不同屏幕、如何组织商品卡片和列表布局。
- 智能应用生成平台有实时预览能力，可能追问 iframe 内页面如何缩放、如何适配移动端预览。

## 阶段二：Vue3 与组件化

必须掌握：

- Vue3 响应式：`ref`、`reactive`、`computed`、`watch`、依赖收集的基本思想。
- Composition API：组合逻辑、可复用 hooks、生命周期。
- 组件通信：`props`、`emits`、`provide/inject`、插槽、事件总线替代方案。
- Vue Router：动态路由、嵌套路由、导航守卫、权限元信息。
- Pinia/Vuex：全局状态、异步 action、持久化、模块拆分。

简历关联：

- 云端图像协同系统的 `meta.access` + `beforeEach` 是路由权限重点。
- 智能应用生成平台的 `props` / `emits` 和业务组件封装是组件化重点。
- ECharts 动态更新要能解释 Vue 响应式数据变化和图表实例更新之间的关系。

推荐输出：

- 画一张“登录态 -> 路由守卫 -> 权限判断 -> 页面渲染/重定向”的流程图。
- 从一个项目中抽出 2 个可复用 hooks，例如 `useSSE`、`useTaskPolling`、`useChartResize`。

## 阶段三：工程化与质量

必须掌握：

- Vite：开发服务器、HMR、依赖预构建、生产构建的基本流程。
- 包管理：npm/pnpm、依赖版本、lockfile、脚本管理。
- 代码规范：ESLint、Prettier、提交规范、Git 分支协作。
- 接口联调：OpenAPI/FoxAPI、Postman、错误码、Mock、代理、跨域。
- 测试：Vitest 单元测试、组件测试、Playwright E2E 基础。
- 构建优化：按需引入、代码分割、懒加载、静态资源压缩、产物分析。

简历关联：

- 你写了 Git、Docker、Postman、JMeter、FoxAPI，需要能讲这些工具如何服务前端交付，而不是只列工具名。
- AI 前端项目有接口流式响应和异步任务状态，建议准备错误处理、超时、重试和降级策略。

推荐输出：

- 为智能应用生成平台准备一份“接口联调与错误处理说明”。
- 为云端图像协同系统准备一份“异步任务状态机说明”。

## 阶段四：浏览器、网络与安全

必须掌握：

- 浏览器渲染流程：HTML 解析、CSSOM、渲染树、布局、绘制、合成。
- 网络：HTTP/HTTPS、状态码、缓存、Cookie、Token、跨域、CORS。
- 实时通信：轮询、SSE、WebSocket 的适用场景和限制。
- 存储：Cookie、localStorage、sessionStorage、IndexedDB 的差异。
- 安全：XSS、CSRF、点击劫持、CSP、`iframe sandbox`、`postMessage` origin 校验。

简历关联：

- SSE 与 WebSocket 都出现在简历中，必须能讲两者区别。
- `iframe` 和 DOM 注入天然涉及安全，必须主动讲同源策略、消息来源校验、脚本注入风险和沙箱限制。

推荐输出：

- 准备一张“AI 对话流式输出链路图”：浏览器 EventSource -> 后端 SSE -> token 增量渲染 -> 结束/异常处理。
- 准备一张“预览 iframe 通信链路图”：主应用 -> `postMessage` -> 子页面监听 -> 状态回传 -> origin 校验。

## 阶段五：性能与复杂交互

必须掌握：

- Core Web Vitals：LCP、INP、CLS 的含义和优化方向。
- 首屏优化：代码分割、路由懒加载、图片压缩、预加载、缓存。
- 运行时优化：虚拟列表、防抖节流、减少不必要渲染、Web Worker。
- 图表优化：按需渲染、resize 监听、数据抽样、大数据量渲染策略。
- 协同编辑：连接状态、心跳、重连、编辑锁、冲突检测、乐观更新和回滚。

简历关联：

- 云端图像协同系统可以从 WebSocket、编辑锁、冲突检测、ECharts 性能展开。
- 智能应用生成平台可以从 SSE、`iframe` 预览、DOM 监听、跨域通信和安全展开。

推荐输出：

- 每个项目准备 3 个 Bad Case，例如连接断开、任务超时、权限失效、预览页脚本注入失败、图表数据异常。
- 每个项目准备 2 个“如果重做会优化什么”的答案。

## 阶段六：算法题与手撕代码

前端岗位不需要把算法准备成算法岗强度，但校招筛选仍会考。优先掌握：

- 数组/字符串：双指针、滑动窗口、前缀和。
- 哈希表：计数、去重、缓存。
- 栈/队列：括号匹配、单调栈、BFS。
- 链表：反转、合并、快慢指针。
- 二叉树：遍历、层序、路径。
- 动态规划：爬楼梯、打家劫舍、最长递增子序列、编辑距离的思路。

前端高频手写：

- 防抖、节流、深拷贝、发布订阅、事件委托。
- `Promise.all`、`Promise.race`、并发限制。
- `Array.prototype.map/filter/reduce`。
- LRU Cache、模板字符串解析、扁平数组转树。

## 每周复盘模板

每周末用下面问题检查自己：

- 本周是否至少完成 10 道手写/算法题并复盘错因？
- 简历中是否有 1 个项目点被我讲得更深？
- 有没有把一个“工具名”升级为“原理 + 选择理由 + 异常处理”？
- 有没有形成可面试输出，例如一段 3 分钟项目讲述或一页流程图？
- 我能否用 30 秒解释 SSE、WebSocket、`postMessage`、Vue 响应式和路由守卫？
