![AI/ML Month 1: Python and Core Mathematics](../assets/readme-banner.png)

# Calculator: Modules, Packages, and Testing

An interactive command-line calculator that separates arithmetic functions into a package and exercises them with pytest.

## Overview

The `calculator` package contains one module for each arithmetic operation. `main.py` provides an interactive interface that dispatches the selected operator to the corresponding function. The tests verify representative results and division by zero.

## Purpose

This project demonstrates how to organize reusable functions into a Python package, keep command-line interaction separate from arithmetic, and test the operations independently.

## Features

- Supports addition, subtraction, multiplication, and division.
- Repeats calculations until the user enters `q`.
- Reports an invalid operator, non-numeric input, or division by zero.
- Includes pytest tests for all four operations and the division-by-zero case.

## Core Concepts

- Python packages and module imports.
- Mapping operator strings to functions.
- A command-line loop with targeted exception handling.
- Parameterized tests with pytest.

## Technology Stack

- Python 3.10 or later (as specified by this project)
- pytest, installed from `requirements-dev.txt`

## Project Structure

```text
Day-05-Python-Modules-Packages-Testing/
├── calculator/
│   ├── __init__.py
│   ├── addition.py
│   ├── division.py
│   ├── multiplication.py
│   └── subtraction.py
├── tests/
│   └── test_calculator.py
├── main.py
├── README.md
└── requirements-dev.txt
```

## Installation and Setup

From this project directory, create and activate a virtual environment, then install the test dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

On macOS or Linux, activate the environment with:

```sh
source .venv/bin/activate
```

## How to Run

With the environment active:

```console
python main.py
```

## Usage

Choose `+`, `-`, `*`, or `/`, then enter two numeric values. The prompt repeats after a calculation or handled input error. Enter `q` at the operation prompt to exit.

The arithmetic functions can also be imported directly, for example:

```python
from calculator.division import division

result = division(20, 10)
```

## Implementation Notes

The operation functions contain only the arithmetic expressions. `main.py` maps operator symbols to those functions, reads and converts operands to `float`, and handles errors at the user-interface boundary.

## Error Handling and Limitations

Unknown operators are rejected before requesting operands. Failed float conversion and `ZeroDivisionError` are caught and reported by the CLI. The operation functions themselves do not validate operand types or provide decimal-specific precision; division by zero is surfaced as `ZeroDivisionError`.

## Testing

Run the existing pytest suite from this project directory:

```console
python -m pytest
```

`tests/test_calculator.py` checks the four arithmetic operations with representative inputs and verifies that division by zero raises `ZeroDivisionError`.

## Learning Outcomes

- Split related behavior into importable modules within a package.
- Keep the user interface separate from calculation logic.
- Use parameterized tests to apply the same assertion shape to multiple functions.

## Future Improvements

- Add tests for invalid CLI input and operator selection.
- Define an explicit policy for precision and supported numeric types.
- Add type annotations to the operation functions.

## Project Information

Part of the AI/ML Month 1 Python and Core Mathematics learning series.

Author: [chetanaybuilder](https://github.com/chetanaybuilder)
