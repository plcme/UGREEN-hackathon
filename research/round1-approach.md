# Round 1 方案调研与计划（PDF + Skill ZIP）

> 依据：`cursor/ugreen-organizer-info-ca0f` 分支上的主办方资料（organizer-info/*.md）+ 2026-11-04 网络调研。
> 本文是**方法论与执行计划**，不包含最终创意。主办方 FAQ 建议"项目命名、PDF 回答、核心创意"由人完成，AI 只辅助。

## 0. 先搞清楚：这里的 "Skill" 到底是什么

和常见的"写个插件 / 写个脚本"完全不同：

- Skill = **一个 Markdown 工作流描述**（`SKILL.md` + 可选 `references/*.md`），**禁止**任何脚本、可执行文件、manifest。
- 真正干活的是 NAS 上**已注册的 expert agent**。Skill 只能写 `delegate --target <agent-id> --instruction '<task>'`，不能直接 `cli.invoke`。
- 每一步只能用 `capability-catalog.json` 里存在的 CLI capability；"没有就明说不支持"。
- 必须处理五种状态：`completed / failed / cancelled / waiting_user / waiting_approval`；删除/移动/覆盖/外发前必须确认。
- `SKILL.md` 模板章节：Goal / Required input / Capability evidence / Expert orchestration / Completion and failure。

**结论：这是一个"Agent 工作流编排设计"比赛，不是写代码比赛。** 拉开差距的地方在：选题、跨能力域的编排、确认关口和失败处理、文档严谨度。

## 1. 可借鉴的方法论

| 方法论 / 来源 | 核心思想 | 在本项目中的用法 |
|---|---|---|
| **Agent Skills 开放标准**（agentskills.io，Anthropic `anthropics/skills`） | Progressive disclosure：frontmatter 常驻 → SKILL.md 触发时加载 → references 按需加载；`description` 决定能否被正确触发；正文精简，细节放 references；"Gotchas" 段价值最高 | Uliya 的格式几乎就是这个标准的子集。`description` 要写清"何时用 / 产出什么"；主流程 ≤ 1 屏，细节拆到 `references/` |
| **Anthropic《Building Effective Agents》五种模式** | Prompt chaining（带 gate）、Routing、Parallelization、Orchestrator-workers、Evaluator-optimizer；"先用最简单的模式" | Skill 的 "Expert orchestration" 本质就是 **prompt chaining + gate**（每步用上一步真实输出、在 gate 处 `waiting_approval`）。可在 PDF Q7 里直接点名所用模式，显得设计有据 |
| **skill-creator 的 eval 循环**（Executor + Grader，`evals.json`） | 先写测试 prompt 与期望输出，再迭代 Skill | 直接对应 PDF **Q9（2 个核心用例 + 1 个边界用例）**：先写用例，再写 Skill，用 kit 自带 `check-skill.mjs` 做静态检查迭代 |
| **JTBD + 选题打分矩阵** | 用户在什么场景"雇佣"这个工具；按痛点强度 × 频率 × 可行性打分 | 用评审四项标准做打分矩阵（见 §3），四项**等权**，并列时按 User Value 优先 |
| **Human-in-the-loop / dry-run 模式**（Paperless-ai、Facet、PixCull 等都用） | 先给预览/报告，用户确认后再执行破坏性操作 | 天然契合"删除/移动前必须确认"的硬性规则，也是 Technical Quality 的加分项 |

## 2. 同类开源 / 商业方案（用于选题与 Q5 "差异化"）

| 赛道 | 现有方案 | 它们的局限 → 我们的机会 |
|---|---|---|
| 文件 / 文档自动化 | Paperless-ngx + paperless-ai / paperless-gpt（OCR、自动打标签、MCP server 已有多个）；QNAP Qsirch RAG 搜索 | 都是**单一 App、单一域**；需要部署 Docker、配 API token。Skill 可**跨域串联**（文档 + 知识库 + 文件整理）且零部署 |
| 照片回忆 | Immich（CLIP 语义搜索、人脸）、PhotoPrism、Synology Photos、QuMagie | 擅长"搜"和"分组"，不擅长"讲故事/按意图生成成果物"（如：带摘要的旅行相册 + 行程文档） |
| 创作者媒体 | Facet、PixCull、Nítido、fineshyt（连拍/模糊/重复筛选，dry-run） | 都是独立工具、需本地安装；NAS 上的 Skill 可在素材原地完成"筛选 → 打标签 → 归档 → 生成审片清单" |
| Skill 市场 | OpenClaw / ClawHub（上万个 skill，file-manager、organise-photos 等）| 大量 skill **因权限/安全被 flag**——这正是我们的差异点：显式权限、确认关口、数据不出 NAS |

**差异化公式（Q5 可用）：** 现有工具 = 单域 + 自动化；我们 = **跨 ≥2 个 NAS 能力域串联 + 每个高风险步骤可确认 + 数据本地处理（隐私）+ 产出一个可用成果物**。

## 3. 选题打分矩阵（评审四项等权，1–5 分）

| 维度 | 自问 |
|---|---|
| User Value | 真实、高频的痛点？结果是一个"拿来就能用"的东西吗？ |
| Innovation & Differentiation | 和 Immich/Paperless/Qsirch/ChatGPT 直接做有何本质不同？（另有 2×$5k "Most Creative" 只看这一项） |
| Technical Quality | 每一步都能映射到 catalog 里的真实 capability？确认/失败分支清晰？ |
| AI NAS Fit | 必须依赖 NAS 上的本地数据/存储/算力/隐私吗？还是"随便哪儿都能跑"？ |

额外过滤条件（不满足直接淘汰）：
1. 所有步骤在 `capability-catalog.json` 里能找到对应 capability；
2. 至少串联 2 个能力域（Files / Albums / Documents / Knowledge / Video·Music / Surveillance）；
3. 能写出 2 个核心用例 + 1 个边界用例；
4. 不需要把敏感数据发到外部服务。

## 4. Round 1 执行计划

截止：**2026-11-15 23:45 PT = 悉尼时间 11-16（周一）18:45**。注意：ai.ugreen.com 活动页写的是 11:59 PM PT，以官方规则 23:45 为准。

| 步骤 | 内容 | 产出 |
|---|---|---|
| 1 | 下载 `uliya-skill-kit-0.7.3-en.zip`，放入 Claude 的 skills 目录；通读 `docs/skill-development-standard.md`、`data/capability-catalog.json`、`references/examples/*` | 能力清单表（agent-id ↔ CLI ↔ action） |
| 2 | 头脑风暴 5–8 个想法（**由人主导**），用 §3 矩阵打分，选 1 个；选赛道 | 选题 + 一句话描述 |
| 3 | 先写 eval：2 个核心用例 + 1 个边界用例（对应 Q9） | `references/test-cases.md` |
| 4 | 用 kit 生成 SKILL.md（"Do not generate any files yet…" → 生成 → "Help me check this skill." 循环至无必改项） | Skill 文件夹 |
| 5 | 补齐披露：第三方组件/许可证、AI 工具及用途、本次黑客松新开发的功能 | `references/disclosures.md`（从 SKILL.md 直接链接） |
| 6 | 写 PDF：10 题合计 ≤ 500 英文词，≤ 1 MB；每题对齐评审标准 | proposal.pdf |
| 7 | 打包自检：ZIP 与解压后均 ≤ 10 MB、单文件 ≤ 1 MB、≤ 100 文件、无脚本/凭据/TODO/TBD | skill.zip |
| 8 | Devpost 提交草稿（提前 1–2 天），截止前再更新 | 提交完成 |

### PDF 500 词预算建议

| 题号 | 词数 | 备注 |
|---|---|---|
| Q1 一句话 | 25 | |
| Q2 用户与问题 | 50 | |
| Q3 方案 | 50 | |
| Q4 核心流程 | 60 | 可配一张流程图（图不占词数） |
| Q5 差异化 | 60 | 用 §2 公式 |
| Q6 用到的 NAS 能力及步骤 | 50 | 表格：步骤 → capability → agent |
| Q7 技术方案 | 80 | 点名编排模式、权限、模型选择（优先本地模型）、数据流 |
| Q8 开发现状 | 40 | 已完成 / 未完成 / 待 NAS 验证 |
| Q9 验证计划 | 50 | 2 核心 + 1 边界 |
| Q10 限制与风险 | 35 | |

## 5. 风险

- **当前云端环境无法访问 `cdn.shopify.com` / `ai.ugreen.com` / `skills.ugreen.com`**，拿不到 capability catalog —— 选题必须等看到 catalog 后再定。
- Round 1 评审可能用 AI 自动分析，文档结构要清晰、关键词与评审标准对齐。
- Round 2 分数不继承，Round 1 里承诺的功能必须真能在 NAS 上跑通 —— 不要过度承诺。

## 参考来源

- Agent Skills 最佳实践：https://geminicli.com/docs/cli/skills-best-practices/ ，https://www.newsletter.swirlai.com/p/agent-skills-progressive-disclosure
- Anthropic skill-creator：https://github.com/anthropics/skills （skills/skill-creator）
- Building Effective Agents 模式综述：https://docs.spring.io/spring-ai/reference/api/effective-agents.html
- Paperless-ngx AI 方案：https://blog.admin-intelligence.de/?p=7226 ，https://lobehub.com/pl/mcp/nloui-paperless-mcp
- QNAP Qsirch AI/RAG 搜索：https://www.qnap.com/go/solution/qsirch
- 照片筛选开源工具：https://pypi.org/project/pixcull/2.45.1/ ，https://qweliant.github.io/fineshyt/ ，https://github.com/brunoaclopes/nitido/releases
- ClawHub 生态：https://www.datacamp.com/blog/best-clawhub-skills ，https://clawhub.ai/skills/organise-photos
- UGREEN 活动页：https://ai.ugreen.com/pages/ugreen-hackathon
