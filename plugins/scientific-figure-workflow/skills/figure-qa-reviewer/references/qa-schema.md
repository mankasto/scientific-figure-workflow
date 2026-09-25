# QA report schema

```json
{
  "passed": true,
  "semantic": {"passed": true, "findings": []},
  "visual": {
    "passed": true,
    "connector_routing": {"passed": true, "findings": []},
    "typography": {"passed": true, "findings": []},
    "numbering_and_containers": {"passed": true, "findings": []},
    "publication_size": {"passed": true, "findings": []},
    "findings": []
  },
  "package": {"passed": true, "slide_count": 1, "findings": []},
  "editability": {
    "passed": true,
    "native_shape_count": 0,
    "editable_text_count": 0,
    "connector_count": 0,
    "raster_asset_count": 0,
    "whole_slide_raster_count": 0,
    "findings": []
  }
}
```

Do not infer editability from file extension or visual similarity. Inspect the package or imported presentation object model.
