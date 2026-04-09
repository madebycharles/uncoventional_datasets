"""Validate and ingest ambiguous instruction entries from a JSON source file.

Usage:
    python scripts/ingest.py <source.json>

The source must be a JSON array of objects matching the label schema.
Valid entries are appended to data/entries.json; invalid entries are
reported to stderr and skipped.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_FIELDS: dict[str, type] = {
    "instruction_text": str,
    "source_category": str,
    "source": str,
    "ambiguity_type": str,
    "misinterpretation_examples": list,
    "severity": str,
}

VALID_SOURCE_CATEGORIES = {
    "product_manual", "recipe", "wayfinding", "policy", "medical", "ui_copy", "other",
}
VALID_AMBIGUITY_TYPES = {
    "syntactic", "referential", "scope", "omission", "jargon", "cultural",
}
VALID_SEVERITIES = {"cosmetic", "inconvenient", "safety_relevant"}


def validate_entry(entry: dict[str, Any], index: int) -> list[str]:
    errors: list[str] = []
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in entry:
            errors.append(f"entry[{index}]: missing required field '{field}'")
        elif not isinstance(entry[field], expected_type):
            errors.append(f"entry[{index}]: '{field}' must be {expected_type.__name__}")
    if entry.get("source_category") not in VALID_SOURCE_CATEGORIES:
        errors.append(f"entry[{index}]: invalid source_category '{entry.get('source_category')}'")
    if entry.get("ambiguity_type") not in VALID_AMBIGUITY_TYPES:
        errors.append(f"entry[{index}]: invalid ambiguity_type '{entry.get('ambiguity_type')}'")
    if entry.get("severity") not in VALID_SEVERITIES:
        errors.append(f"entry[{index}]: invalid severity '{entry.get('severity')}'")
    return errors


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: python {Path(sys.argv[0]).name} <source.json>", file=sys.stderr)
        sys.exit(1)

    source = Path(sys.argv[1])
    with open(source, encoding="utf-8") as f:
        raw = json.load(f)

    if not isinstance(raw, list):
        print("ERROR: source file must be a JSON array", file=sys.stderr)
        sys.exit(1)

    valid: list[dict] = []
    skipped = 0
    for i, entry in enumerate(raw):
        errs = validate_entry(entry, i)
        if errs:
            for err in errs:
                print(f"SKIP  {err}", file=sys.stderr)
            skipped += 1
        else:
            valid.append(entry)

    out_path = Path(__file__).parent.parent / "data" / "entries.json"
    out_path.parent.mkdir(exist_ok=True)

    existing: list[dict] = []
    if out_path.exists():
        with open(out_path, encoding="utf-8") as f:
            existing = json.load(f)

    existing.extend(valid)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    print(
        f"Ingested {len(valid)} entries ({skipped} skipped). "
        f"Total in {out_path.name}: {len(existing)}."
    )


if __name__ == "__main__":
    main()
