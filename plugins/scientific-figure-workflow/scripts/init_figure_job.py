#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Initialize a collaborative scientific-figure job")
    parser.add_argument("job_dir")
    parser.add_argument("--owner", default="unassigned")
    args = parser.parse_args()

    root = Path(args.job_dir).expanduser().resolve()
    for rel in (
        "00_source",
        "01_prompt",
        "02_render/candidates",
        "03_reconstruct/assets",
        "03_reconstruct/build",
        "04_qa",
    ):
        (root / rel).mkdir(parents=True, exist_ok=True)

    status = root / "status.json"
    if status.exists():
        raise SystemExit(f"Refusing to overwrite existing job: {status}")
    payload = {
        "job_id": root.name,
        "stage": "source",
        "state": "ready",
        "owner": args.owner,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "inputs": [],
        "outputs": [],
        "hard_gates": {
            "prompt": "pending",
            "render": "pending",
            "reconstruct": "pending",
            "qa": "pending",
        },
        "notes": [],
    }
    status.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(root)


if __name__ == "__main__":
    main()
