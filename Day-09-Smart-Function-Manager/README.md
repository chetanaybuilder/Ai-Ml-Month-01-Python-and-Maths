# Day-09-Smart-Function-Manager

A lightweight Python utility that demonstrates a reusable **monitoring decorator**.  
The `monitor` decorator logs every invocation of a decorated function — including
call count, positional/keyword arguments, and the return value — while keeping the
original function's behavior and metadata intact.

## Project Structure

```
Day-09-Smart-Function-Manager/
├── main.py                # Entry point demonstrating the decorator
├── decorators/
│   ├── __init__.py        # Package marker (optional)
│   └── manager.py         # Reusable `monitor` decorator
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Features

*   **Per-function call counting** — each decorated function tracks its own call
    number independently.
*   **Argument logging** — positional and keyword arguments are printed on every
    call.
*   **Result logging** — the return value is displayed after execution.
*   **Transparent wrapper** — the decorated function returns its original result
    and preserves `__name__`, `__doc__`, etc. via `functools.wraps`.

## Installation

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/chetanaybuilder/Ai-Ml-Month-01-Python-and-Maths.git
cd Ai-Ml-Month-01-Python-and-Maths/Day-09-Smart-Function-Manager
```

Install dependencies (none required beyond the Python standard library):

```bash
pip install -r requirements.txt
```

## Usage

```python
from decorators.manager import monitor

@monitor
def add(a: int, b: int) -> int:
    return a + b

add(10, 20)
# Output:
# -------------------------------
# Function: add
# Call number: 1
# Positional arguments: (10, 20)
# Keyword arguments: {}
# Result: 30
# ----------------------------------
```

## Running the Demo

```bash
python main.py
```

## Requirements

*   Python 3.8+

No external packages are required; the project uses only the standard library
(`functools`, `typing`).

## License

MIT