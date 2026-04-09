# Degraded Signage

> Images of signs at various stages of legibility — sun-bleached, partially obscured, vandalised, weathered, poorly lit, or otherwise compromised.

## Overview

| Field    | Value          |
| -------- | -------------- |
| Modality | image          |
| Size     | ~N items       |
| License  | CC-BY-4.0      |
| Version  | 0.1.0          |
| Status   | 🟡 In Progress |

## Description

Autonomous systems, accessibility tools, and OCR pipelines all assume signs are crisp and well-lit. They rarely are. This dataset captures the gradient from perfectly readable to functionally invisible. Most of the images are captured using an iPhone or Smartphone camera.

## Label Schema

| Field              | Type   | Required | Description                                               |
| ------------------ | ------ | -------- | --------------------------------------------------------- |
| `legibility_score` | int    | Yes      | (0–5 scale, 0 = unreadable)                               |
| `degradation_type` | string | Yes      | `faded` `obscured` `damaged` `poorly_lit` `other`         |
| `sign_category`    | string | Yes      | `road` `commercial` `wayfinding` `safety` `informational` |
| `original_text`    | string | Yes      | Text on the sign if readable                              |
| `environment`      | string | Yes      | `urban` `suburban` `rural` `indoor`                       |
| `location`         | string | Yes      | Where was this sign found? Enter as 'city/town, country'  |

## Collection Method

Contributed photos from everyday environments. Phone camera quality is fine.

## Known Limitations

- Geographic bias toward the contributor's home region; signage conventions and degradation patterns vary significantly by country
- Predominantly smartphone photography; controlled or professional imaging is not represented
- Legibility scores are single-annotator ratings with no calibration baseline or reference images
- Night-time and low-light photography is underrepresented in the early collection
- Non-Latin scripts are not currently represented

## Citation

```bibtex
@misc{unconventional_degraded_signage,
  author = {Njoku, Charles},
  title  = {{Degraded Signage}},
  year   = {2026},
  url    = {https://github.com/madebycharles/unconventional_datasets/tree/main/datasets/degraded_signage}
}
```
