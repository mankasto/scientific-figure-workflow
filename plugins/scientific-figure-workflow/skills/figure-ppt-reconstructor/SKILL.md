---
name: figure-ppt-reconstructor
description: Reconstruct an approved scientific-figure PNG as a hybrid editable one-slide PowerPoint with native text, shapes, connectors, and separately replaceable raster assets. Use after PNG selection; never satisfy the request by placing the whole PNG on one slide.
---

# Figure PPT Reconstructor

Read the approved PNG and semantic contract. Write under `03_reconstruct/`:

- `final.pptx` and `preview.png`;
- `component_manifest.json`;
- `assets/` containing only justified raster regions;
- `build/` containing the reproducible authoring script and validation receipts.

Use the installed img2pptx backend when available. Rebuild these as native PowerPoint objects wherever practical:

- titles, labels, metrics, legends, and short annotations;
- panel fills, borders, cards, badges, bars, nodes, arrows, and connectors;
- simple icons and charts whose semantics depend on color, direction, order, or geometry.

Keep photorealistic simulator scenes, microscopy, screenshots, dense plots, and highly detailed illustrations as tightly cropped independent raster assets. Never keep editable text, panel borders, or arrows baked into a large raster crop merely to save effort.

Editability must not lower the visual evidence to placeholder quality. If the approved master uses a technically rich scene, trajectory, propagation map, distribution, cutaway, or comparison thumbnail, preserve that richness with a separate text-free raster or polished modular vector asset. Use native primitives for structure and genuinely simple graphics; do not substitute generic circles, squares, or line sketches for evidence that carries recognizable detail.

Plan typography and connector routing before authoring. Follow [references/layout-quality-contract.md](references/layout-quality-contract.md) and the shared [publication design standard](../figure-workflow/references/publication-design-standard.md). In particular:

- route connectors behind nodes and text, with explicit attachment sides and waypoints where needed;
- reject crossings through labels, unrelated objects, or panel interiors;
- size text boxes from the rendered font metrics and rewrite or resize the layout rather than relying on aggressive shrink-to-fit;
- prevent mid-word wrapping, orphaned one-word lines, clipped text, and inconsistent internal margins;
- use plain typographic stage numbers by default. Do not place every number in a colored circle or badge unless the source design or meaning calls for it.
- keep semantic accents muted enough that color remains subordinate to topology and evidence; correct high-saturation raster assets before assembly.

Render and inspect the slide after authoring. Package validation cannot detect whether an arrow communicates the wrong path or whether a layout looks mechanically generated.

The manifest must report native shapes, editable text objects, connectors, raster assets, and any remaining whole-slide image. A whole-slide image count above zero is a hard failure unless the user explicitly requested a non-editable slide.

See [references/editability-contract.md](references/editability-contract.md) and [references/layout-quality-contract.md](references/layout-quality-contract.md).
