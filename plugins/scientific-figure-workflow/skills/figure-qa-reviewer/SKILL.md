---
name: figure-qa-reviewer
description: Independently review a scientific PNG and reconstructed PPTX for semantic correctness, visual fidelity, package integrity, and real object-level editability. Use as the final gate or when a figure is claimed to be editable.
---

# Figure QA Reviewer

Review upstream artifacts without relying on producer claims. Write under `04_qa/`:

- `qa_report.json` and `qa_report.md`;
- `pptx_preview.png`;
- `overlay.png` and localized comparisons where useful.

Verify:

1. Semantic invariants: region count, order, connections, direction, color meanings, text associations, and forbidden additions.
2. Visual quality: hierarchy, density, alignment, typography, connector routing, numbering treatment, image quality, and consistency with the approved PNG.
3. PPTX integrity: intended slide count, valid package, expected dimensions, no clipping or unreadable text.
4. Editability: native shapes, native text objects, connectors, raster images, and any whole-slide raster.

Fail the editability gate when the slide is effectively one screenshot, even if it renders perfectly. Accept raster assets only for inherently raster or impractically complex visual regions that remain independently replaceable.

Apply the reconstructor's [layout quality contract](../figure-ppt-reconstructor/references/layout-quality-contract.md) and the shared [publication design standard](../figure-workflow/references/publication-design-standard.md) independently. Fail visual QA for arrows that cross text, enter the wrong target, reverse direction, detach from endpoints, or form unexplained tangles. Also fail for mid-word wrapping, clipped or emergency-small text, inconsistent typography, or gratuitous numbered circles and badge-heavy headings. Review at the intended publication size. Automated geometry warnings are evidence to inspect, not findings to dismiss without a rendered visual check.

Fail asset fidelity when evidence-rich source regions have been replaced by low-fidelity primitive placeholders merely to increase editability. Fail palette restraint when repeated high-saturation colors dominate the page without carrying proportionate semantic importance.

Use [references/qa-schema.md](references/qa-schema.md). Update `status.json` to `complete` only when every hard gate passes.
