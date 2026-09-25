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

The manifest must report native shapes, editable text objects, connectors, raster assets, and any remaining whole-slide image. A whole-slide image count above zero is a hard failure unless the user explicitly requested a non-editable slide.

See [references/editability-contract.md](references/editability-contract.md).
