# Contributing to Unconventional Datasets

Thanks for your interest. Here's how to contribute well.

## Adding Data to an Existing Dataset

1. Read the dataset's `README.md` for its specific label schema
2. Place your files in the appropriate `data/` directory
3. Fill in all required metadata fields — leave optional fields blank rather than guessing
4. Include at least one example in `examples/` if you're adding a new category
5. Open a PR with a clear description of what you collected and how

## Proposing a New Dataset

Open an Issue with:
- **Name**: A short, descriptive slug
- **What**: One paragraph on what the dataset contains
- **Why**: One paragraph on why it's useful and underserved
- **Modality**: Image, text, audio, or multimodal
- **Label schema**: Draft fields and types
- **Collection method**: How you'd gather the data

## Labelling Standards

- **Honest uncertainty wins.** If you're unsure about a label, mark it as uncertain rather than guessing. A dataset with calibrated confidence is more valuable than one with false precision.
- **Use the full scale.** If a field is 0–5, use all six values — don't cluster around 3.
- **Document edge cases.** If something doesn't fit the schema cleanly, note it in a comment field rather than forcing it into a category.

## Quality Over Volume

Ten well-labelled images beat a hundred sloppy ones. Take your time.

## Code Contributions

- Collection or cleaning scripts go in the dataset's `scripts/` directory
- Use Python 3.10+ with type hints
- Include a brief docstring explaining what the script does
- Pin dependencies in a `requirements.txt` if applicable

## License

By contributing, you agree that your contributions are licensed under CC-BY-4.0 (data) and MIT (code).
