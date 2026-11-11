<div align="center">

# Log File Parser + JSON Reporter 🧾

> **A small, dependency-free Python utility for summarizing log levels and exporting a structured JSON report.**

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=flat-square&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-success?style=flat-square)
![Output](https://img.shields.io/badge/Output-JSON-8250DF?style=flat-square)

</div>

---

## 🧭 Overview

The parser reads `app.log`, counts lines containing `INFO`, `WARNING`, and `ERROR`, and collects the complete lines classified as errors. It writes the counts and error messages to an indented `summary.json` file.

The project uses Python's standard library and runs as a single command-line script.

## 🏗️ System Architecture

```text
[ app.log ]
     │
     ▼
[ File Read ] ────────────> Read UTF-8 input with a context manager
     │
     ▼
[ Log Classification ] ───> Count INFO, WARNING, and ERROR entries
     │
     ▼
[ Error Collection ] ─────> Retain complete error lines
     │
     ▼
[ JSON Serialization ] ───> Write formatted summary.json
```

`main.py` reads the input file, classifies each line, assembles the completed summary, and serializes it to JSON. If `app.log` is missing, the script prints a clear message instead of writing a report.

## 📂 Project Structure

```text
Day-03-Log-file-parser-and-json-reporter/
├── app.log                   # Sample log input
├── main.py                   # Parser and JSON report generation
├── summary.json              # Generated report
├── README.md                 # Project documentation
└── screenshots/
    ├── terminal-run.png      # Successful terminal execution
    └── json-summary.png      # Generated summary preview
```

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or newer
- No third-party packages

### Run

From this directory, execute:

```bash
python main.py
```

On Windows, `py main.py` is also supported when the Python launcher is installed. Keep `app.log` in the working directory when running the script. Each successful run replaces `summary.json`.

## 💻 Core Implementation

```python
for line in lines:
    if "INFO" in line:
        INFO_count += 1
    elif "WARNING" in line:
        WARNING_count += 1
    elif "ERROR" in line:
        ERROR_count += 1
        error_messages.append(line.strip())

summary = {
    "Total_logs": len(lines),
    "INFO_logs": INFO_count,
    "WARNING_logs": WARNING_count,
    "ERROR_logs": ERROR_count,
    "error_messages": error_messages,
}

with open("summary.json", "w", encoding="utf-8") as file:
    json.dump(summary, file, indent=4)
```

## 📊 Sample Results

The included `app.log` produces:

| Metric | Result |
|:--|--:|
| Total lines (`Total_logs`) | 29 |
| INFO entries | 7 |
| WARNING entries | 3 |
| ERROR entries | 5 |

`Total_logs` is the number of physical lines read, including blank lines. The JSON report also includes all five error lines.

## 💡 Engineering Takeaways

- **Resource safety:** Use context managers to close input and output files reliably.
- **Single-pass processing:** Classify and count each line in one loop.
- **Structured output:** Serialize a Python dictionary to readable JSON with `json.dump()`.
- **Targeted error handling:** Handle the expected missing-input case with `FileNotFoundError`.
- **Explicit encoding:** Open text files as UTF-8 for predictable text handling.

## 🖼️ Screenshots

### Terminal execution

<p align="center">
  <img src="screenshots/terminal-run.png" alt="Terminal showing parser banner and successful JSON export" width="80%">
</p>

### Generated JSON summary

<p align="center">
  <img src="screenshots/json-summary.png" alt="JSON report with log counts and error messages" width="80%">
</p>

---

**Author:** [chetanaybuilder](https://github.com/chetanaybuilder) · AI & ML Month 01
