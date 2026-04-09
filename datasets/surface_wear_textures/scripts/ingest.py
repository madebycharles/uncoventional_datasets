"""Validate and ingest surface wear texture image metadata.

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

VALID_MATERIALS = {
    "metal", "plastic", "wood", "fabric", "rubber",
    "stone", "paint", "leather", "other",
}
VALID_WEAR_PATTERNS = {
    "abrasion", "discolouration", "deformation", "cracking", "polishing", "other",
}
VALID_SEVERITIES = {"cosmetic", "inconvenient", "safety_relevant"}

DATA_DIR = Path(__file__).parent.parent / "data"
IMAGES_DIR = DATA_DIR / "images"
LABELS_FILE = DATA_DIR / "labels.json"


def validate_entry(entry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required: dict[str, type] = {
        "filename": str,
        "wear_level": int,
        "material": str,
        "object": str,
        "wear_pattern": str,
        "severity": str,
    }
    for field, expected_type in required.items():
        if field not in entry:
            errors.append(f"missing required field '{field}'")
        elif not isinstance(entry[field], expected_type):
            errors.append(f"'{field}' must be {expected_type.__name__}")

    wear = entry.get("wear_level")
    if isinstance(wear, int) and not (0 <= wear <= 5):
        errors.append(f"wear_level must be 0–5, got {wear}")
    if entry.get("material") not in VALID_MATERIALS:
        errors.append(f"invalid material '{entry.get('material')}'")
    if entry.get("wear_pattern") not in VALID_WEAR_PATTERNS:
        errors.append(f"invalid wear_pattern '{entry.get('wear_pattern')}'")
    if entry.get("severity") not in VALID_SEVERITIES:
        errors.append(f"invalid severity '{entry.get('severity')}'")

    if "estimated_age" in entry and entry["estimated_age"] is not None:
        if not isinstance(entry["estimated_age"], int):
            errors.append("optional field 'estimated_age' must be int if provided")
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
