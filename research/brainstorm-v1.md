# Brainstorm v1（2026-11-04）

约束回顾：只能用 9 个 CLI（见 capability-catalog-summary.md）；至少串 2 个 agent；写操作要确认；**不能解压缩、不能上网、不能定时**。
重要背景：UGOS Pro **已内置** Universal Search（自然语言语义搜索）和 Uliya 本地知识库问答 —— 单纯的"自然语言找文件"会和系统自带功能撞车，必须在其上做"组合 + 动作 + 场景"。

目标人群（按 NAS 买家调研）：A 家庭数字管家｜B 摄影/视频创作者｜C SOHO/自由职业/小房东。

| # | 名称 | 人群 | 一句话 | 流程（agent → 确认点） | 主要风险 |
|---|---|---|---|---|---|
| 1 | `memory-lane-finder` 回忆式找东西 | A/C | 用"我记得…"的模糊描述，跨文档、照片（含照片里的字）、文件时间去找，找不准就反问缩小范围，找到后可一键收拢 | document qa(semantic_lookup/locate_content) + photo search-picture(ocr-contains/时间/地点) + file find(日期/类型) → 结果过多则 waiting_user 反问 → 列候选+证据 → 确认后打标签或复制到一个文件夹 | 与内置 Universal Search 重叠；差异要靠"反问 + 跨类型 + 收拢动作" |
| 2 | `cloud-landing-tidy` 云盘搬家落地整理 | A | 把 iCloud/Google 导出的数据整理成 NAS 的样子 | file find(archive) → **不能解压，提示用户先解压** → scan-dedupe → file-workflow organize(按时间) → photo timeline/按地点建相册 → document 分类 → 每步确认 | 无解压能力；和官方"下载目录去重"示例接近 |
| 3 | `family-health-timeline` 家庭健康档案（TrackBite 血统） | A | 把散落在 PDF 和手机拍照里的全家体检报告，按人整理成时间线，标出跨年变化 | file find + photo search-picture(ocr-contains"体检/报告") → document extract(schema=medical-report) → document qa(comparison/period) → knowledge save-text 每人一份摘要（确认）→ 给原件打人名标签 | 医疗内容只能"整理/对比"，不能给诊断；需合成测试数据 |
| 4 | `warranty-and-proof-keeper` 保修/凭证管家 | A/C | 从小票照片、电子发票、保修卡里找出"买了什么、何时过保" | photo search-picture(ocr) + vision-ocr → document extract(receipt/invoice) → qa(period: 未来 90 天过保) → save-text 清单 + 打标签 | 与官方合同发票审计示例相近 |
| 5 | `package-arrival-check` 快递到了吗 | A/C | 把订单确认单/截图与门口摄像头的"包裹"事件对上，告诉你哪些到了、哪些没到 | document extract(purchase_order/receipt) 或 photo ocr 订单截图 → surveillance event-timeline(topic=Package, 时间窗) → event-evidence 截图 → knowledge save-text 对账结果 | 订单单据需已在 NAS 上；包裹事件无法对应具体是哪单（只能按时间窗匹配） |
| 6 | `rental-move-out-report` 退租/交房对比报告 | C（小房东/民宿） | 对比入住和退房时同一房间的照片，结合租约条款，起草一份损坏/状态报告 | photo search-picture(目录/时间) 取入住与退房两组照片 → vision-vlm 逐对描述差异 → document qa(租约中关于押金/损坏条款) → document writing(draft) → knowledge save-text（确认）；可选 surveillance 查搬出当天的人员/车辆事件 | vision-vlm 是单图提问，需要"分别描述再对比"；照片配对依赖目录规范 |
| 7 | `client-shoot-delivery` 摄影交付助手 | B | 一场拍摄结束后：按机身/镜头/时间建智能相册，挑出明显废片待审，生成客户交付说明 | photo search-screen(相机/镜头/目录) → create-album-condition（确认）→ 对抽样图 vision-vlm 评估"闭眼/虚焦"→ filemgr 打"待审"标签（确认）→ document writing 交付说明 → save-text | VLM 逐张调用慢，需限量；与 Facet/PixCull 方向相近 |
| 8 | `oral-history-book` 长辈口述回忆录 | A | 把和爷爷奶奶聊天的录音转写，按提到的年代和人物找出对应老照片，生成一份图文回忆录草稿和相册 | knowledge audio-transcription(多说话人) → document qa(抽取年份/人名/地点) → photo search-picture(人物/时间/地点) → create-album（确认）→ document writing(draft) → save-text | 老照片缺少 EXIF 时间；情感价值高、技术演示好 |
| 9 | `client-handover-pack` 客户资料打包 | C | 一句话把某个客户的合同、发票、往来文件、现场照片收集成一个交接包 + 摘要 | file find + document qa(按客户名) + photo search-picture(ocr/目录) → document reconcile → file mkdir + cpmv copy（确认）→ writing 摘要 | 与合同发票审计部分重叠 |

## 初步打分（1–5，四项等权；I=创新, F=NAS 契合）

| # | User Value | Innovation | Tech Quality(可行性) | NAS Fit | 合计 | 备注 |
|---|---|---|---|---|---|---|
| 1 | 5 | 3 | 4 | 4 | 16 | 需求最普遍，但要证明比内置搜索强 |
| 2 | 4 | 3 | 2 | 4 | 13 | 解压能力缺失是硬伤 |
| 3 | 4 | 4 | 4 | 5 | **17** | 隐私论证最强，和你的 TrackBite 经验直接相关 |
| 4 | 4 | 2 | 5 | 4 | 15 | 稳但撞官方示例 |
| 5 | 3 | 5 | 3 | 5 | 16 | 跨"监控 × 文档"的组合没人做过，冲 Most Creative |
| 6 | 4 | 5 | 3 | 5 | **17** | 明确的 B 端人群 + 三域串联，演示效果好 |
| 7 | 4 | 3 | 3 | 4 | 14 | 官方点名赛道，但开源竞品多 |
| 8 | 4 | 5 | 3 | 5 | **17** | 情感价值强、四域串联，适合 Track 2 |
| 9 | 4 | 2 | 4 | 4 | 14 | 实用但不出彩 |

打分为主观初评，需团队讨论后修正。
