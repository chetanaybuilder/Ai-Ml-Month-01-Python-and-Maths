"""Demo of the monitor decorator on sample functions."""

from decorators.manager import monitor


@monitor
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


@monitor
def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


@monitor
def greet(name: str, age: int) -> str:
    """Return a personalized greeting string."""
    return f"hello {name}, age {age}"


def main() -> None:
    """Run demonstration calls for each decorated function."""
    print("=====Smart Function Manager======")
    add(10, 20)
    add(50, 60)
    multiply(5, 4)
    greet(name="alex", age=16)


if __name__ == "__main__":
    main()
