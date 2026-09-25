# Layout quality contract

Apply this contract to publication-facing scientific figures. Fidelity to an approved reference may override a default only when the reference clearly uses a different convention intentionally.

## Connectors and arrows

- Establish the graph and reading direction before placing shapes. Give every edge a named source, target, direction, and semantic role.
- Prefer the simplest route that communicates the relation: straight for aligned neighbors, orthogonal for structured pipelines, and a controlled curve for feedback loops.
- Set explicit attachment sides. Do not rely on automatic routing when it creates loops, reversals, diagonal detours, or unstable paths.
- Keep connectors behind nodes, labels, and foreground images. Arrowheads terminate at the target boundary rather than inside the target.
- Maintain visible clearance from text and unrelated objects. Do not cross labels, icons, panels, or another connector unless the crossing is unavoidable and visually disambiguated.
- Use one arrowhead at the destination. Use two only for a genuinely bidirectional relationship. Avoid decorative arrowheads on association lines.
- Keep line weight, arrowhead size, dash pattern, and color consistent by semantic role.
- Render the slide and inspect the actual path. Treat connector-over-text, wrong-direction, detached-endpoint, and unexplained-crossing findings as failures.

## Typography

- Define a small type scale before layout: title, section heading, label, annotation, and caption. Use weight and spacing before adding more colors or containers.
- Give text enough width for natural phrase boundaries. Never split a word across lines or leave a single short word on an orphaned line.
- Avoid shrink-to-fit as a layout strategy. If text does not fit at the minimum readable size, shorten the copy, widen the box, or revise the composition.
- Keep body text left-aligned unless a short label is intentionally centered. Use consistent line spacing, paragraph spacing, and internal margins.
- Keep labels out of arrows and connector paths. Do not place long phrases inside small circles, ellipses, or icons.
- Render at final slide size and inspect clipping, wrapping, baseline alignment, and density. Source-code bounds alone are insufficient.

## Numbering and containers

- Default to restrained typographic numbering such as `1  Scene Modeling`, `01 Scene Modeling`, or a small eyebrow label above the heading.
- Use a numbered circle, pill, or badge only when it conveys a meaningful state, matches an established visual system, or is explicitly present in the approved reference.
- Preserve unnumbered semantic circles when they represent states, agents, loop anchors, or other topology-bearing nodes. Do not confuse them with decorative numbered badges during simplification.
- Do not repeat the same decorative container around every label. Avoid excessive rounded cards, floating bubbles, gradients, shadows, and saturated accent colors.
- Let alignment, whitespace, rules, and a limited palette establish hierarchy. Prefer fewer, stronger groups over many small framed objects.

## Professionalism gate

Fail the design review when any of these remain visible:

- tangled, reversed, duplicated, detached, or text-crossing arrows;
- mid-word wrapping, clipped labels, inconsistent type sizes, or emergency-small text;
- gratuitous numbered circles or badge-heavy step headings;
- repeated generic icons, excessive rounded rectangles, or ornamental gradients that do not encode information;
- dense symmetry or decorative repetition that makes the figure look templated rather than authored for its content.
