# Scoring, Safety, and Output

Score interpretation, safety boundaries, response style, and compact output templates for the `skincare-product-research` skill.

## Scoring guidance

Scores are recommendations, not measurements.

Suggested interpretation:

- **9–10**: unusually strong fit; little reason to prefer alternatives at the same price.
- **8–8.9**: strong recommendation.
- **7–7.9**: good product with meaningful caveats or price competition.
- **6–6.9**: acceptable but not compelling.
- **5–5.9**: average / replaceable.
- **3–4.9**: poor fit or weak value.
- **0–2.9**: generally avoid for this user or purpose.

Price can materially lower value-for-money but should not retroactively make an effective formulation ineffective.

## Safety boundaries

Do not diagnose a medical condition from product-selection context.

Flag medical evaluation when relevant, especially for:

- nodulocystic or scarring acne;
- persistent severe erythema or burning;
- eczema-like recurrent dermatitis;
- suspected rosacea;
- infection;
- rapidly changing lesions;
- severe allergic reactions;
- persistent symptoms despite appropriate basic care.

Do not frame prescription medication as an ordinary cosmetic upgrade.

When discussing pregnancy, prescription retinoids, systemic acne therapy, or other medically significant issues, use authoritative medical guidance and clearly state the clinical boundary.

## Response style

Use concise, analytical Chinese by default when the user writes in Chinese.

Lead with the conclusion.

Explain mechanisms in enough depth that the user learns how to evaluate future products independently.

Do not repeat marketing copy unless directly analyzing it.

Avoid vague praise such as "ingredients are luxurious" or "formula is clean".

Prefer statements such as:

- "the cleansing architecture is a fatty-acid soap system";
- "the humectants improve after-feel but do not negate the stronger degreasing system";
- "the headline ingredient is present in a rinse-off product, so practical exposure is limited";
- "the formula is effective, but its premium price mainly buys sensory elegance rather than stronger clinical efficacy".

When comparing products, keep the table concise and put detailed reasoning beneath only for the finalists.

## Compact templates

### Template A — Specific product

#### Verdict

[One-paragraph conclusion]

#### What the formula is actually doing

[Mechanism and formulation architecture]

#### Key ingredients

| Component | Ingredient / system | Real role | Importance |
|---|---|---|---|

#### Marketing audit

| Claim | What it actually means | Evidence | Assessment |
|---|---|---|---|

#### Fit for the user

[Skin state + current routine + risks + redundancy]

#### Score

| Dimension | Score / 10 | Reason |
|---|---:|---|

**Recommendation Index:** X/10  
**Good buy price:** X  
**Fair price:** X  
**Overpriced above:** X

#### Other merits

[Brand, scent, packaging, texture, foam, prestige, convenience]

#### Better alternatives

[Only if materially better options exist]

### Template B — Need-based product search

#### Recommendation

[One paragraph: what type of formula should be prioritized and top pick]

#### How they work

[Mechanism explanation derived at runtime from first principles: how this product class does its job, what actually separates the shortlisted systems, and where each product sits — with every property attributed to its correct system level and each assertion checked against fundamentals. Written for a non-specialist; expand every term on first use; connect the user's stated complaint to the mechanism]

| Product | Core system / actives | Strengths | Weaknesses | Best for | Typical price | Good buy price | Recommendation |
|---|---|---|---|---|---:|---:|---:|

Then briefly explain the top 2–3 finalists and the main tradeoffs, in mechanistic terms where the ranking depends on them.
