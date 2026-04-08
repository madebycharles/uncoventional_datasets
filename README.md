# Unconventional Datasets

Open-source datasets of commonly uncommon things — the long tail of everyday phenomena that nobody bothers to systematically catalogue.

## Why This Exists

Foundation models are trained on the obvious. They stumble on the subtle: the difference between drizzle and mist, a faded road sign vs. a new one, the way handwriting changes when someone is writing standing up. This project builds small, well-labelled datasets that fill those gaps. Every dataset here follows one principle: **if a human would pause before labelling it, it belongs here.**

## Repository Structure

```
unconventional-datasets/
├── datasets/
│   ├── {dataset-name}/
│   │   ├── README.md          # Dataset card (description, schema, provenance, license)
│   │   ├── metadata.yaml      # Machine-readable metadata
│   │   ├── data/              # Raw data (or pointers to HF hosting for large files)
│   │   ├── scripts/           # Collection, cleaning, or augmentation scripts
│   │   └── examples/          # Sample items for quick inspection
│   └── ...
├── schema/
│   └── dataset-card.template.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Metadata Schema

Every dataset ships with a `metadata.yaml`:

```yaml
name: dataset-slug
version: "0.1.0"
description: One-line description
author: Charles Njoku
license: CC-BY-4.0
modality: image | text | audio | multimodal
size: ~number of items
labelling_method: manual | semi-automated | programmatic
source: original-collection | web-scraped | derived
tags: [tag1, tag2]
created: YYYY-MM-DD
```

## Datasets

| #   | Dataset                  | Modality | Status        |
| --- | ------------------------ | -------- | ------------- |
| 1   | `degraded-signage`       | Image    | 🟡 In Progress |
| 2   | `ambiguous-instructions` | Text     | 🟡 In Progress |
| 3   | `surface-wear-textures`  | Image    | 🟡 In Progress |

---

### 3 · Surface Wear Textures

**What:** Close-up images of everyday surfaces at different stages of use and deterioration — shoe soles, keyboard keys, door handles, stair edges, floor tiles, painted walls, book spines.

**Why it matters:** Wear patterns encode usage history. Predictive maintenance, forensic analysis, material science, and even UX research (which button gets pressed most?) all benefit from systematic visual data on how surfaces degrade through interaction.

**Label schema:**
- `wear_level` (0–5 scale, 0 = new)
- `material` (metal | plastic | wood | fabric | rubber | stone | paint | leather | other)
- `object` (free text, e.g., "office chair armrest")
- `wear_pattern` (abrasion | discolouration | deformation | cracking | polishing)
- `estimated_age` (optional, order of magnitude)

**Collection method:** Macro photography of everyday objects. Pairs of new vs. worn versions of the same object type are especially valuable.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version:

1. Pick a dataset (or propose a new one via Issue)
2. Follow the metadata schema
3. Label honestly — uncertain labels are better than wrong labels
4. Open a PR

## License

Datasets: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
Code: [MIT](LICENSE)
