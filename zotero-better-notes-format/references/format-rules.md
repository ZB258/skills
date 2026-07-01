# Better Notes/Zotero Format Rules

## Source Markdown

- Keep Markdown as the editable master file.
- Preserve inline formulas as `$...$`.
- Preserve display formulas as `$$...$$` on their own lines.
- Normalize list spacing so Markdown parsers do not merge surrounding paragraphs into list items.
- Use semantic headings instead of visual dividers when possible.
- Avoid first-person process notes inside the final note.

## HTML Math Shapes

Better Notes handles math best when formulas enter through its Markdown/math pipeline or through math-marked HTML.

Use these HTML shapes for exported fragments:

- Inline math: `<span class="math">$...$</span>`
- Display math: `<pre class="math">$$...$$</pre>`

Do not emit display formulas as ordinary `<div><pre>...</pre></div>` blocks, because Better Notes may not render those as math.

## Export Expectations

- The full HTML file is for browser preview and manual copying from the rendered page.
- The fragment file is for workflows that need only body HTML.
- Tables, blockquotes, headings, and lists should be valid HTML produced from Markdown rather than hand-built where possible.

## Paste Guidance

- For manual paste into Better Notes, open the exported HTML in a browser and copy the rendered page content.
- Do not copy the HTML source code unless the receiving workflow explicitly accepts raw HTML.
- If formulas fail after HTML paste, test direct Markdown paste with `$...$` and `$$...$$` preserved.
