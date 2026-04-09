"""Validate and ingest degraded signage image metadata.

Usage (batch mode with a JSON manifest):
    python scripts/ingest.py --manifest <manifest.json>

The manifest must be a JSON array of objects matching the label schema.
Image files referenced in the manifest are copied from the manifest's
directory into data/images/. Valid entries are appended to data/labels.json.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

VALID_DEGRADATION_TYPES = {"faded", "obscured", "damaged", "poorly_lit", "other"}
VALID_SIGN_CATEGORIES = {"road", "commercial", "wayfinding", "safety", "informational"}
VALID_ENVIRONMENTS = {"urban", "suburban", "rural", "indoor"}

DATA_DIR = Path(__file__).parent.parent / "data"
IMAGES_DIR = DATA_DIR / "images"
LABELS_FILE = DATA_DIR / "labels.json"


def validate_entry(entry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required: dict[str, type] = {
        "filename": str,
        "legibility_score": int,
        "degradation_type": str,
        "sign_category": str,
        "original_text": str,
        "environment": str,
        "location": str,
    }
    for field, expected_type in required.items():
        if field not in entry:
            errors.append(f"missing required field '{field}'")
        elif not isinstance(entry[field], expected_type):
            errors.append(f"'{field}' must be {expected_type.__name__}")

    score = entry.get("legibility_score")
    if isinstance(score, int) and not (0 <= score <= 5):
        errors.append(f"legibility_score must be 0–5, got {score}")
    if entry.get("degradation_type") not in VALID_DEGRADATION_TYPES:
        errors.append(f"invalid degradation_type '{entry.get('degradation_type')}'")
    if entry.get("sign_category") not in VALID_SIGN_CATEGORIES:
        errors.append(f"invalid sign_category '{entry.get('sign_category')}'")
    if entry.get("environment") not in VALID_ENVIRONMENTS:
        errors.append(f"invalid environment '{entry.get('environment')}'")
    return errors


def load_labels() -> list[dict]:
    if LABELS_FILE.exists():
        with open(LABELS_FILE, encoding="utf-8") as f:
            return json.load(f)
    return []


def save_labels(labels: list[dict]) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    with open(LABELS_FILE, "w", encoding="utf-8") as f:
        json.dump(labels, f, indent=2, ensure_ascii=False)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True,
                        help="JSON manifest file for batch ingestion")
    args = parser.parse_args()

    with open(args.manifest, encoding="utf-8") as f:
        entries = json.load(f)

    if not isinstance(entries, list):
        print("ERROR: manifest must be a JSON array", file=sys.stderr)
        sys.exit(1)

    labels = load_labels()
    ingested = 0
    for i, entry in enumerate(entries):
        errs = validate_entry(entry)
        if errs:
            for err in errs:
                print(f"SKIP  entry[{i}]: {err}", file=sys.stderr)
            continue

        src = args.manifest.parent / entry["filename"]
        if src.exists():
            IMAGES_DIR.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, IMAGES_DIR / entry["filename"])

        labels.append(entry)
        ingested += 1

    save_labels(labels)
    print(f"Ingested {ingested} entries. Total in labels.json: {len(labels)}.")


if __name__ == "__main__":
    main()
