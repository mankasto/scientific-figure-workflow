---
name: figure-workflow
description: Orchestrate a collaborative research-figure workflow from paper content or a reference figure through structured prompt, high-resolution PNG, hybrid editable PowerPoint reconstruction, and independent QA. Use when several people, agents, or skills need to hand off one scientific figure reproducibly.
---

# Figure Workflow

Coordinate four specialist skills through files, not conversational memory:

1. `$figure-prompt-compiler` writes the semantic contract and render prompt.
2. `$figure-png-renderer` generates and selects the high-resolution PNG master.
3. `$figure-ppt-reconstructor` rebuilds the master as a hybrid editable PPTX.
4. `$figure-qa-reviewer` independently checks semantics, appearance, package structure, and editability.

Create a job with `scripts/init_figure_job.py JOB_DIR`. Follow the folder and status contract in [references/handoff-contract.md](references/handoff-contract.md). Each specialist must read existing upstream manifests, write its own outputs, update `status.json`, and preserve rejected candidates for review.

When starting from a natural-language request, use [references/prompt-template.md](references/prompt-template.md) as the intake contract. Fill it from the user's materials and stated preferences; infer ordinary defaults instead of forcing the user to complete every placeholder. Preserve explicit constraints verbatim, especially approved visible text, semantic invariants, and editability requirements.

Apply [references/publication-design-standard.md](references/publication-design-standard.md) across all stages. It governs semantic topology, information density, skeleton approval, typography, connector design, visual restraint, editability, and rendered QA; it is a quality contract rather than a mandatory visual template.

## Completion rule

The workflow is complete only when:

- the approved prompt and visible-text list exist;
- a selected PNG master and render manifest exist;
- the PPTX contains independently editable text and shapes plus separately replaceable raster assets where justified;
- QA records semantic, visual, and editability results;
- `status.json` reports `complete` and no hard gate remains unresolved.

Never describe a one-piece image placed on a slide as an editable reconstruction. Report native-object and raster-object counts separately.

## External adapters

Use installed adapters when available:

- prompt: Happy Figure Skill or CCF-Figure;
- PNG: PaperBanana or the runtime image-generation tool;
- PPT: img2pptx or another object-level reconstruction backend.

The adapters are independent projects and are not redistributed by this plugin. Read [references/adapters.md](references/adapters.md) before choosing one.
