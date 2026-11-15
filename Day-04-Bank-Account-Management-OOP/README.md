![AI/ML Month 1: Python and Core Mathematics](../assets/readme-banner.png)

# Bank Account Management with OOP

A runnable Python example of encapsulating account data and basic transactions in a class.

## Overview

`main.py` defines `BankAccount` and runs a short demonstration. The class stores an account holder's name and balance, supports deposits and withdrawals, and implements selected Python special methods.

## Purpose

The example focuses on object-oriented design and validation around simple state-changing operations. It is an in-memory programming exercise, not a banking system.

## Features

- Creates an account with a non-negative initial balance.
- Supports positive deposits and withdrawals that do not exceed the balance.
- Provides readable and debugging representations of account objects.
- Compares accounts by holder name and exposes the name length through `len()`.
- Demonstrates transactions with two sample account instances.

## Core Concepts

- Class and instance state.
- Encapsulation of operations and validation in instance methods.
- Special methods: `__str__`, `__repr__`, `__eq__`, and `__len__`.
- Exceptions for invalid balances and transactions.
- A guarded command-line entry point.

## Technology Stack

- Python 3.6 or later
- Python standard library only; no third-party packages

## Project Structure

```text
Day-04-Bank-Account-Management-OOP/
├── main.py
└── README.md
```

## Installation and Setup

Install Python 3.6 or later. No package installation or virtual environment is required.

## How to Run

From this project directory:

```console
python main.py
```

On Windows, `py main.py` also works when the Python launcher is installed.

## Usage

The script runs a fixed demonstration. The class can also be imported from another Python file:

```python
from main import BankAccount

account = BankAccount("Alex", 5000.0)
account.deposit(250.0)
account.withdraw(100.0)
print(account)
```

## Sample Output

The demonstration initializes Alex's balance at `$5,000.00`, deposits `$500.00`, and withdraws `$200.00`. The resulting balance is `$5,300.00`.

## Implementation Notes

`__eq__` defines equality using only the account holder's name, while `__len__` returns the number of characters in that name. Balances are held as Python numeric values and formatted as USD for display.

## Error Handling and Limitations

The constructor rejects a negative initial balance. `deposit()` and `withdraw()` reject non-positive amounts, and `withdraw()` also rejects an amount greater than the current balance; these conditions raise `ValueError`. Account state is held only in memory. The example uses floating-point balances and does not model real financial requirements.

## Testing

No automated test files are included in this project.

## Learning Outcomes

- Group related data and behavior in a class.
- Use special methods to integrate objects with Python's built-in operations.
- Define validation rules at the operations that modify state.

## Future Improvements

- Add unit tests for valid transactions and each validation failure.
- Use `decimal.Decimal` for monetary arithmetic.
- Separate the reusable class from the demonstration entry point.

## Project Information

Part of the AI/ML Month 1 Python and Core Mathematics learning series.

Author: [chetanaybuilder](https://github.com/chetanaybuilder)
