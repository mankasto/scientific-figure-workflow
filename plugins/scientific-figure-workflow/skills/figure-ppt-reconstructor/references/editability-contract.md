# Editability contract

A reconstructed PPTX passes when:

- every visible label likely to be revised is native editable text;
- structural panels, nodes, arrows, borders, metric bars, and simple legends are native shapes or editable vector groups;
- each retained raster region is independently replaceable and tightly bounded;
- there is no full-slide screenshot used as the visual implementation;
- the manifest reports object counts and the preview contains no clipping or duplicate baked-in labels.

Report PowerPoint conversion or ungrouping as tested only when it was actually performed in Microsoft PowerPoint.
