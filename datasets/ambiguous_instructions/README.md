# Ambiguous Instructions

> Real-world written instructions that are technically correct but practically confusing — assembly manuals, recipe steps, wayfinding text, policy language, UI microcopy, medical leaflets.

## Overview

| Field    | Value          |
| -------- | -------------- |
| Modality | text           |
| Size     | ~N items       |
| License  | CC-BY-4.0      |
| Version  | 0.1.0          |
| Status   | 🟡 In Progress |

## Description

NLP models parse grammar well but struggle with pragmatic ambiguity — the kind that makes a human re-read a sentence three times. This is directly relevant to human factors research: if a human misinterprets an instruction, an AI advisory system might too.

## Label Schema

| Field                        | Type   | Required | Description                                                                 |
| ---------------------------- | ------ | -------- | --------------------------------------------------------------------------- |
| `instruction_text`           | string | Yes      | the instruction as-is                                                       |
| `source_category`            | string | Yes      | `product_manual` `recipe` `wayfinding` `policy` `medical` `ui_copy` `other` |
| `source`                     | string | Yes      | Where was the instruction found? Include any brand affiliation.             |
| `ambiguity_type`             | string | Yes      | `syntactic` `referential` `scope` `omission` `jargon` `cultural`            |
| `misinterpretation_examples` | string | Yes      | list of plausible wrong readings                                            |
| `severity`                   | string | Yes      | `cosmetic` `inconvenient` `safety_relevant`                                 |

## Collection Method

Contributed instructions from everyday environments and social media. Manual transcription from real-world sources. No synthetic generation; the point is that these were written by humans who thought they were being clear.

## Known Limitations

- English-language only; ambiguity is highly language-dependent and many patterns do not translate
- Source categories are weighted toward consumer product manuals and recipes; legal contracts, software documentation, and academic writing are underrepresented
- Severity ratings are single-annotator judgements — no inter-annotator agreement has been established
- Synthetic or AI-generated instructions are excluded by design, which limits collection speed
- Misinterpretation examples are researcher-generated, not sourced from users who actually misread the instruction

## Citation

```bibtex
@misc{unconventional_ambiguous_instructions,
  author = {Njoku, Charles},
  title  = {{Ambiguous Instructions}},
  year   = {2026},
  url    = {https://github.com/madebycharles/unconventional_datasets/tree/main/datasets/ambiguous_instructions}
}
```
