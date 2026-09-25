# Figure specification

Required YAML fields:

```yaml
version: 1
purpose: string
audience: string
figure_type: architecture|concept|mechanism|workflow|graphical-abstract|evaluation
aspect_ratio: string
reading_order: [string]
visual_anchor:
  subject: string
  medium: raster|vector|mixed
regions:
  - id: string
    role: string
    position: string
    treatment: raster|vector|mixed
palette_roles:
  semantic-role: '#RRGGBB'
connector_policy:
  routing: straight|orthogonal|curved|mixed
  direction: string
  crossing_policy: string
typography:
  hierarchy: [string]
  minimum_font_size: string
  wrapping_policy: string
numbering_style: plain-text|eyebrow|reference-defined|none
visible_text: [string]
semantic_invariants: [string]
negative_constraints: [string]
source_evidence: [string]
```

Use `mixed` when a region combines editable diagram structure with a generated scene or other detailed image.

The connector, typography, and numbering fields are required for diagrammatic figures. For figures without flows or numbered stages, use a concise not-applicable value rather than inventing structure.
