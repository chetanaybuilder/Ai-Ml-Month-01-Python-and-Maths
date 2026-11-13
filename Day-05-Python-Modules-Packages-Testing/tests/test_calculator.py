"""Unit tests for the calculator's arithmetic operations."""

import pytest

from calculator.addition import addition
from calculator.division import division
from calculator.multiplication import multiplication
from calculator.subtraction import subtraction


@pytest.mark.parametrize(
    ("operation", "left", "right", "expected"),
    [
        (addition, 20, 10, 30),
        (subtraction, 20, 10, 10),
        (multiplication, 20, 10, 200),
        (division, 20, 10, 2),
    ],
)
def test_arithmetic_operations(operation, left, right, expected):
    """Each operation returns the expected result for representative inputs."""
    assert operation(left, right) == expected


def test_division_by_zero_raises_error():
    """Division by zero is reported to callers as a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        division(20, 0)
