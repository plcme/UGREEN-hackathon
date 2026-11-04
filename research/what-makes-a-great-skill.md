# 一个优秀的 Uliya Skill 应该是什么样子

来源（按权威性排序）：
1. **uliya-skill-kit 0.7.3**：`docs/skill-development-standard.md`、`references/*.md`、`assets/skill-template/SKILL.template.md`，以及检查器源码 `scripts/check-lib.mjs`（比赛"必须通过的检查"）。
2. **UGREEN SkillHub Content Submission and Publication Standards**（审核规范，api.ugnas.com）。
3. **Anthropic《Skill authoring best practices》**（platform.claude.com）：通用的 Skill 写作方法论。
4. 评审四项标准（Official Rules §6）。

---

## 1. 硬性规则：检查器会报 error 的（必须全部满足）

| 规则 | 检查器代码 | 怎么做 |
|---|---|---|
| frontmatter 只有 `name`、`description` | SKILL_FRONTMATTER_INVALID | 不要加其他字段 |
| name：小写字母数字加连字符，2–64 字符，**与目录名一致** | SKILL_NAME_* | 例如 `family-emergency-archive/` |
| description ≤ 1024 字符 | DESCRIPTION_LENGTH_EXCEEDED | |
| 四个必需一级标题 | SKILL_REQUIRED_SECTION_MISSING | `# Goal`、`# Required input`、`# Workflow`（或 `# Orchestration`）、`# Completion and failure` |
| 不能有 `TODO` / `TBD` / `replace-with-` / "待定" | SKILL_PLACEHOLDER_REMAINS | |
| 能力依据章节，格式严格 | CAPABILITY_EVIDENCE_* | 标题必须是 `# Generation-time capability evidence`，每行 ``- `ug-document` → `document-agent` ``（**用 → 箭头，两边反引号**），每个 CLI 只写一次 |
| 每个 delegate target 都要有对应的能力依据 | DELEGATE_TARGET_EVIDENCE_MISSING | |
| delegate 格式 | DELEGATE_FORMAT_INVALID | 单行，`delegate --target <agent> --instruction '<task>'`，**单引号**，不能有管道、反引号、`&&`，不能有其他 `--参数` |
| 只能用 6 个公开 agent | DELEGATE_TARGET_UNKNOWN | file-agent、document-agent、knowledge-agent、photo-agent、media-agent、security-monitor-agent |
| 正文必须出现全部 5 个状态词 | DELEGATION_RESULT_HANDLING_MISSING | `completed`、`failed`、`cancelled`、`waiting_user`、`waiting_approval` |
| 不能直接调用 `cli.invoke` | RUNTIME_DIRECT_CLI_INVOKE | 只能写"禁止 cli.invoke"这类否定句 |
| 安全扫描 | SECURITY_* | 不能有：凭据赋值、curl/wget、bash/python 代码块、`cp `/`mv `/`rm `/`cat ` 这类命令词、`/volume1`/`/mnt`/`/share` 这类 NAS 绝对路径、"bypass/skip … approval" 这类字样，也不能出现 `request-id` 这类内部标识 |
| references 链接必须存在 | RESOURCE_PATH_INVALID | |
| 包：≤100 个文件，单文件 ≤1MB，总共 ≤10MB，只能是 Markdown | PACKAGE_* / RESOURCE_UNSUPPORTED | |

### ⚠️ 官方模板和检查器对不上的两处（踩坑点）
- 模板写的是 `# Capability evidence` 加 `- <cli> -> <agent>`，**检查器只认** `# Generation-time capability evidence` 加 ``- `cli` → `agent` ``。
- 模板写的是 `# Expert orchestration`，**检查器的必需标题只认** `# Workflow` / `# Orchestration` / `# 专家编排`。
- Starter Kit 说包里"推荐"放 `README.md`，但检查器把根目录的 README.md 判为 RESOURCE_UNSUPPORTED（error，状态 not-uploadable）。**包里不能放 README.md**；说明文档放在包外。
→ 前两处都照检查器写：用 `# Workflow` 作为主标题，必要时在下面用二级标题 `## Expert orchestration`。

## 2. 警告级（不阻断，但评审和 AI 审阅会注意到）

| 警告 | 含义 | 我们的做法 |
|---|---|---|
| DESCRIPTION_TRIGGER_MISSING | description 没写"什么时候用" | 写上 `Use when the user …` |
| DESCRIPTION_EXECUTION_DETAIL | description 前半段写了执行顺序、保存位置、否定规则 | description 只写"产出什么 + 何时触发"，细节放正文 |
| DESCRIPTION_IMPERATIVE_STYLE | description 以"生成/创建/输出…"开头，像一条命令 | 用陈述句或名词短语开头，第三人称 |
| SKILL_BODY_LINES_RECOMMENDATION_EXCEEDED | 正文超过 500 行 | 主文件保持精简，细节拆到 references |
| RESOURCE_UNREFERENCED | references 里的文件没有被 SKILL.md 直接链接 | 每个 reference 都从 SKILL.md 直接链接，并说明何时读取 |
| DELEGATE_HARDCODED_HOME_PATH | instruction 写死了 `/home/某人` | 让专家自己解析用户目录（`get-user-dir`） |
| DELEGATE_DYNAMIC_VALUE_UNRESOLVED | instruction 里有 `<占位>` 或"上一步的结果"这类跨步指代 | 在正文说明运行时用上一步返回的真实值替换；instruction 本身写成自包含的任务 |
| EMPTY_RESULT_HANDLING_MISSING | 有查询类动作但没写"无结果怎么办" | 写明 "If no results / empty result: report it and stop; do not widen the scope" |
| DELEGATION_WORKFLOW_STATIC_VALIDATION_INCOMPLETE | 多次委托却没说明结果如何传递 | 写明 "downstream steps use only the real result returned upstream" |

## 3. 审核规范（UGREEN SkillHub Standards）里和我们相关的要点

- **描述必须与实际一致**（2.4）：凡是查询、写入、访问本地文件的动作都要在描述里**明确披露**。
- **禁止夸大用语**（2.2/2.3）：不能出现 best、only、official、certified、"absolutely safe"、free 这类词；不能冒充 UGREEN 官方。
- **权限最小化**（4.1/4.2）：只访问用户明确授权的路径。
- **涉及照片要说明必要性**（4.4）：我们会读照片里的文字，需要说明为什么。
- **高影响操作必须由用户确认**（4.6）：删除、移动、对外发送、改配置。
- **禁止持久化**（5.4）：调用结束即停止，不能注册定时任务（我们本来也没有这个能力）。
- **隐私**（7.1）：示例、日志、产出里不能带他人的个人信息 → 测试数据全部合成。
- **不能有空壳占位或自相矛盾的说明**（2.5）。

## 4. 通用方法论（Anthropic best practices）落到我们这里

| 原则 | 落地 |
|---|---|
| 简洁：模型已经很聪明，只写它不知道的 | 不解释"什么是保单"，只写**我们独有的规则**：清单、判断"即将过期"的阈值、确认点 |
| 自由度匹配风险 | 读操作给高自由度；**写操作（建文件夹、写索引、打标签）给低自由度**：精确的步骤和确认 |
| description 第三人称，写"做什么 + 何时用"，带关键词 | 带上 emergency documents、passport、insurance、will、medical records、expiry 等用户会说的词 |
| 渐进披露，reference 只链接一层 | SKILL.md 放主流程；`references/document-checklist.md`（清单）、`references/report-template.md`（输出模板）、`references/disclosures.md`（披露） |
| 超过 100 行的 reference 开头放目录 | 清单文件加目录 |
| 复杂流程给可勾选的 checklist | 在 Workflow 开头放一份进度清单 |
| 输出用模板 | 给出"已有 / 缺失 / 即将过期"报告的固定格式，保证每次输出一致 |
| 先写评测再写 Skill（至少 3 个场景） | 正好对应 PDF Q9：2 个核心用例 + 1 个边界用例，先写 `references/test-cases.md`（或放在仓库里、不进包） |
| 术语一致 | 全文统一用 document / member / missing / expiring，不混用同义词 |
| 不写会过时的信息 | 清单不写具体年份或政策细节 |
| 用多个模型测试 | Uliya 默认跑本地 Qwen3（较小的模型）→ 指令要写得更明确，不能只按 Opus 级别的理解力来写 |

## 5. 对照评审四项：优秀 Skill 的样子

| 评审项 | 优秀的表现 | 我们在 SKILL.md 里如何体现 |
|---|---|---|
| User Value | 清晰的问题 → 清晰的流程 → 有用的反馈 → 实在的结果 | 每一步都告诉用户进度；最终产出一页"应急档案索引"和一份缺口清单 |
| Innovation | 和普通 AI 工具、现有方案有实质不同 | "告诉你缺什么"，而不是"帮你找已有的"；按家庭成员组织 |
| Technical Quality | 编排合理、能力用得对、权限与错误处理完善、可重复运行 | 5 种状态全覆盖；空结果和部分结果有明确处理；写操作前确认；**重复运行时只更新、不覆盖**（幂等） |
| AI NAS Fit | 真正用到本地数据、存储、算力、隐私 | 本地 OCR、文档抽取、本地模型；文件不出 NAS；建好文件夹引导用户补齐 |

## 6. 需要额外确认的
- 已实际运行 kit 检查器验证上述规则（2026-11-04）。
- 清单内容依据：FEMA / Operation HOPE《Emergency Financial First Aid Kit》的四大类（Household Identification、Financial and Legal Documentation、Medical Information、Household Contacts）——需要做成国家无关、可由用户调整的版本。
