---
name: figure-png-renderer
description: Render and iteratively select a high-resolution scientific-figure PNG from an approved figure specification and prompt. Use after prompt compilation and before PowerPoint reconstruction; do not redesign scientific meaning during rendering.
---

# Figure PNG Renderer

Read `01_prompt/figure_spec.yaml`, `structure_lock.yaml`, `structure_skeleton.png`, `prompt.md`, and `visible_text.txt`. Write under `02_render/`:

- `candidates/candidate-N.png`;
- `selected.png`;
- `render_manifest.json` with backend, prompt hash, dimensions, candidate scores, and selection rationale;
- `render_review.md` with observed defects and corrections.

Prefer a native 2K or 4K landscape render for dense framework figures. Keep the topology, visual anchor, region geometry, connector grammar, and density distribution defined by the structure lock. Treat the skeleton as a layout control image when the backend supports reference conditioning. Generate no factual data graphics absent from the source.

Use PaperBanana when configured for reference-driven, multi-round rendering. Otherwise use the runtime image-generation tool. The rendering backend may be proprietary even when orchestration code is open source; record it truthfully.

Reject candidates with missing regions, changed macro topology, displaced visual center, collapsed information density, wrong arrow direction, swapped color semantics, invented labels, malformed visible text, generic stock-photo appearance, or loss of requested simulator or scene texture. Select only after explicit visual review.
