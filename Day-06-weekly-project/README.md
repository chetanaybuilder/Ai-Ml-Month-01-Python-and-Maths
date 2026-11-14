# Study Tracker

A clean, beginner-friendly command-line project for tracking study sessions, viewing saved records, and calculating total study time by subject.

## Overview

This application helps learners log how much time they spend studying different subjects and chapters. It stores the data in a local JSON file and exposes a simple terminal-based menu for quick interaction.

## Features
- Add a new study session with subject, chapter, date, and duration
- View all previously saved sessions
- Calculate total study time across all sessions
- See time spent per subject for better progress tracking
- Lightweight JSON-based persistence without external databases

## Project Structure

```text
study-tracker/
├── .gitignore
├── main.py
├── requirements.txt
├── README.md
├── data/
│   └── session.json
├── tests/
│   └── test_operation.py
├── trackers/
│   ├── __init__.py
│   ├── operation.py
│   ├── statistics.py
│   └── storage.py
└── __pycache__/
```

## Requirements
- Python 3.10+

## Setup

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python main.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Example Menu

```text
1. Add session
2. View sessions
3. View statistics
4. Exit
```

## Notes

This project is designed for learning and small personal productivity tracking. It is intentionally simple, easy to read, and suitable for GitHub showcases or academic assignments.
