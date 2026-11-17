"""Reusable decorator that logs each call to a wrapped function."""

from functools import wraps
from typing import Any, Callable


def monitor(func: Callable[..., Any]) -> Callable[..., Any]:
    """Monitor and log invocations of the decorated function."""
    count: int = 0

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Increment per-function call counter.
        nonlocal count
        count += 1

        # Log invocation details before executing the function.
        print("\n-------------------------------")
        print(f"Function: {func.__name__}")
        print(f"Call number: {count}")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")

        # Execute the wrapped function and capture its result.
        result: Any = func(*args, **kwargs)

        # Log the result after execution.
        print(f"Result: {result}")
        print("----------------------------------")

        # Return the result so the decorator stays transparent.
        return result

    return wrapper

