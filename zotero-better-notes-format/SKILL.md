---
name: zotero-better-notes-format
description: Format Markdown notes for Zotero Better Notes rich-text import, especially when preserving LaTeX formulas, headings, lists, tables, and readable note styling matters. Use when Codex is asked for Zotero-ready notes, Better Notes-compatible HTML, HTML fragments for pasting into Zotero, or troubleshooting Markdown/math conversion for Zotero notes.
---

# Zotero Better Notes Format

Format Markdown notes into Better Notes/Zotero-friendly HTML while keeping Markdown as the editable source of truth.

## Workflow

1. Keep Markdown as the master file.
   - Preserve formulas as `$...$` and `$$...$$` in Markdown.
   - Normalize heading hierarchy before export.
   - Prefer compact prose and clean lists; avoid decorative separators unless they carry structure.

2. Read `references/format-rules.md` when preparing or reviewing note content.
   - Use it for math shapes, list spacing, paste guidance, and troubleshooting.

3. Export HTML with `scripts/md_to_zotero_html.py`.
   - Full preview HTML:

```bash
python scripts/md_to_zotero_html.py input.md -o output.html
```

   - Full preview HTML plus body fragment:

```bash
python scripts/md_to_zotero_html.py input.md -o output.html --fragment output_fragment.html
```

4. Verify the exported HTML before delivery.
   - Check that display math appears as `<pre class="math">$$...$$</pre>`.
   - Check that inline math appears as `<span class="math">$...$</span>`.
   - Do not accept ordinary `<pre>` blocks for display formulas.

5. Tell the user which file to use.
   - For manual Better Notes paste, copy the rendered HTML page, not the HTML source.
   - If formulas fail after HTML paste, try direct Markdown paste with `$...$` and `$$...$$` preserved.

## Dependencies

The export script requires Python-Markdown:

```bash
python -m pip install markdown
```

Install it if missing, or report that HTML export cannot run in the current environment.

## Resources

- Format rules: `references/format-rules.md`
- Export script: `scripts/md_to_zotero_html.py`
