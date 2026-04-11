# Note Writing Rules

Use these rules when turning a paper into Markdown notes.

## Structure

- Follow the paper's logic only as far as it helps explanation.
- Group content by reader value: method, formulas, framework, evidence, critique.
- Integrate figures inside the section they support.
- Do not create a standalone figure gallery unless explicitly requested.

## Technical Fidelity

- Reuse original symbols and notation where possible.
- Separate the paper's definitions from your interpretation.
- Make clear whether a statement is from the paper, from supplementary material, or from your inference.
- When a file name or citation year conflicts with the actual online record, state the exact date briefly and move on.

## Figure Rules

- Prefer figures that carry structural information:
  - overall framework
  - dataset organization
  - global performance summary
- Skip decorative or repetitive visualizations unless the user asks for them.
- Use size by importance:
  - large: overall framework, architecture, pipeline
  - medium: benchmark overview or main comparison summary
  - small: dataset composition, taxonomies, crowded catalog figures
- Add a caption that says what the figure contributes to understanding, not just its title.

## Tone

- Keep code and release-status wording objective.
- Avoid first-person process notes inside the final Markdown.
- Avoid filler conclusions and generic future-work offers.
- Prefer compact prose over repeated bullet summaries.

## Better Notes/Zotero HTML Export

- Keep Markdown as the editable master file.
- Export HTML only as a delivery format for Better Notes or Zotero rich-text notes.
- Better Notes handles math best when formulas enter through its Markdown/math pipeline or through math-marked HTML.
- For exported HTML fragments, use these math shapes:
  - Inline math: `<span class="math">$...$</span>`
  - Display math: `<pre class="math">$$...$$</pre>`
- Do not emit display formulas as ordinary `<div><pre>...</pre></div>` blocks.
- When troubleshooting manual paste, distinguish copying rendered HTML from copying HTML source code.
- If formulas still fail after HTML paste, test direct Markdown paste with `$...$` and `$$...$$` preserved.
