<div align="center">

# Bank Account Management with OOP

> A compact, dependency-free Python demonstration of object-oriented programming and basic account transactions.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=flat-square&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-success?style=flat-square)
![Project](https://img.shields.io/badge/AI%20%26%20ML%20Month%2001-Day%2004-purple?style=flat-square)

</div>

---

## Overview

This project models a bank account with a holder name and balance. It demonstrates Python classes, instance methods, special methods, input validation, and a formatted command-line report.

The program creates two sample accounts, compares their holders, displays the holder-name length, and demonstrates a deposit followed by a withdrawal.

## Features

- Groups account data and transaction behavior in the `BankAccount` class.
- Formats account details and balances for readable terminal output.
- Implements `__str__`, `__repr__`, `__eq__`, and `__len__`.
- Rejects non-positive transactions and withdrawals that exceed available funds.
- Uses only the Python standard library.

## Project Structure

```text
Day-04-Bank-Account-Management-OOP/
├── main.py      # BankAccount implementation and runnable demo
└── README.md    # Project documentation
```

## Requirements

- Python 3.6 or newer
- No third-party packages

## Run

Open a terminal in this directory and run:

```bash
python main.py
```

On Windows, the Python launcher can also be used:

```powershell
py main.py
```

## Example Output

```text
=============== BANK ACCOUNT DEMO ================

ACCOUNTS
  Account holder: Alex, Balance: $5,000.00
  Account holder: Sam, Balance: $3,000.00

ACCOUNT DETAILS
  Same account holder: No
  Name length: 4 characters

TRANSACTION SUMMARY
  Deposit: +$500.00
  Withdrawal: -$200.00
  Updated: Account holder: Alex, Balance: $5,300.00
```

## Use the Class

```python
from main import BankAccount

account = BankAccount("Alex", 5000.0)
account.deposit(250.0)
account.withdraw(100.0)

print(account)
```

`deposit()` and `withdraw()` raise `ValueError` for invalid amounts; withdrawals also raise it when funds are insufficient.

## Learning Notes

This is an educational example, not a production banking system. Balances are stored as floating-point numbers, and the sample data is held in memory only. A real financial application would require precise decimal arithmetic, persistence, authentication, audit trails, and additional security and regulatory controls.
