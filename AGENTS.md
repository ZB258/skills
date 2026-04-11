# Repository Guidelines

This repository is a workspace for maintaining multiple Codex skills. Keep guidance generic enough to apply across all skill folders, not only the currently active skill.

## Scope

- Treat each top-level skill directory as an independent skill package.
- Keep shared repository rules in this file.
- Keep skill-specific workflows inside that skill's `SKILL.md` or its `references/` files.

## Editing Rules

- Use LF line endings for all files.
- Prefer ASCII unless a file already uses non-ASCII or the content requires it.
- Fix obvious spelling mistakes in code, user prompts, documentation, and skill text when encountered, and mention the correction in the final response.
- Do not add auxiliary files such as README, changelog, or installation notes inside a skill unless they are directly required for the skill to function.
- Update the repository root `README.md` in the same change whenever a skill is added, removed, renamed, or materially changed.

## Skill Structure

- Each skill folder must include `SKILL.md`.
- Optional resources should be organized under `scripts/`, `references/`, `assets/`, and `agents/` as appropriate.
- Keep `SKILL.md` concise and move longer reusable guidance into `references/`.
- Scripts included in skills should be deterministic, reusable, and tested when changed.

## Verification

- Run `ruff check .` after every code modification.
- If the `ruff` executable is not on PATH, run the equivalent `python -m ruff check .`.
- If Ruff is unavailable, install it or report that verification could not be run.
- Validate changed skills with the skill validator when `SKILL.md`, `agents/openai.yaml`, or resource layout changes.

## Git

- Use conventional commit messages, for example `feat: add paper reading skill` or `docs: add repository agent guidelines`.
- Commit related changes together after verification passes.
- Do not amend or rewrite commits unless explicitly requested.
