"""Validate all metadata.yaml files in the datasets/ directory.

Usage:
    python schema/validate.py

Exits with code 0 if all files pass, 1 if any errors are found.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REQUIRED_FIELDS: dict[str, type] = {
    "name": str,
    "version": str,
    "description": str,
    "author": str,
    "license": str,
    "modality": str,
    "size": str,
    "labelling_method": str,
    "source": str,
    "tags": list,
    "created": str,
}

VALID_MODALITIES = {"image", "text", "audio", "multimodal"}
VALID_LABELLING_METHODS = {"manual", "semi-automated", "programmatic"}
VALID_SOURCES = {"original-collection", "web-scraped", "derived"}

# Values that indicate the file is still an unfilled template
TEMPLATE_SENTINELS: dict[str, object] = {
    "name": "dataset-slug",
    "description": "One-line description",
    "created": "YYYY-MM-DD",
    "size": "~number of items",
}


def validate(path: Path) -> list[str]:
    errors: list[str] = []

    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        return ["file is empty or not a YAML mapping"]

    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in data:
            errors.append(f"missing required field '{field}'")
        elif not isinstance(data[field], expected_type):
            actual = type(data[field]).__name__
            errors.append(
                f"field '{field}' must be {expected_type.__name__}, got {actual}"
            )

    for field, sentinel in TEMPLATE_SENTINELS.items():
        if data.get(field) == sentinel:
            errors.append(f"field '{field}' is still the template placeholder value")

    if "modality" in data and data["modality"] not in VALID_MODALITIES:
        errors.append(
            f"'modality' must be one of {sorted(VALID_MODALITIES)}, got '{data['modality']}'"
        )
    if "labelling_method" in data and data["labelling_method"] not in VALID_LABELLING_METHODS:
        errors.append(
            f"'labelling_method' must be one of {sorted(VALID_LABELLING_METHODS)}, "
            f"got '{data['labelling_method']}'"
        )
    if "source" in data and data["source"] not in VALID_SOURCES:
        errors.append(
            f"'source' must be one of {sorted(VALID_SOURCES)}, got '{data['source']}'"
        )

    return errors


def main() -> None:
    root = Path(__file__).resolve().parent.parent / "datasets"
    files = sorted(root.glob("*/metadata.yaml"))

    if not files:
        print("No metadata.yaml files found under datasets/.")
        sys.exit(1)

    all_errors: dict[Path, list[str]] = {}
    for path in files:
        errs = validate(path)
        if errs:
            all_errors[path] = errs

    if all_errors:
        for path, errs in all_errors.items():
            for err in errs:
                print(f"ERROR  {path.relative_to(root.parent)}: {err}")
        sys.exit(1)

    print(f"OK  {len(files)} metadata.yaml file(s) passed validation.")


if __name__ == "__main__":
    main()
