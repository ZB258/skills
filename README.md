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
