---
name: reviewer-response
description: 期刊修回（major/minor revision）的逐条审稿意见回复交付：先复核（拆子点、核数字/表号/页码/完整性/礼貌性），再按合作者/目标文档体例生成可直接粘贴进回复信 docx 的 Word 片段（About 引导分点 ≤3–4、三线表、矢量图 EMF）+ HTML 交付页。用户说"处理这条审稿意见""按回复交付页流程"、粘贴审稿意见要求回复、或要求"给我能放入 docx 的回复"时使用。
---

# 审稿意见回复（Rebuttal）交付流程

适用场景：已有修改稿与底层数据，需要为单条审稿意见产出定稿回复。产出三件套：Word 片段（粘贴入回复信外壳）、HTML 交付页（核查结论 + 可复制回复）、md 源同步。

## 0. 输入

- 审稿意见原文（逐字）；
- 我方回复草稿（若有）；
- 修改稿最新版（LaTeX 源 + 编译产物 .aux/.pdf）；
- 底层数据文件（一切数字的权威来源，禁止凭记忆或推测填数）。

## 1. 复核（动笔前必做）

1. **拆子点**：从审稿人原句拆出其全部诉求（含隐含子点），逐点列清单。
2. **三方核对**：回复文字 ↔ 修改稿 ↔ 底层数据，每个数字、每处修改落点都要对上。
3. **表号/页码**：以最新编译版为准（.aux 的 label→编号/页 + PDF 文字层 fitz 复核）；并行排版会漂移，跨页段落用 pp. x–y；交稿前须按最终版统一复核。
4. **礼貌性**：感谢开头、不争辩、不同意时以证据平静说明；审稿人常只读回复文件——**汇总数字必须写进回复正文**。

## 2. 内容规则

1. **引导语 = 审稿人原句措辞**。分点用加粗 "About xxx." 开头，xxx 逐字或紧缩转述审稿人的提问（例：审稿人问 "clarify whether Figure 2 compares SAR-image counts or total pretraining samples" → "About whether Figure 2 compares SAR-image counts or total pretraining samples."）。**严禁自造审稿人未用过的抽象词**。
2. **如无必要不分点**：逻辑相近的子点提炼合并成段（例：R2-10 三点逻辑紧密即并成一段流畅回复）；确需分点才用引导语且 ≤3–4 个，逐数据一行点的清单式写法作废。**单一诉求意见、简单意见一律纯段落作答且从简**，不长篇大论。行文避免拗口叠词（"image retrieval—cross-modal image-text retrieval" 类直接简化）。
3. **笔风**：多句流畅的解释性段落，数字嵌入行文；先顺着审稿人的话认可或澄清，再给证据，最后指向稿件落点。忌一行式数据点。
4. **图文并茂**：短要点 + reproduced 数据表（注明 "Reproduced from Table X of the revised manuscript"）+ 必要的矢量图。
5. **自包含按 venue 区分**：**期刊（journal）回复必须自包含**——关键统计与 exhibit 嵌入回复（汇总数字写进正文、表/图 reproduced），不能只指向稿件；宽表确实无法复现时，也须先把汇总数字完整写入正文再指向全表。**会议（conference）回复允许直接引用文章的图、表**（指向稿件图表为常态，可不复现）。
6. **exhibit 编号**：reproduced 稿件对象 → 沿用**原文标号 + 原 caption 逐字**（+ Reproduced 尾句，有增改行须注明 added）；response 新增 exhibit → "Table A-xxx / Figure A-xxx" 占位（黄色高亮，汇编时统一定号）。
7. 人称：第一人称复数（we），对审稿人第二人称（you/your）。

## 3. Word 片段排版规格（从目标 docx 逐项核实所得；换目标文档须重新核实再沿用）

- **字体**：Times New Roman + 宋体（eastAsia）12pt。
- **正文段**：左缩进 420 twips、首行不缩进、两端对齐（jc=both）、段后 8pt、行距 ≈1.08（259 auto）；**无 bullet/编号列表**。
- **三线表**：表级边框全 none；表头单元格上下 single sz=8；末行底线 sz=8（强调行上方可加一条）；无竖线、无底纹；单元格水平垂直居中、段距 0 + 单倍行距；表左缩进 tblInd≈421 twips、宽 ~7943 twips；加粗行（final/Total）用 run 级 bold。
- **表 caption 在表上方**：正文式段落，"Table X." 加粗 + 说明普通体；**表下注 9pt**。
- **图必须矢量，禁止位图**：matplotlib 无 EMF 后端，也不指定转换器——**默认路径 = `savefig('fig.svg')` + Word 2016+ 直接插入 SVG**（原生矢量，docx 以 svgBlip 存储）；python-docx 片段在图位留"插入 fig.svg"占位行，由汇编者插入；需要 EMF 时由汇编者工具链自行转换。**禁止位图 PNG/JPG**（含 300 dpi 高分辨率位图）。图建议居中；图注为正文式段落（12pt，"Figure X." 加粗，首句加粗沿用稿件图注体例）。
- 生成工具 python-docx；生成后自验：表数、About 引导数（≤4）、0 列表段、两端对齐段数、图为矢量（SVG 占位或 EMF）。

## 4. 交付三件套

1. **Word 片段**：`reply_<RxCy>_response_block.docx`（被 Word 占用时另存 _v2 并提示清理旧版）。
2. **HTML 交付页**：`reply_<RxCy>_to_collaborator.html`——自包含单文件（双主题 CSS token、图以 base64 内嵌、复制按钮 ClipboardItem 双载荷 text/html + text/plain 保表格格式）；固定分区：核查结论 / 英文终版（可复制）/ 交付物清单。
3. **源同步**：回复 md 源同步终版；口径与裁决记入项目记档文件；**交付新版后检查回复信外壳 docx 中已贴入的旧版贴块并同步**。

## 5. 实战踩坑清单

- 页码/表号随并行排版漂移——引用前查最新 .aux；附录重排常使 p.30→31→32。
- docx 合并单元格会带入空段——merge 后清理多余空段落。
- OOXML `<w:b/>` 无 val = 加粗开启，`w:val="0"` = 关闭——核实格式必须看 val 属性。
- 目标文档里的嵌入图未必是原文图表——读 EMF 元数据（Inkscape 源文件名）先核实再决定 reproduced 口径。
- bash heredoc 长脚本易被截断——脚本落盘再执行。
- docx 被打开时保存报 PermissionError——捕获后另存 vN。
- 审稿人给的参考文献编号 [1][2] 要在回复中显式认领（作者+年份+venue），并核对 bib 作者列表。
