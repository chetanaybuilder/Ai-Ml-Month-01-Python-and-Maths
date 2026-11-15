![AI/ML Month 1: Python and Core Mathematics](../assets/readme-banner.png)

# Study Tracker

A command-line application for recording study sessions in JSON and summarizing study time by subject.

## Overview

The tracker provides a terminal menu to add sessions, view saved records, and calculate aggregate statistics. Session data is persisted locally in `data/session.json`; no database service is required.

## Purpose

This weekly project brings together a small command-line interface, separated application modules, JSON file persistence, and automated tests.

## Features

- Adds a session with a subject, chapter, date string, and duration in minutes.
- Lists previously saved sessions.
- Reports session count, total minutes, and minutes grouped by subject.
- Persists session records in a local JSON file.
- Includes tests for adding, retrieving, and summarizing session data.

## Core Concepts

- Separating CLI, operations, statistics, and storage responsibilities.
- Reading and writing JSON with `pathlib` and context-managed files.
- Aggregating records using dictionaries and counters.
- Testing with `unittest`, temporary files, and `unittest.mock.patch`.

## Technology Stack

- Python 3.10 or later (as specified by this project)
- Runtime logic uses the Python standard library.
- `requirements.txt` lists pytest; the checked-in tests use the standard-library `unittest` runner.

## Project Structure

```text
Day-06-weekly-project/
├── data/
│   └── session.json
├── tests/
│   ├── __init__.py
│   └── test_operation.py
├── trackers/
│   ├── __init__.py
│   ├── operation.py
│   ├── statistics.py
│   └── storage.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

`main.py` handles prompts and presentation. `trackers/operation.py` adds and retrieves records, `trackers/statistics.py` calculates totals, and `trackers/storage.py` reads and writes the JSON file.

## Installation and Setup

From this project directory, create and activate a virtual environment and install the listed dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```sh
source .venv/bin/activate
```

The application itself uses only the standard library; pytest is listed in the requirements file.

## How to Run

From this project directory:

```console
python main.py
```

Choose `1` to add a session, `2` to view sessions, `3` for statistics, or `4` to exit.

## Usage

When adding a session, provide a subject, chapter, date string, and an integer duration in minutes. The date prompt requests `YYYY-MM-DD`, but the application stores the supplied string without validating the date format.

The statistics view reports the count and total minutes for all records in `data/session.json`, along with totals grouped by subject.

## Implementation Notes

The storage module resolves `data/session.json` relative to the project location, not the current working directory. Session records are dictionaries containing `subject`, `date`, `duration`, and `chapter`. Statistics convert each duration to an integer and sum values by subject.

## Error Handling and Limitations

The CLI rejects non-integer durations and empty subject, chapter, or date fields. It does not reject zero or negative durations and does not validate date formats. The storage loader returns an empty list when the file is absent, empty, malformed, unreadable, or contains a JSON value other than a list; this can make a storage problem appear like an empty tracker. Save errors are not caught by the storage layer.

## Testing

Run the existing standard-library tests from this project directory:

```console
python -m unittest discover -s tests -v
```

The tests cover adding a record, reading saved records, and calculating total and per-subject statistics using temporary files.

## Learning Outcomes

- Split an application into modules with distinct responsibilities.
- Persist structured records using JSON and `pathlib`.
- Test file-backed behavior without changing the project's real data file.

## Future Improvements

- Validate date strings and require positive durations.
- Report malformed or unreadable storage explicitly instead of treating it as empty.
- Add tests for invalid input and storage edge cases.
- Provide a backup or export workflow for the session data.

## Project Information

Part of the AI/ML Month 1 Python and Core Mathematics learning series.

Author: [chetanaybuilder](https://github.com/chetanaybuilder)
