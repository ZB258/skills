# Review Lens

Use these prompts to avoid becoming trapped in the paper's own narrative.

## Method

- What is the real technical move?
- What part is genuinely new, and what part is recombination?
- Is the paper changing the objective, the data, the supervision source, or just the training scale?

## Contribution and Evaluation

- Does the claimed gain remain after controlling for more data, stronger labels, extra compute, better tuning, or implementation details?
- Is the core contribution separable from the surrounding evaluation harness, model head, prompt, retrieval system, simulator, or deployment stack?
- Does the method use supervision that is stronger than the paper's framing suggests?

## Domain-Specific Claims

- If the paper claims domain-informed modeling, does the implementation still match that claim after augmentations and engineering details are included?
- Does the training target or measurement target truly match the paper's interpretation?
- Does the loss optimize the interpretation the paper claims?

## External Guidance or Extra Signals

- Is the auxiliary target, teacher, retrieved context, annotation source, simulator, or extra modality meaningful at the claimed granularity?
- How sensitive is the method to alignment errors, timestamp mismatch, annotation noise, distribution shift, or source bias?
- Could the external signal inject a bias that suppresses task-relevant structure?

## Evidence

- Which ablations are decisive?
- Which missing ablations would most weaken the main claim?
- Are improvements broad across tasks, or concentrated on the tasks most favorable to the method?

## Reader Guidance

Always tell the reader:

- what to reuse
- what to distrust
- what to test before building on the paper
