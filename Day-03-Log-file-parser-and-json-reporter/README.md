![AI/ML Month 1: Python and Core Mathematics](../assets/readme-banner.png)

# Log File Parser and JSON Reporter

A standard-library command-line utility that counts selected log-level markers and writes a JSON summary.

## Overview

`main.py` reads `app.log` from the current working directory, counts lines containing `INFO`, `WARNING`, or `ERROR`, collects lines classified as errors, and writes the result to `summary.json`.

## Purpose

This project demonstrates basic file processing, conditional classification, aggregation, and JSON serialization for a small offline report.

## Features

- Reads UTF-8 log text using a context manager.
- Counts `INFO`, `WARNING`, and `ERROR` markers.
- Includes the full matching error lines in the report.
- Writes an indented JSON document to `summary.json`.
- Prints a message when the input file cannot be found.

## Core Concepts

- File input/output with explicit text encoding.
- Single-pass iteration and counter-based aggregation.
- Conditional classification and list accumulation.
- JSON serialization using the standard library.
- Targeted handling of a missing input file.

## Technology Stack

- Python 3.6 or later
- Python standard library only; no third-party packages

## Project Structure

```text
Day-03-Log-file-parser-and-json-reporter/
├── app.log
├── main.py
├── README.md
├── summary.json
└── screenshots/
    ├── json-summary.png
    └── terminal-run.png
```

`summary.json` is the included report file; a successful run replaces it.

## Installation and Setup

Install Python 3.6 or later. No package installation or virtual environment is required. Keep `app.log` in the project directory.

## How to Run

Run the command from this project directory so the relative input and output paths resolve as intended:

```console
python main.py
```

On Windows, `py main.py` also works when the Python launcher is installed.

## Usage

The script processes the bundled `app.log` without additional prompts. After a successful run, inspect `summary.json` for the counts and error lines.

## Sample Results

The checked-in `app.log` and `summary.json` contain this report:

| Report field | Value |
|---|---:|
| `Total_logs` (physical lines, including blank lines) | 29 |
| `INFO_logs` | 7 |
| `WARNING_logs` | 3 |
| `ERROR_logs` | 5 |

The JSON report also contains the five error lines.

## Implementation Notes

The parser uses substring checks rather than a formal log format or regular expression. It tests `INFO`, then `WARNING`, then `ERROR` with an `if`/`elif` chain; at most one category is counted per physical line. `Total_logs` is the number of lines returned by `readlines()`, including blank lines.

## Error Handling and Limitations

If `app.log` is missing, the script prints a message and does not create a report. Other file errors are not handled explicitly. The script assumes it is launched from the project directory and overwrites `summary.json` on each successful run.

## Testing

No automated test files are included in this project.

## Learning Outcomes

- Process line-oriented input and aggregate values in one pass.
- Use context managers to manage file handles.
- Serialize structured results as human-readable JSON.

## Future Improvements

- Resolve input and output paths relative to `main.py` rather than the current directory.
- Parse structured log levels instead of matching arbitrary substrings.
- Add automated tests for missing files, empty files, and classification edge cases.

## Project Information

Part of the AI/ML Month 1 Python and Core Mathematics learning series.

Author: [chetanaybuilder](https://github.com/chetanaybuilder)
