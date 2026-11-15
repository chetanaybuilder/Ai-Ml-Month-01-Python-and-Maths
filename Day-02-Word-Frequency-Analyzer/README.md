![AI/ML Month 1: Python and Core Mathematics](../assets/readme-banner.png)

# Word Frequency Analyzer

A dependency-free command-line script that normalizes a paragraph and reports the frequency of each word.

## Overview

The analyzer reads one paragraph from standard input, removes ASCII punctuation, lowercases the text, and splits it on whitespace. It prints each word's count in alphabetical order, followed by total and unique token counts.

## Purpose

This project demonstrates a compact text-processing pipeline using Python's string utilities, whitespace tokenization, and dictionary-based counting.

## Features

- Accepts a paragraph entered at the terminal.
- Removes characters listed in `string.punctuation` and normalizes case.
- Counts tokens and prints their frequencies in sorted order.
- Reports total token count and the number of unique tokens.

## Core Concepts

- `str.translate()` and `str.maketrans()` for punctuation removal.
- `str.lower()` and `str.split()` for normalization and tokenization.
- Dictionary accumulation with `dict.get()`.
- Sorting dictionary items to produce stable, readable output.

## Technology Stack

- Python 3.6 or later
- Python standard library only; no third-party packages

## Project Structure

```text
Day-02-Word-Frequency-Analyzer/
├── text_analyzer.py
├── README.md
└── screenshots/
    ├── Screenshot1.png
    └── Screenshot2.png
```

## Installation and Setup

Install Python 3.6 or later. No package installation or virtual environment is required.

## How to Run

From this project directory:

```console
python text_analyzer.py
```

On Windows, `py text_analyzer.py` also works when the Python launcher is installed.

## Usage

At the prompt, enter a paragraph. For example:

```text
Python is useful. Python is readable.
```

The script reports normalized word counts and the total and unique token counts.

## Implementation Notes

All processing is performed in `text_analyzer.py`. Punctuation is removed before lowercasing and splitting; the resulting words are counted in a dictionary and sorted alphabetically for display.

## Error Handling and Limitations

The script has no custom error handling for terminal input. Punctuation handling follows Python's ASCII `string.punctuation` constant, not a Unicode-aware tokenizer. Punctuation is deleted rather than treated as a separator, so text such as `well-known` becomes `wellknown`; an empty input produces zero total and unique words.

## Testing

No automated test files are included in this project.

## Learning Outcomes

- Apply a sequence of normalization steps before analyzing text.
- Count repeated values using a dictionary.
- Separate data processing from the ordering used for presentation.

## Future Improvements

- Add a testable function that accepts text and returns a report.
- Define Unicode punctuation and tokenization behavior explicitly.
- Support input from a text file as well as a terminal prompt.

## Project Information

Part of the AI/ML Month 1 Python and Core Mathematics learning series.

Author: [chetanaybuilder](https://github.com/chetanaybuilder)
