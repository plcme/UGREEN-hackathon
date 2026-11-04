# UGOS Skill 能力清单（摘自 uliya-skill-kit 0.7.3 `data/capability-catalog.json`，catalogVersion 2.0.0，2026-09-01）

> 原始 kit 未提交进仓库（受 SkillHub 协议约束），这里只是我们自己的摘要。精确参数以原 JSON 为准。
> approval：`none` 无需确认；`gateway`/`workflow`/`conditional` 需要用户确认（由平台子工作流执行）。

Skill 只能写 `delegate --target <agent> --instruction '<task>'`，一共 **6 个 agent / 9 个 CLI**：

| Agent | CLI | 读（无需确认） | 写（需确认） |
|---|---|---|---|
| file-agent | `ug-filesystem` | cat, category, find（按类型/大小/日期）, getfattr, ls, md5sum, sha256sum, stat | chtimes, cpmv(移动/复制), del, echo(写文件), mkdir, rename, restore, share-mkdir, touch |
| file-agent | `ug-filemgr` | mediainfo, scan-dedupe, tag-filter/get/list… | tag-add, tag-add-file, tag-delete, tag-set |
| file-agent | `file-workflow` | get-user-dir, start(organize/deduplication 预案，按类型/时间/大小/分辨率/时长) | run, batch-del, batch-move |
| document-agent | `ug-document` | page-count, metadata, **qa**(问答/抽取/对比/摘要/定位…), **extract**(schema: invoice/contract/expense/receipt/medical-report/purchase_order/mixed_reconciliation), **reconcile**(对账) | translate, writing(outline/polish/rewrite/draft/minutes…) |
| knowledge-agent | `ug-knowledge` | answer-official(查官方文档), **audio-transcription**(录音转写，可分说话人), collect-evidence | save-text(保存文本) |
| photo-agent | `ug-photo` | albums, album-detail, figure-albums(人物), object-albums, **search-picture**(人物/宠物/地点/物体/OCR 文字/时间/目录), search-screen(含相机型号/镜头), search-classify, meta, **vision-ocr**, **vision-vlm**(对单张图自定义 prompt 提问), health | create-album, create-album-condition(按地点/人物/相机/镜头/焦段/光圈/ISO/OCR 文字…), create-album-anniversary, create-album-baby, create-album-custom, timeline |
| media-agent | `ug-video` | search(影视/演员/类型…), subtitle-search | control(播放), subtitle-download |
| media-agent | `ug-music` | search | control(播放) |
| security-monitor-agent | `ug-surveillance` | cameras, **event-timeline**(人/人脸/车辆/宠物/**快递包裹**；熟人/陌生人), identity-resolve, event-evidence(截图/片段), faces, vehicle-plates | （全部只读） |

## 官方自带的 7 个示例（避免撞车）
1. 下载目录去重归档 2. 按人物/地点建相册（年度照片） 3. 监控异常事件查询 4. 找字幕 5. 搜音乐 6. 合同发票审计 7. 会议录音转纪要并保存
（另有 find-pdf-and-read-metadata、extract-conclusion-and-save 两个小示例）

## 值得注意的"冷门但强"的能力
- `ug-photo vision-vlm`：对任意一张图片用自定义 prompt 提问，等于本地多模态模型。
- `ug-photo search-picture --ocr-contains`：按照片里的文字搜照片（小票、白板、证件…）。
- `ug-photo create-album-condition`：按相机/镜头/焦段/光圈/ISO 建智能相册（摄影师向）。
- `ug-surveillance event-timeline --topic Package`：快递包裹事件。
- `ug-document extract --schema medical-report|receipt|expense` + `reconcile`：票据/体检报告结构化与对账。
- `ug-knowledge audio-transcription --speak-count`：多人录音转写。
- **没有**：网络请求/外部 API、日历/提醒、发邮件/消息、定时任务、智能家居控制、数据库。
