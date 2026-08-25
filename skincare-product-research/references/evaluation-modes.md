# Evaluation Modes

Detailed procedures for the two operating modes of the `skincare-product-research` skill. Load this file when executing Mode A (evaluate a specific product) or Mode B (need-based product search).

---

## Mode A — Evaluate a product supplied by the user

### Step A1 — Resolve exact product identity

Confirm, by research when needed:

- brand;
- full product name;
- region / market;
- version or reformulation year if relevant;
- product type;
- current INCI ingredient list;
- pack size;
- current market price range.

If multiple formulations exist, explicitly state which formulation is being analyzed and avoid merging ingredient lists from different versions.

### Step A2 — Gather sources

Prefer:

- official brand ingredient list and directions;
- retailer or regulatory ingredient listings when useful;
- dermatology guidelines;
- PubMed-indexed research / systematic reviews;
- independent formulation references;
- current retail pricing from multiple sellers;
- independent user reports only for sensory properties, scent, pilling, finish, packaging failure, or other experiential traits.

Actively discount advertorials, affiliate pages, retailer copy, sponsored content, and SEO articles.

### Step A3 — Identify the functional architecture

For cleansers, identify:

- surfactant family/families;
- soap-based versus syndet system;
- fatty acid + alkali combinations that form soap in situ;
- likely cleansing strength;
- pH if verifiable;
- foaming system;
- humectants and after-feel modifiers;
- fragrance / essential oils;
- relevant irritation risks.

For moisturizers, identify:

- humectants;
- emollients;
- occlusives;
- barrier-relevant lipids;
- silicones;
- film formers;
- fragrance;
- texture and likely finish.

For sunscreens, identify:

- UV filters;
- UVA / UVB coverage;
- SPF / PA / UVA-PF when available;
- photostability;
- water resistance;
- film-forming system;
- alcohol level if relevant;
- cosmetic finish;
- eye-sting / pilling concerns from credible user reports.

For treatment-oriented products, identify:

- primary active ingredient(s);
- concentration;
- chemical form;
- biological mechanism;
- quality of human evidence;
- realistic time-to-effect;
- irritation / contraindication considerations;
- redundancy or conflict with current routine.

### Step A4 — Decode marketing claims

Create a mapping:

**marketing phrase -> actual ingredient / formulation feature -> plausible mechanism -> evidence strength -> practical significance**

Prioritize claims emphasized by the brand.

### Step A5 — Evaluate fit for this user

Use user-specific information whenever available:

- oiliness level;
- dryness / tightness after washing;
- sensitivity / redness;
- acne / comedones;
- post-inflammatory erythema or pigmentation;
- current actives;
- shaving;
- sunscreen / makeup;
- cleansing frequency;
- climate / season;
- budget and fragrance preferences.

Do not infer sensitive medical diagnoses. If a medical condition may be present, state the boundary and recommend appropriate clinical evaluation.

### Step A6 — Score the product

Use the following scores from 0–10. Scores are conditional on the user's situation, not universal.

- **Goal fit**: how well it serves the user's stated goal.
- **Formulation quality**: how coherent the formulation is for that goal.
- **Evidence quality**: quality of evidence supporting the meaningful claims.
- **Tolerance fit**: suitability for this user's skin and current routine.
- **Cosmetic elegance**: texture, finish, foaming, scent, packaging, usability.
- **Value for money**: performance relative to current market price.
- **Marketing honesty**: whether claims are proportionate to evidence.

Then provide an overall **Recommendation Index / 10**.

Do not calculate the overall score as a naive arithmetic average. Weight goal fit, formulation, evidence, and tolerance more heavily than scent, packaging, or brand prestige.

### Step A7 — Price guidance

Give three price levels where possible:

- **Good buy price**: strong value, worth buying if the user wants this product category.
- **Fair price**: acceptable if the user likes its sensory / brand advantages.
- **Overpriced above**: price at which alternatives become clearly more compelling.

Use current market data. Distinguish official list price from realistic street price.

### Step A8 — Final verdict format

Start with a concise conclusion, then explain.

Recommended structure:

**Verdict**

One paragraph summarizing what the product fundamentally is, whether the marketing is proportionate, and who should / should not buy it.

**How it works**

Explain the cleansing / moisturizing / sunscreen / treatment pathway in mechanistic terms.

**Key ingredients and formulation**

Use a compact table when useful:

| Component | Ingredient / system | Function | Importance | Evidence / caveat |
|---|---|---|---|---|

**Marketing audit**

Explain whether headline claims are supported, partially supported, misleadingly framed, or weak.

**Fit for this user**

Explicitly account for the user's skin state and existing routine.

**Scores and price**

| Dimension | Score / 10 | Reason |
|---|---:|---|

Then state:

- Recommendation Index;
- Good buy price;
- Fair price;
- Overpriced above;
- best alternatives if relevant.

**Other advantages**

Only after efficacy and value, discuss:

- brand positioning / prestige;
- fragrance;
- packaging;
- foam / texture;
- retail availability;
- travel convenience;
- aesthetic experience.

---

## Mode B — User gives a need; research and compare products

Trigger when the user asks for products for a goal, skin type, budget, region, routine, or preference.

Examples:

- "recommend a mild cleanser for combination-oily skin"
- "find me a retinol under $30"
- "compare sunscreens for oily acne-prone skin"

### Step B1 — Convert the request into explicit criteria

Extract or infer only what is safe and reasonable:

- goal;
- product category;
- skin characteristics;
- current routine / active ingredients;
- irritation tolerance;
- region / availability;
- budget;
- fragrance preference;
- texture / finish preference;
- medical / pregnancy constraints if explicitly provided by the user.

If a missing detail would materially change the shortlist, ask one focused question. Otherwise make a stated assumption and proceed.

### Step B2 — Build a broad candidate pool

Research multiple products before narrowing.

Avoid selecting only famous or premium brands. Include:

- mass-market;
- pharmacy / dermocosmetic;
- specialist skincare;
- premium products only when they offer a meaningful formulation or sensory advantage.

Do not allow affiliate rankings or social-media popularity to determine the shortlist.

### Step B3 — Filter by hard constraints

Examples:

- exclude strong soap-based cleansers for a user seeking very mild cleansing;
- exclude fragranced products if the user explicitly requests fragrance-free;
- avoid duplicate active ingredients when the current routine already contains them;
- exclude products above budget;
- exclude unavailable regional products unless importing is reasonable and requested.

### Step B4 — Compare on decision-relevant dimensions

Use a concise table rather than long product-by-product essays.

Default table:

| Product | Core system / actives | Strengths | Weaknesses | Best for | Marketing concern | Typical price | Good buy price | Recommendation |
|---|---|---|---|---|---|---:|---:|---:|

For cleansers, add "cleansing strength" and "surfactant system" when helpful.

For sunscreens, add protection, finish, water resistance, and eye-sting / pilling if evidence is available.

For treatment products, add active concentration, evidence level, and irritation risk.

In the "core system / actives" column, state the functional meaning of the system — what it does and how strongly — rather than only INCI names; expand surfactant or filter families on first use.

### Step B5 — Explain the mechanism

Before the ranking, explain how the product category achieves its function and why the shortlisted systems differ in effect, so a non-specialist user can reconstruct the reasoning:

- open with the shared mechanism of the category;
- derive the variables that actually change outcomes in this category, separating structural constraints from formulator choices;
- map each shortlisted product to its position on that mechanistic axis, in plain language, and connect the user's original complaint to the mechanism.

Follow the mechanism reasoning rules in [`../SKILL.md`](../SKILL.md) throughout — attribute every property to its correct system level, and check each assertion against fundamentals you are confident in. Do not let the comparison table substitute for this explanation. A user who cannot reconstruct why the top pick wins has not been served.

### Step B6 — Rank products by user fit, not generic prestige

Give a clear top recommendation and explain why it wins for this user.

When useful, also name:

- best value;
- gentlest option;
- strongest active option;
- best sensory / premium option.

Do not create categories merely to give every product an award.
