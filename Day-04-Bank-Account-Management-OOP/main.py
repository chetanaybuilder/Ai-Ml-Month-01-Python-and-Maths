"""Bank Account Management Module.

Demonstrates object-oriented encapsulation, Python dunder methods,
input validation, and formatted terminal output.
"""


class BankAccount:
    """Represents an individual bank account with basic transaction operations.

    Attributes:
        name: Full name of the account holder.
        balance: Current available funds in USD.
    """

    def __init__(self, name: str, balance: float = 0.0) -> None:
        """Initializes a BankAccount instance after validating initial funds."""
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.name = name
        self.balance = balance

    def __str__(self) -> str:
        """Returns a formatted, human-readable account summary."""
        return f"Account holder: {self.name}, Balance: ${self.balance:,.2f}"

    def __repr__(self) -> str:
        """Returns an unambiguous representation for debugging."""
        return f"BankAccount(name={self.name!r}, balance={self.balance!r})"

    def __eq__(self, other: object) -> bool:
        """Checks equality based on account holder name."""
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.name == other.name

    def __len__(self) -> int:
        """Returns the character length of the account holder's name."""
        return len(self.name)

    def deposit(self, amount: float) -> None:
        """Credits a positive amount to the account balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Debits a valid amount from the account balance if funds permit."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


def main() -> None:
    """Runs a terminal demonstration of BankAccount operations."""
    # ANSI styling constants for terminal output
    bold, cyan, reset = "\033[1m", "\033[36m", "\033[0m"

    # Initialize sample accounts
    primary_account = BankAccount("Alex", 5000.0)
    secondary_account = BankAccount("Sam", 3000.0)

    # Display initial state
    print(f"\n{bold}{cyan}{' BANK ACCOUNT DEMO ':=^50}{reset}")
    print(f"\n{bold}ACCOUNTS{reset}")
    print(f"  {primary_account}")
    print(f"  {secondary_account}")

    # Inspect account metadata and equality
    is_same_holder = "Yes" if primary_account == secondary_account else "No"
    print(f"\n{bold}ACCOUNT DETAILS{reset}")
    print(f"  Same account holder: {is_same_holder}")
    print(f"  Name length: {len(primary_account)} characters")

    # Execute transactions
    primary_account.deposit(500.0)
    primary_account.withdraw(200.0)

    # Display updated balance
    print(f"\n{bold}TRANSACTION SUMMARY{reset}")
    print("  Deposit: +$500.00")
    print("  Withdrawal: -$200.00")
    print(f"  Updated: {primary_account}\n")


if __name__ == "__main__":
    main()