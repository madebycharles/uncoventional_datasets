# Ambiguous Instructions

> Real-world written instructions that are technically correct but practically confusing — assembly manuals, recipe steps, wayfinding text, policy language, UI microcopy, medical leaflets.

## Overview

| Field    | Value     |
| -------- | --------- |
| Modality | text      |
| Size     | ~N items  |
| License  | CC-BY-4.0 |
| Version  | 0.1.0     |
| Status   | 🔴 Planned |

## Description

Autonomous systems, accessibility tools, and OCR pipelines all assume signs are crisp and well-lit. They rarely are. This dataset captures the gradient from perfectly readable to functionally invisible. Most of the images are captured using an iPhone or Smartphone camera.

## Label Schema

| Field                        | Type   | Required | Description                                                                 |
| ---------------------------- | ------ | -------- | --------------------------------------------------------------------------- |
| `instruction_text`           | string | Yes      | the instruction as-is                                                       |
| `source_category`            | string | Yes      | `product_manual` `recipe` `wayfinding` `policy` `medical` `ui_copy` `other` |
| `source`                     | string | Yes      | Where was the instruction found? Include any brand affiliation.             |
| `ambiguity_type`             | string | Yes      | `syntactic` `referential` `scope` `omission` `jargon` `cultural`            |
| `misinterpretation_examples` | string | Yes      | list of plausible wrong readings                                            |
| `severity`                   | string | Yes      | `cosmetic` `inconvenient` `rural` `safety_relevant`                         |


## Collection Method

Contributed instructions from everyday environments and social media. Manual transcription from real-world sources. No synthetic generation; the point is that these were written by humans who thought they were being clear.

## Known Limitations

What this dataset does NOT cover, known biases, and caveats.

## Citation

```bibtex
@misc{unconventional_dataset},
  author = {Njoku, Charles},
  title = {{Ambiguous Instructions}},
  year = {2026},
  url = {https://github.com/madebycharles/unconventional_datasets/tree/main/datasets/ambiguous_instructions}
```
