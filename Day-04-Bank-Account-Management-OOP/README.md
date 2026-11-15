<p align="center">
  <img src="../assets/readme-banner.png" alt="AI/ML Month 1 — Python and Core Mathematics" width="90%">
</p>

<h1 align="center">Bank Account Management with OOP</h1>

<p align="center">
  A small in-memory model demonstrating class design, transaction validation, and Python special methods.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.6 or later">
  <img src="https://img.shields.io/badge/Design-Object--Oriented-4F46E5?style=flat-square" alt="Object-oriented design">
  <img src="https://img.shields.io/badge/Month%2001-Day%2004-6D5BD0?style=flat-square" alt="Month 01, Day 04">
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#what-i-learned">Learning</a> ·
  <a href="#setup-and-run">Run</a> ·
  <a href="#engineering-takeaways">Takeaways</a>
</p>

---

## Overview

[`main.py`](main.py) defines a `BankAccount` class with a holder name and balance, then runs a fixed demonstration with two sample accounts. The project is an educational example; it does not persist accounts or implement real banking controls.

## What I Learned

### Learning Progress

**Day 04 — Object-Oriented Programming**

This project applies classes and instance state to a concrete domain example. It also explores how special methods connect custom objects to Python's built-in operations and representations.

### What I Built

I implemented the `BankAccount` class with:

- An initializer that rejects negative opening balances.
- `deposit()` and `withdraw()` methods with transaction validation.
- `__str__` and `__repr__` for display and debugging.
- `__eq__` to compare account-holder names and `__len__` to return the holder-name length.

The entry point demonstrates a deposit followed by a withdrawal and prints the updated balance.

### Engineering Takeaways

1. Put state-changing rules close to the state they protect.
2. Special methods should have clear, documented semantics; here equality means same holder name, not identical account state.
3. Raise a specific exception when an operation violates an invariant.
4. Use this example as a learning model, not as a financial implementation.

## Features

| Method or behavior | Contract |
|---|---|
| `BankAccount(name, balance)` | Rejects an initial balance below zero |
| `deposit(amount)` | Requires a positive amount |
| `withdraw(amount)` | Requires a positive amount no greater than the balance |
| `str(account)` | Displays the holder and formatted balance |
| `account_a == account_b` | Compares holder names |
| `len(account)` | Returns the number of characters in the holder name |

## Object Model

```mermaid
classDiagram
    class BankAccount {
        +name: str
        +balance: float
        +deposit(amount)
        +withdraw(amount)
        +__str__()
        +__repr__()
        +__eq__(other)
        +__len__()
    }
    BankAccount : validates opening balance
    BankAccount : rejects invalid transactions
```

## Project Structure

```text
Day-04-Bank-Account-Management-OOP/
├── main.py
└── README.md
```

## Setup and Run

Requirements: Python 3.6 or later. No package installation is required.

```console
python main.py
```

Run the command from this project directory. On Windows, `py main.py` also works if the Python launcher is installed.

## Reuse the Class

```python
from main import BankAccount

account = BankAccount("Alex", 5000.0)
account.deposit(250.0)
account.withdraw(100.0)
print(account)
```

## Verified Demonstration

The fixed example starts Alex at `$5,000.00`, deposits `$500.00`, and withdraws `$200.00`. The displayed final balance is `$5,300.00`.

## Error Handling and Limitations

Invalid opening balances and transaction amounts raise `ValueError`; withdrawing more than the current balance also raises `ValueError`. Balances are stored in memory as floating-point numbers, which are not a suitable default for precise financial arithmetic. There is no persistence, authentication, transaction history, or concurrency handling.

## Testing

No automated test files are included in this project.

## Future Improvements

- Add unit tests for normal transactions and every validation condition.
- Use `decimal.Decimal` for monetary values.
- Separate the reusable class from the demonstration in `main.py`.

## Project Information

Part of the **AI/ML Month 1 — Python and Core Mathematics** learning series.

Author: [chetanaybuilder](https://github.com/chetanaybuilder)
