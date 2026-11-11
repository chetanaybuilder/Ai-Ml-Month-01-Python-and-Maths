<div align="center">

# Word Frequency Analyzer 📊

> **A lightweight text-processing utility that normalizes a paragraph and reports word frequencies from the command line.**

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=flat-square&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-success?style=flat-square)
![Project](https://img.shields.io/badge/AI%20%26%20ML%20Month%2001-Day%2002-purple?style=flat-square)

</div>

---

## 🧭 Overview

The Word Frequency Analyzer reads a paragraph from standard input, removes ASCII punctuation, converts the remaining text to lowercase, and splits it into words. It counts each word and displays the alphabetically sorted frequencies, total word count, and unique word count.

The implementation is a single Python script and requires no third-party packages.

## 🏗️ System Architecture

```text
[ Paragraph Input ]
        │
        ▼
[ Text Normalization ] ──> Remove ASCII punctuation + convert to lowercase
        │
        ▼
[ Tokenization ] ─────────> Split normalized text into words
        │
        ▼
[ Frequency Counter ] ────> Accumulate counts in a dictionary
        │
        ▼
[ Terminal Report ] ──────> Sorted frequencies + total and unique counts
```

The script processes the input in a single pass after normalization. A dictionary stores each distinct word and its count; the output is sorted by word for consistent reading.

## 📂 Project Structure

```text
Day-02-Word-Frequency-Analyzer/
├── text_analyzer.py       # Input processing and frequency report
├── README.md              # Project documentation
└── screenshots/
    ├── Screenshot1.png    # Input prompt
    ├── Screenshot2.png    # Analysis output
    └── banner.png         # Course banner
```

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or newer
- No third-party packages

### Run

From this directory, execute:

```bash
python text_analyzer.py
```

Enter a paragraph when prompted. On Windows, `py text_analyzer.py` is also supported when the Python launcher is installed.

## 💻 Core Implementation

```python
text = text.translate(str.maketrans("", "", string.punctuation))
text = text.lower()
words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in sorted(frequency.items()):
    print(f"{word}: {count}")

print(f"Total words: {len(words)}")
print(f"Unique words: {len(frequency)}")
```

For example, `Python is powerful. Python is useful. Python is powerful.` produces 9 total words and 4 unique words.

## 💡 Engineering Takeaways

- **Normalization:** Apply consistent casing and remove punctuation before counting.
- **Tokenization:** Use whitespace splitting to create a sequence of words.
- **Dictionary accumulation:** Use `dict.get()` to initialize and increment counts in one operation.
- **Deterministic reporting:** Sort dictionary items so frequency output appears in alphabetical order.
- **Standard-library design:** Use Python's built-in `string` module and data structures without external dependencies.

## 🖼️ Screenshots

### Input prompt

<p align="center">
  <img src="screenshots/Screenshot1.png" alt="Word frequency analyzer input prompt" width="80%">
</p>

### Analysis output

<p align="center">
  <img src="screenshots/Screenshot2.png" alt="Word frequency report in the terminal" width="80%">
</p>

### Course banner

<p align="center">
  <img src="screenshots/banner.png" alt="AI and ML Month 1 course banner" width="80%">
</p>

---

**Author:** [chetanaybuilder](https://github.com/chetanaybuilder) · AI & ML Month 01
