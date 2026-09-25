---
name: figure-prompt-compiler
description: Convert papers, methods, captions, research plans, and reference figures into an auditable scientific-figure specification and an image-model prompt. Use for the prompt stage of a collaborative figure workflow; do not generate the final image or PPTX.
---

# Figure Prompt Compiler

Read the source material and reference images. Write under `01_prompt/`:

- `figure_spec.yaml`: purpose, audience, figure type, aspect ratio, layout regions, reading order, visual anchor, palette roles, image preferences, text policy, semantic invariants, negative constraints, and evidence sources;
- `prompt.md`: the complete image-generation prompt;
- `visible_text.txt`: the only text permitted in the generated figure;
- `review.md`: ambiguities, assumptions, and items requiring later verification.

Use [references/figure-spec-schema.md](references/figure-spec-schema.md). Preserve observed facts separately from inferred design choices. Do not invent model modules, data, metrics, causal relations, or experimental results.

For image-rich architecture or conceptual figures, explicitly describe which regions should look photographic, simulated, rendered, diagrammatic, or vector-like. Record color meanings and element partitioning. Avoid vague instructions such as “make it professional.”

Specify connector direction and attachment intent, a realistic typography hierarchy, the figure-title policy, and the numbering treatment. For manuscript figures, default to no figure-level title or subtitle because the caption supplies context. Default to restrained text numbering rather than colored circles or badges. Add negative constraints against tangled arrows, text-crossing connectors, mid-word wrapping, excessive rounded cards, floating bubbles, ornamental gradients, and repetitive generic icons unless the reference or subject explicitly requires them. Apply the shared [publication design standard](../figure-workflow/references/publication-design-standard.md), including the source topology, information-budget, and grayscale-skeleton requirements.

If Happy Figure Skill or CCF-Figure is installed, it may draft the prompt, but normalize the result into this plugin's schema before handoff.
