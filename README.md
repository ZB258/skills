# Codex Skills

This repository maintains reusable Codex skills. Each top-level skill directory is an independent skill package with its own `SKILL.md` and optional bundled resources such as scripts, references, assets, and UI metadata.

## Available Skills

### paper-reading-notes

`paper-reading-notes` helps Codex read research papers from PDF into polished Markdown notes. It emphasizes faithful method reconstruction, formulas in the paper's notation, integrated figures, reviewer-style analysis, and optional Better Notes/Zotero-friendly HTML export.

Bundled resources:

- `scripts/extract_pdf_images.py`: Extract embedded image objects from PDFs and write a `manifest.json`.
- `scripts/md_to_zotero_html.py`: Convert Markdown notes into Better Notes/Zotero-friendly HTML.
- `references/note-writing-rules.md`: Detailed note structure, figure handling, tone, and export rules.
- `references/review-lens.md`: Critical reading prompts for method, evidence, contribution, and reuse risk.

Script dependencies:

```bash
python -m pip install pymupdf markdown
```

### research-pipeline

`research-pipeline` is an agent-agnostic research workflow skill: discover research ideas from a literature corpus, then land them through A2B root-cause analysis and cross-domain transfer. Stage one (discover ideas): scaffold the project with Git branch rules, pick a reproducible baseline, batch-analyze top-conference papers, generate "surprise" experiments (MinerU → analysis-paper notes → deep-read problem-x-phenomenon cross matrix → squeeze-experiment), and locate a breakthrough via A2B. Stage two (implement ideas): pick a direction by impact-x-feasibility, drill A2B down to operator level, search other domains for existing solutions, and transfer them by creating the conditions they need.

Bundled resources:

- `references/workflow-manual.md`: faithful copy of the source methodology manual.
- `references/methodology-adjustments.md`: eight deliberate deviations from the manual that are part of the workflow and must be followed.
- `references/a2b-rules.md`: A2B analysis stages, fallback rules, and innovation grades a-d.
- `references/credibility-tiers.md`: honesty constraints and paper credibility tiers A/B/C.
- `pipeline/analysis-paper/SKILL.md`: self-contained sub-skill that turns a paper (MinerU-parsed Markdown) into an 11-section structured note, the single input contract consumed by all downstream batch analyses. It is an honestly labeled rebuild of the original private skill, not the original; load it directly when only single-paper notes are needed.

The skill carries no scripts; it drives external tools such as the `mineru` CLI.

### skincare-product-research

`skincare-product-research` is an evidence-oriented skincare product research expert. It evaluates a specific product or researches and compares products for a stated skin need by reasoning from the full formulation architecture, human clinical evidence, and the user's skin state and routine instead of marketing. It runs in two modes: Mode A evaluates a user-supplied product (identity resolution, functional architecture, marketing-claim audit, seven-dimension scoring, three-level price guidance) and Mode B converts a stated need into criteria and compares a broad candidate pool on decision-relevant tables.

Bundled resources:

- `references/evaluation-modes.md`: detailed Mode A (A1–A8) and Mode B (B1–B5) procedures.
- `references/research-rules.md`: source hierarchy, marketing contamination control, evidence language, and terminology rules.
- `references/category-heuristics.md`: formulation heuristics for cleansers, moisturizers, sunscreens, and retinoids/acids.
- `references/scoring-safety-output.md`: score interpretation, safety boundaries, response style, and output templates.

The skill carries no scripts; it relies on the agent's web research for formulations, evidence, and current pricing.

### zotero-better-notes-format

`zotero-better-notes-format` formats Markdown notes for Zotero Better Notes rich-text import while keeping Markdown as the editable source of truth. It preserves LaTeX formulas, normalizes heading hierarchy, and exports full-preview or fragment HTML via `scripts/md_to_zotero_html.py`. Use when Zotero-ready notes, Better Notes-compatible HTML, or math/table conversion for Zotero matters.

Bundled resources:

- `scripts/md_to_zotero_html.py`: Convert Markdown notes into Better Notes/Zotero-friendly HTML.
- `references/format-rules.md`: Math shapes, list spacing, paste guidance, and troubleshooting.

## Install In Codex

Codex discovers skills from the skills directory under `CODEX_HOME`. If `CODEX_HOME` is not set, the default location is usually `~/.codex/skills`.

### Option 1: Clone This Repository As Your Skills Directory

Use this when you want this repository to be the full skills workspace:

```bash
git clone git@github.com:ZB258/skills.git ~/.codex/skills
```

On Windows PowerShell:

```powershell
git clone git@github.com:ZB258/skills.git "$env:USERPROFILE\.codex\skills"
```

Restart Codex after cloning so the skill metadata is rediscovered.

### Option 2: Copy One Skill Into An Existing Skills Directory

Use this when you already have other local skills:

```bash
git clone git@github.com:ZB258/skills.git ~/src/codex-skills
cp -R ~/src/codex-skills/paper-reading-notes ~/.codex/skills/
```

On Windows PowerShell:

```powershell
git clone git@github.com:ZB258/skills.git "$env:USERPROFILE\src\codex-skills"
Copy-Item -Recurse "$env:USERPROFILE\src\codex-skills\paper-reading-notes" "$env:USERPROFILE\.codex\skills\"
```

Restart Codex after copying the skill.

## Use

Invoke the skill explicitly in Codex:

```text
Use $paper-reading-notes to read this paper into concise Markdown notes with formulas, figures, and critical analysis.
```

Codex may also invoke the skill automatically when a user asks for research-paper reading, method analysis, formula reconstruction, code or dataset availability, Zotero note-ready output, or a critical reading that goes beyond a plain summary.

## Maintain

- Keep each skill self-contained in its own top-level directory.
- Keep detailed reusable guidance in `references/` instead of bloating `SKILL.md`.
- Keep deterministic helpers in `scripts/` and test them when changed.
- Do not add README, changelog, or installation notes inside an individual skill unless that file is directly required for the skill to function.
- Update this root `README.md` whenever a skill is added, removed, renamed, or materially changed.

## Verify

Run the repository checks after modifying skills:

```bash
python -m ruff check .
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ./paper-reading-notes
```

Adjust the validator path if your Codex system skills are installed somewhere else.
