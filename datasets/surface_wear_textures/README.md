# Surface Wear Textures

> Close-up images of everyday surfaces at different stages of use and deterioration — shoe soles, keyboard keys, door handles, stair edges, floor tiles, painted walls, book spines.

## Overview

| Field    | Value     |
| -------- | --------- |
| Modality | text      |
| Size     | ~N items  |
| License  | CC-BY-4.0 |
| Version  | 0.1.0     |
| Status   | 🔴 Planned |

## Description

Wear patterns encode usage history. Predictive maintenance, forensic analysis, material science, and even UX research (which button gets pressed most?) all benefit from systematic visual data on how surfaces degrade through interaction.

## Label Schema

| Field           | Type   | Required | Description                                                                  |
| --------------- | ------ | -------- | ---------------------------------------------------------------------------- |
| `wear_level`    | int    | Yes      | 0–5 scale, 0 = new                                                           |
| `material`      | string | Yes      | `metal` `plastic` `wood` `fabric` `rubber` `stone` `paint` `leather` `other` |
| `object`        | string | Yes      | free text, e.g., "office chair armrest"                                      |
| `wear_pattern`  | string | Yes      | `abrasion` `discolouration` `deformation` `cracking` `polishing` `other`     |
| `estimated_age` | int    | No       | How old fo you think the item is? This is optional, ignore if you don't know |
| `severity`      | string | Yes      | `cosmetic` `inconvenient` `rural` `safety_relevant`                          |


## Collection Method

Macro photography of everyday objects. Pairs of new vs. worn versions of the same object type are especially valuable

## Known Limitations

What this dataset does NOT cover, known biases, and caveats.

## Citation

```bibtex
@misc{unconventional_dataset},
  author = {Njoku, Charles},
  title = {{Surface Wear Textures}},
  year = {2026},
  url = {https://github.com/madebycharles/unconventional_datasets/tree/main/datasets/surface_wear_textures}
```