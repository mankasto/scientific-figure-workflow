#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

STAGE_FILES = {
    "prompt": ["01_prompt/figure_spec.yaml", "01_prompt/prompt.md", "01_prompt/visible_text.txt"],
    "render": ["02_render/selected.png", "02_render/render_manifest.json"],
    "reconstruct": ["03_reconstruct/final.pptx", "03_reconstruct/component_manifest.json", "03_reconstruct/preview.png"],
    "qa": ["04_qa/qa_report.json", "04_qa/qa_report.md"],
}


def main():
    parser = argparse.ArgumentParser(description="Validate scientific-figure job handoffs")
    parser.add_argument("job_dir")
    args = parser.parse_args()
    root = Path(args.job_dir).expanduser().resolve()
    status_path = root / "status.json"
    errors = []
    if not status_path.exists():
        errors.append("missing status.json")
        status = {}
    else:
        try:
            status = json.loads(status_path.read_text(encoding="utf-8"))
        except Exception as exc:
            status = {}
            errors.append(f"invalid status.json: {exc}")

    for stage, files in STAGE_FILES.items():
        if status.get("hard_gates", {}).get(stage) == "passed":
            for rel in files:
                if not (root / rel).exists():
                    errors.append(f"{stage} gate passed but file is missing: {rel}")

    qa_path = root / "04_qa/qa_report.json"
    if qa_path.exists():
        try:
            qa = json.loads(qa_path.read_text(encoding="utf-8"))
            visual = qa.get("visual", {})
            edit = qa.get("editability", {})
            if qa.get("passed"):
                for check in ("connector_routing", "typography", "numbering_and_containers", "publication_size"):
                    result = visual.get(check)
                    if not isinstance(result, dict):
                        errors.append(f"QA passed without required visual check: {check}")
                    elif result.get("passed") is not True:
                        errors.append(f"QA passed despite failed visual check: {check}")
                for section in ("semantic", "visual", "package", "editability"):
                    if qa.get(section, {}).get("passed") is not True:
                        errors.append(f"QA passed despite failed section: {section}")
            if qa.get("passed") and edit.get("whole_slide_raster_count", 0) > 0:
                errors.append("QA passed despite a whole-slide raster")
            if qa.get("passed") and edit.get("native_shape_count", 0) < 1:
                errors.append("QA passed without native shapes")
        except Exception as exc:
            errors.append(f"invalid qa_report.json: {exc}")

    report = {"passed": not errors, "errors": errors}
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
