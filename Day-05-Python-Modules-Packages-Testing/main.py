"""Command-line interface for the calculator package."""

from calculator.addition import addition
from calculator.division import division
from calculator.multiplication import multiplication
from calculator.subtraction import subtraction

OPERATIONS = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


def run_calculator():
    """Run the interactive calculator until the user chooses to quit."""
    while True:
        operation = input("Enter operation (+, -, *, /) or q to quit: ").strip()
        if operation.lower() == "q":
            break
        if operation not in OPERATIONS:
            print("Error: Invalid operation. Please choose +, -, *, or /.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = OPERATIONS[operation](num1, num2)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        else:
            print(f"{num1} {operation} {num2} = {result}")


if __name__ == "__main__":
    run_calculator()
