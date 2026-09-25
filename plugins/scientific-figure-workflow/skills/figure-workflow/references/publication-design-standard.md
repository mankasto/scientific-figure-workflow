# Publication figure design standard

Use this standard across prompt compilation, raster generation, PowerPoint reconstruction, and QA. It defines transferable publication-quality criteria rather than a fixed visual template.

## 1. Freeze meaning before styling

- Classify the source and the target figure separately. A method, benchmark, survey, mechanism analysis, and embodied-agent loop do not share one default layout.
- Create a node-and-relation inventory before drawing. Record sequence, influence, conditioning, comparison, concurrency, revision, feedback, and bidirectionality explicitly.
- Preserve role ownership: actor, action, affected entity, response, consequence, and update target must not drift during styling.
- Trace every scientific module, arrow, metric, example, and visual encoding to the source or mark it as non-semantic illustration.
- Do not force a left-to-right pipeline, closed loop, radial diagram, or multi-panel grid onto content that does not have that topology.

## 2. Budget information by argumentative importance

- Identify one primary visual anchor and one main claim.
- Mark each mechanism as `expanded`, `summarized`, or `referenced`.
- Expand the mechanism carrying the contribution; summarize supporting mechanisms with one necessary internal relation; reference background mechanisms with a short label, compact symbol, or connector annotation.
- Give each region one communicative job. Split the figure or demote detail when one region tries to explain several unrelated mechanisms.
- Use evidence-bearing visuals such as trajectories, masks, plots, maps, tokens, simulator frames, or source-derived crops only when they communicate a scientific fact faster than prose.
- Remove decoration and repeated context that has no scientific or navigational role.

## 3. Approve a grayscale skeleton

- Establish the exact canvas, title anchors, panel bounds, module footprints, evidence slots, connector corridors, and major whitespace before detailed drawing.
- The main organization must be understandable from geometry alone, without color, icons, or reading every label.
- Preserve clean whitespace corridors between locally dense regions so connectors and the reader's eye have stable routes.
- Size regions to their actual content. Reject oversized empty panels, cramped evidence slots, and mechanically equal boxes when the content is unequal.
- For complex or structurally new figures, do not proceed until a rendered grayscale skeleton passes semantic and layout review.

## 4. Use a restrained visual system

- Start from a white or near-white canvas, neutral text and borders, and two semantic accent colors. Add a small auxiliary color only for a real additional role.
- Encode one role consistently across color, stroke, shape, and label treatment. Do not assign a new color to every module or rely on color alone.
- Prefer alignment and whitespace for grouping. Use pale regions or boundaries only when they encode a real scope, phase, domain, or responsibility.
- Prefer rectangles, micro-rounded rectangles, straight or elbow connectors, and modest line weights. Use circles, curves, diamonds, pills, or large rounding only when the geometry itself carries meaning.
- Avoid card walls, dashboard controls, poster banners, floating bubbles, decorative sidebars, generic icon repetition, gradients, glow, neon, and shadows on structural modules.
- Keep one figure family across a paper: semantic color roles, font family, type hierarchy, strokes, arrowheads, corner treatment, panel markers, notation, icon family, and scene-rendering style remain consistent.

## 5. Treat typography as geometry

- Define title, module-title, body, and annotation tiers before detailed authoring. Prefer two main sizes plus one annotation size.
- Keep the largest and smallest normal tiers within roughly a 2.5:1 ratio unless the source clearly requires otherwise.
- Shorten copy or revise layout before shrinking essential text.
- Preserve intended phrases and line breaks. Reject mid-word wrapping, orphaned fragments, accidental extra lines, clipped glyphs, inconsistent capitalization, and misaligned baselines.
- Avoid long text inside circles, ellipses, icons, or narrow pills.
- Inspect at final insertion size. As a practical floor, critical labels should remain effectively about 8 pt or larger and supporting labels about 7 pt or larger after scaling.

## 6. Design connectors as semantic components

- Give each connector a source, target, direction, relation type, attachment side, path type, line style, and arrowhead endpoint.
- Use consistent ports for peer modules. Route fan-out through a short bus or junction rather than several crossing diagonals.
- Use the shortest unambiguous feedback path to the state it updates; avoid a full-canvas perimeter loop when a local return path is clearer.
- Prefer orthogonal paths in dense architectures. Use curves for genuine cycles, continuous change, spatial motion, or a deliberate reference-grounded grammar.
- Build connector routes before foreground nodes, then keep connectors behind text, nodes, and evidence.
- Reject reversed, duplicated, detached, unexplained-crossing, text-crossing, or double-arrowhead paths.

## 7. Use images and icons as evidence

- Keep photographs, simulator scenes, microscopy, and dense technical imagery only where they provide unique evidence or context.
- Repeated scenes must differ for a scientific reason such as time, action, viewpoint, modality, or outcome; otherwise reuse one context and express variation abstractly.
- Keep repeated evidence consistent in crop, scale, camera, lighting, annotation, and border treatment.
- Do not replace recognizable technical symbols with emoji, arbitrary Unicode glyphs, or generic placeholders.
- Raster exceptions must be tightly cropped, independently replaceable, free of baked editable text, and recorded with provenance and rationale.

## 8. Preserve useful PowerPoint editability

- Use native text, preset shapes, connectors, tables, and charts first; grouped native primitives second; modular vector assets third; atomic raster assets last.
- Decompose by semantic editing value rather than into meaningless geometric fragments.
- Create a component manifest and geometry ledger before detailed authoring for faithful reconstruction tasks.
- Reuse a canonical component for repeated modules instead of redrawing copies independently.
- Do not use a whole-slide image, a near-full-slide image, hidden reference bitmap, or invisible objects added to inflate object counts.
- Do not claim that an embedded SVG is natively editable in PowerPoint or WPS unless conversion and ungrouping were actually tested.

## 9. Validate the rendered artifact

Review the actual PNG and PPTX render, not only source code or object bounds. Run independent gates for:

1. source faithfulness and semantic topology;
2. conciseness and information budgeting;
3. grayscale macro organization;
4. typography and publication-size readability;
5. connector topology and routing;
6. visual-system and figure-family consistency;
7. package integrity and object-level editability.

A failure in one gate cannot be averaged away by strengths in another. Pixel similarity or package validity cannot override a wrong arrow, broken label, unsupported claim, or flattened slide.

## 10. Correct in dependency order

When a review fails, correct in this order:

1. canvas, major regions, and module geometry;
2. spacing, containment, alignment, and whitespace corridors;
3. typography, text bounds, line breaks, and hierarchy;
4. connector topology, direction, routing, strokes, and arrowheads;
5. repeated components and simple semantic shapes;
6. palette and line-style consistency;
7. detailed icons, textures, and other cosmetic refinements.

Do not polish complex imagery while an earlier structural layer still fails.
