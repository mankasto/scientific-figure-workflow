# Workflow prompt template

Use this template when a user wants the complete paper-to-PNG-to-editable-PPT workflow. Replace bracketed fields where information is available. Omit irrelevant fields; do not ask the user to complete placeholders that can be inferred safely from the source material.

```text
Use $figure-workflow to create a publication-ready scientific figure and run these stages:

1. $figure-prompt-compiler
2. $figure-png-renderer
3. $figure-ppt-reconstructor
4. $figure-qa-reviewer

Source material:
- Paper, method description, or research plan: [PATH OR TEXT]
- Reference figure(s): [PATHS, OPTIONAL]
- Caption or semantic brief: [TEXT, OPTIONAL]
- Target venue or visual community: [VENUE, OPTIONAL]

Structure lock (complete before rendering):
- Reference-structure mode: [preserve-reference / adapt-reference / new-structure]
- Visual center and macro topology: [DESCRIPTION]
- Relative region positions and area ratios: [DESCRIPTION]
- Connector grammar and reading order: [DESCRIPTION]
- Information-density target by region: [DESCRIPTION]
- Per-region content budget: [ENTITIES + INTERNAL RELATION + EVIDENCE + METRIC/OUTPUT]
- Allowed structural changes: [LIST]
- Forbidden structural changes: [LIST]
- Render and approve a grayscale structure_skeleton.png before generating candidates

Figure goal:
- Figure type: [architecture / concept / mechanism / workflow / graphical abstract / evaluation]
- Intended use: [paper / proposal / presentation]
- Audience: [AUDIENCE]
- Aspect ratio or publication size: [16:9 / single column / double column / OTHER]
- Figure-level title: omit for manuscript figures unless standalone use or the user explicitly requires one

Required semantics:
- [MODULE, STAGE, OR CLAIM 1]
- [MODULE, STAGE, OR CLAIM 2]
- [MODULE, STAGE, OR CLAIM 3]
- Reading order or causal direction: [DIRECTION]
- Required feedback, hierarchy, or grouping: [RELATIONSHIPS]
- Required metrics, formulas, or terminology: [ITEMS]

Visual direction:
- Main visual anchor: [SUBJECT OR SCENE]
- Raster-preferred regions: [PHOTOREALISTIC OR SIMULATOR SCENES, DENSE TEXTURES]
- Vector-preferred regions: [PANELS, LABELS, ARROWS, ICONS, METRICS]
- Palette or semantic colors: [COLORS, OPTIONAL]
- Saturation: restrained; mute repeated accents and generated assets when they compete with structure
- Style: restrained, publication-ready, consistent with the target research community
- Improve hierarchy, spacing, grouping, and image quality without changing source meaning
- Numbering style: restrained text numbering or a small eyebrow label; avoid colored numbered circles unless explicitly justified
- Connector style: simple, directional, routed behind content, with explicit attachment sides and no text crossings
- Typography: natural phrase wrapping, consistent type scale and margins, no mid-word breaks or emergency shrink-to-fit
- Do not add a figure-level title or subtitle to a manuscript figure; rely on its caption for context
- Avoid badge-heavy headings, excessive rounded cards, floating bubbles, generic icon repetition, and ornamental gradients

Approved visible text:
- [EXACT STRING 1]
- [EXACT STRING 2]
- [EXACT STRING 3]

Content constraints:
- Do not invent modules, causal relations, results, numeric values, benchmark status, or certification claims.
- Do not add logos, watermarks, decorative slogans, or unsupported annotations.
- The image model may render only the approved visible text.
- Treat generated text as provisional. Rebuild all final labels as native PowerPoint text and remove image-model text artifacts from raster crops.

PNG stage:
- Write 01_prompt/figure_spec.yaml, structure_lock.yaml, structure_skeleton.png, prompt.md, visible_text.txt, and review.md.
- Generate [NUMBER] high-resolution candidates and select the strongest one.
- Record the backend, prompt hash, dimensions, selected candidate, and selection rationale.
- Favor visual quality and scene fidelity while preserving the semantic contract.

PowerPoint reconstruction:
- Produce one editable slide unless the source explicitly requires more.
- Do not use a whole-slide screenshot or a flattened full-slide background.
- Rebuild titles, body text, panels, borders, arrows, connectors, metric bars, and simple icons as native objects.
- Use raster images only for inherently image-like or impractically complex regions.
- Insert each raster region as an independently selectable and replaceable asset.
- Plan connector routes before authoring; reject reversed, tangled, detached, duplicated, or text-crossing arrows.
- Resize or rewrite text boxes when copy does not fit; do not accept mid-word wrapping, clipping, or unreadably small text.
- Use typographic numbers by default instead of circular number badges.
- Write component_manifest.json and render a PPT preview.

QA and delivery:
- Verify semantic invariants, reading order, text associations, palette meanings, and forbidden additions.
- Verify visual hierarchy, typography, alignment, clipping, image quality, slide count, and package integrity.
- Fail visual QA for connector-routing errors, broken word wrapping, inconsistent text hierarchy, or gratuitous numbered circles.
- Inspect the presentation object model; do not infer editability from the .pptx extension.
- Fail QA if whole_slide_raster_count is greater than 0 or if native shapes/text are absent.
- Deliver the specification, prompt, selected PNG, editable PPTX, preview, component manifest, QA report, and status.json.
- Mark the job complete only after every hard gate passes.
```

## Short reference-figure version

Use this form when the user already has a reference image and source document:

```text
Use $figure-workflow to redesign [REFERENCE_IMAGE] using the evidence in [SOURCE_DOCUMENT].

Before rendering, use $figure-prompt-compiler to extract and lock the reference's macro topology, visual center, relative region geometry, connector grammar, reading order, and information-density pattern in structure_lock.yaml, and render structure_skeleton.png for review. Preserve that approved structure while improving hierarchy, spacing, palette, element grouping, and scene quality. Then use $figure-png-renderer to produce and select a high-resolution PNG, $figure-ppt-reconstructor to rebuild it as an object-level editable PowerPoint, and $figure-qa-reviewer to validate the result.

Complex scenes may remain independent high-resolution raster assets. Titles, labels, panels, arrows, connectors, metrics, and simple icons must be native editable PowerPoint objects. A whole-slide raster is forbidden. Do not invent information absent from the source. Deliver the PNG, PPTX, preview, manifests, QA report, and completed status.json.
```
