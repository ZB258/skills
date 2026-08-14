# 可信度分级 + 诚实约束

## 诚实（最重要）

- **严禁臆造**引用、数字、指标、实验结果。不确定就标 `[unverified]` 并询问。
- 始终区分"来源 X 称"与"我的假设"。
- 每个论断须可溯源：指向 `literature/`、`analysis/`、或 `experimental_results/`；否则标 `[hypothesis]` / `[TODO]`。

## 可信度分级（每篇报数必标）

> ⚠️ **论文/笔记里写了"开源:✓" ≠ 真开源。** 很多仓库是空壳、仅 README、或"coming soon / to be released"。判定 A 之前**必须实际查仓库**（目录列表、大小、最后推送、README），确认含可用代码。

| Tier | 条件（**核实，而非假设**） | 处理 |
|------|-----------|----------|
| **A** | 仓库经核实含可用**代码**（真实 train/model 脚本，非仅 README） | 数字可直接使用 |
| **B** | 部分：数据集公开但**无方法代码**，或代码不全，或开源但单源/未复现 | 可用，但标"自行复现后再锚定" |
| **C** | 无可用产物：无仓库、空壳/仅 README 且无数据、"to be released" | **仅作上界参考——绝不作硬比较锚点**，除非自复测 |

### 审计示例（SAR 领域，2026-08 核实）

仅作分级**判据示范**，替换为你自己领域的核实结果：

- **A**（实码确认）：SARVLM, SAR-TEXT, SARLANG-1M, SAREval, SARCLIP-Jiang, Sentinel2Cap, SARATR-X, EarthDial。
- **B**（数据开源，无方法代码）：FSAR-Cap（数据集在 scidb.cn；仓库仅 README）、EarthGPT（MMRS-1M 已发布，无模型代码）。
- **C**（无可用产物）：DGS-CapNet（根本没有代码仓库）、MM-RSVQA（所引链接是另一个项目页）。
