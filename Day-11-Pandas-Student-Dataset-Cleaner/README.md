# 🎓 Day-11-Pandas-Student-Dataset-Cleaner

> A professional, production-ready Python project that cleans and analyzes a messy student dataset using **pandas**. Part of the **AI-ML Month 01: Python and Maths** learning journey.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-2.0.0+-150458?logo=pandas)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Cleaning Pipeline](#data-cleaning-pipeline)
- [Sample Output](#sample-output)
- [Configuration](#configuration)
- 🛠️ [Tech Stack](#tech-stack)
- [License](#license)
- [Author](#author)

---

## 📌 Overview

The **Day-11-Pandas-Student-Dataset-Cleaner** demonstrates end-to-end data preprocessing with pandas. It reads a raw, messy student dataset (`data/messy_student.csv`) containing common real-world data quality issues — such as leading/trailing whitespace, duplicate rows, missing values, out-of-range numeric entries, and non-numeric placeholders — and produces a clean, analysis-ready dataset (`cleaned_student.csv`) along with per-class performance statistics.

---

## ✨ Features

- 🧹 **Whitespace trimming** – cleans string columns (`Name`, `Class`)
- 🗑️ **Duplicate removal** – drops identical rows
- 🔢 **Type coercion** – converts `Marks` and `Attendance` to numeric, turning invalid entries into `NaN`
- 🚫 **Out-of-range handling** – flags values outside the valid `0–100` range as missing
- 📊 **Mean imputation** – fills missing numeric values with column mean, rounded to integers
- 📈 **Class-wise aggregation** – computes mean, max, min, and sum of marks per class
- 💾 **Clean export** – saves the sanitized dataset sorted by `Student_ID`
- ⚙️ **Environment configuration** – configurable paths via `.env`

---

## 📂 Project Structure

```
Day-11-Pandas-Student-Dataset-Cleaner/
│
├── data/
│   └── messy_student.csv          # Raw, uncleaned input dataset
│
├── main.py                        # Data cleaning & analysis script
├── cleaned_student.csv            # Cleaned output dataset (generated)
│
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables (local secrets/config)
├── .gitignore                     # Git ignore rules
└── README.md                      # Project documentation
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/chetanaybuilder/Ai-Ml-Month-01-Python-and-Maths.git
cd Ai-Ml-Month-01-Python-and-Maths/Day-11-Pandas-Student-Dataset-Cleaner
```

### 2. Create a virtual environment (recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Copy `.env` and adjust the values if needed:

```bash
copy .env .env.local   # Windows
cp .env .env.local     # macOS / Linux
```

---

## ▶️ Usage

Run the cleaning pipeline:

```bash
python main.py
```

**What happens:**
1. Reads `data/messy_student.csv`
2. Applies the full cleaning pipeline
3. Prints the cleaned DataFrame and class-wise statistics to the console
4. Writes `cleaned_student.csv` to the project root

**Expected console output:**
```
cleaned dataset saved sucessfully!
```

---

## 🧼 Data Cleaning Pipeline

| Step | Transformation | Columns Affected |
|------|----------------|------------------|
| 1 | Strip leading/trailing whitespace | `Name`, `Class` |
| 2 | Remove duplicate rows | All |
| 3 | Convert to numeric (`errors="coerce"`) | `Marks`, `Attendance` |
| 4 | Mask values outside `0–100` as `NaN` | `Marks`, `Attendance` |
| 5 | Fill `NaN` with column mean (rounded to int) | `Marks`, `Attendance` |
| 6 | Sort by `Student_ID` | All |
| 7 | Export to CSV | `cleaned_student.csv` |

Additionally, the script computes class-wise statistics:

```text
              mean   max  min  sum
Class
11A          84.5   92   67   ...
11B          85.2   94   78   ...
```

---

## 📋 Sample Output (`cleaned_student.csv`)

```csv
Student_ID,Name,Class,Subject,Marks,Attendance
101,Aman,11A,Maths,90,95
102,Riya,11A,Maths,84,88
103,Rahul,11B,Physics,85,92
104,Karan,11A,Chemistry,75,80
105,Priya,11B,Physics,84,90
...
```

---

## ⚙️ Configuration

Edit `.env` to customize behavior:

```env
PROJECT_NAME=Day-11-Pandas-Student-Dataset-Cleaner
INPUT_DATA_PATH=data/messy_student.csv
OUTPUT_DATA_PATH=cleaned_student.csv
LOG_LEVEL=INFO
```

> ⚠️ Never commit real secrets to `.env`. It is already covered by `.gitignore`.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.10+ |
| Data Manipulation | pandas 2.0.0 |
| Env Management | python-dotenv |
| Version Control | Git & GitHub |

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Chetanay Batta**  
GitHub: [@chetanaybuilder](https://github.com/chetanaybuilder)  
Email: chetanaybatta361@gmail.com  
Repo: [Ai-Ml-Month-01-Python-and-Maths](https://github.com/chetanaybuilder/Ai-Ml-Month-01-Python-and-Maths)

---

## 🙏 Acknowledgments

Built as part of the **AI-ML Month 01 – Python and Maths** curriculum.  
Thank you for exploring this project! ⭐ Don't forget to star the repo if you found it helpful.