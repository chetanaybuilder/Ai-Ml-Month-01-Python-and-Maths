# Day 05: Python Modules, Packages, and Testing

A small command-line calculator demonstrating how to organize arithmetic
operations as reusable Python modules, group them in a package, and verify
their behavior with pytest.

## Features

- Addition, subtraction, multiplication, and division.
- Interactive command-line input with an option to quit.
- Clear handling of invalid operations, non-numeric input, and division by
  zero.
- Focused unit tests for each operation and the division-by-zero case.

## Project structure

```text
Day-05-Python-Modules-Packages-Testing/
|-- calculator/
|   |-- __init__.py
|   |-- addition.py
|   |-- division.py
|   |-- multiplication.py
|   `-- subtraction.py
|-- tests/
|   `-- test_calculator.py
|-- main.py
|-- README.md
`-- requirements-dev.txt
```

Each operation is implemented independently in `calculator/`. The package
keeps those functions reusable, while `main.py` provides the interactive
interface and `tests/` verifies the calculation behavior.

## Requirements

- Python 3.10 or later
- pytest (for running the test suite)

## Setup

Create and activate a virtual environment, then install the development
dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

On macOS or Linux, activate the environment with
`source .venv/bin/activate`.

## Run the calculator

```powershell
python main.py
```

Choose `+`, `-`, `*`, or `/`, enter two numbers, and repeat as needed. Enter
`q` at the operation prompt to exit.

## Run the tests

From the project directory:

```powershell
python -m pytest
```
