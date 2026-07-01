---
name: paper-reading-notes
description: Read research papers from PDF into polished Markdown notes with formulas, integrated figures, reviewer-style analysis, and optional Zotero/Better Notes export via the zotero-better-notes-format skill. Use when the user asks for a paper's method, innovations, technical structure, formulas, evaluation or application framework, code or dataset availability, Zotero note-ready output, or a critical reading that goes beyond a plain summary.
---

# Paper Reading Notes

Produce concise but rigorous paper notes. Do not just restate the paper. Reconstruct the method faithfully, then evaluate it with a general reviewer lens appropriate to the paper's domain.

## Workflow

1. Read the PDF structurally.
   - Extract text for search and quick checks.
   - Inspect rendered pages when layout matters.
   - Note exact dates if filename, PDF metadata, or online record disagree.

2. Reconstruct the paper's technical core.
   - Identify the problem setting, method name, training setup, and claimed innovations.
   - Reuse the paper's original symbols and variable names where possible.
   - Write formulas with the paper's notation instead of replacing them with your own notation unless the paper is unclear.

3. Separate the core method from the evaluation or application stack.
   - Identify what belongs to the paper's main contribution versus what belongs to training setup, evaluation framework, downstream heads, prompting, retrieval, or deployment scaffolding.
   - For papers about reusable models, identify how the core model is adapted or evaluated beyond its original training setup.
   - For systems, algorithms, datasets, or empirical studies, identify the benchmark, inference, deployment, or analysis context that wraps the core idea.
   - Call out when the evaluation or application framework is standard and the main contribution lies elsewhere.

4. Verify unstable external facts.
   - Check repositories, weights, datasets, or project pages on the web when the user asks about code availability or current release state.
   - State the checked date explicitly when the online state matters.
   - Keep this section objective and brief.

5. Handle figures deliberately.
   - Prefer direct extraction of embedded PDF image objects via `scripts/extract_pdf_images.py`.
   - Review `manifest.json` after extraction and match candidates to the paper's figure number, caption, page, dimensions, and surrounding text before inserting them.
   - Filter out logos, masks, icons, repeated fragments, and decorative images unless the user explicitly asks for exhaustive extraction.
   - Fall back to page rendering and region extraction only when the figure is not stored as a complete embedded image or the embedded objects are fragmented.
   - Insert each figure in the section where it is discussed. Do not create a separate "key figures" section unless the user explicitly asks for one.
   - Add a short caption for each inserted figure.
   - Size figures by importance and density:
     - Overall method or architecture figure: large.
     - Core result overview figure: medium.
     - Dataset composition, taxonomy, or busy summary figure: smaller.

6. Write the notes in Markdown.
   - Keep the tone objective.
   - Avoid meta commentary about how the notes were produced.
   - Avoid verbose closure text or generic offers of future help unless the user asks.
   - Keep code availability wording factual rather than personal.

7. Export to Better Notes/Zotero HTML when requested.
   - Read and use the `zotero-better-notes-format` skill.
   - If skills are available as folders in the same repository, read `../zotero-better-notes-format/SKILL.md` and its referenced format rules.
   - Keep this skill focused on paper understanding; do not duplicate Zotero/Better Notes format details here.

8. Add reviewer-style judgment.
   - Include what is worth learning from the paper.
   - Include what is fragile, overstated, underspecified, or likely dataset-dependent.
   - Distinguish between the paper's narrative and your own assessment.
   - Tell the reader what to absorb and what to be cautious about.

## Critical Reading Lens

Apply this lens after reconstructing the method:

- Ask whether the claimed gain comes from the proposed idea itself, more data, stronger supervision, better tuning, implementation details, or evaluation setup.
- When the paper makes domain-informed claims, ask whether the implementation actually supports the domain interpretation or only uses domain language around a conventional method.
- When the paper uses external guidance, auxiliary targets, retrieved context, simulators, teachers, or extra modalities, ask whether these signals introduce bias, leakage, stronger supervision than advertised, or dependence on alignment quality.
- Ask whether the training target truly matches the claimed interpretation.
- Ask what ablations are still missing to validate the paper's strongest claim.

## Output Expectations

Default output should include:

- Method summary
- Claimed innovations
- Technical structure or system architecture when relevant
- Module formulas or formal definitions when relevant
- Evaluation or application framework when relevant
- Code, weights, and dataset status when relevant
- Critical assessment

If the user asks for a written artifact, save it as Markdown in the requested location. If they ask for Zotero or Better Notes compatibility, also export HTML.

## Resources

- Figure extraction script: `scripts/extract_pdf_images.py`
- Zotero/Better Notes export skill: `../zotero-better-notes-format`
- Detailed note-writing rules: `references/note-writing-rules.md`
- Detailed critical review prompts: `references/review-lens.md`

Script dependencies:

- `scripts/extract_pdf_images.py` requires PyMuPDF, imported as `fitz`.
- Zotero/Better Notes HTML export dependencies are owned by `zotero-better-notes-format`.
- If a dependency is missing, install only the package needed for the current operation or report that the script could not be run in the current environment.
