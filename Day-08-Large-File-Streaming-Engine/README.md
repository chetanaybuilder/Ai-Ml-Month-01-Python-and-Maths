# Day 08 - Large File Streaming Engine

A lightweight Python utility that reads a log file one line at a time, counts
`INFO`, `WARNING`, and `ERROR` records, and writes the summary to a JSON report.
The reader is a generator, so it does not need to load the entire log file into
memory before processing.

## Features

- Streams log records line by line.
- Counts total records and supported severity levels.
- Recognizes severity labels after a timestamp.
- Ignores blank lines and `#` comment lines in the input.
- Saves the summary as formatted JSON.
- Uses only the Python standard library.

## Requirements

- Python 3.8 or newer

There are no third-party package dependencies. The included `requirements.txt`
is intentionally empty of package installs.

## Project structure

```text
Day-08-Large-File-Streaming-Engine/
├── data/
│   └── sample.log
├── src/
│   ├── genrator.py
│   ├── processor.py
│   └── storage.py
├── main.py
├── report.json
└── requirements.txt
```

## Run

From this project directory, run:

```powershell
python main.py
```

The script reads `data/sample.log` and creates or replaces `report.json` in the
project directory.

## Input format

Each log record should contain one of the supported severity labels:
`INFO`, `WARNING`, or `ERROR`. The sample uses timestamped records, for example:

```text
2026-11-16 09:00:01 INFO Application started successfully
```

Blank lines and lines beginning with `#` are treated as comments and excluded
from the totals.

## Example output

For the included sample data, the generated report is:

```json
{
  "total": 30,
  "info": 19,
  "warning": 6,
  "error": 5
}
```

## Dependency installation

No installation is required beyond Python. To check the dependency manifest:

```powershell
python -m pip install -r requirements.txt
```
