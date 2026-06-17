import pytest

from calculator_service import add, divide, multiply, subtract


def test_adds_two_numbers():
    assert add(2, 3) == 5


def test_subtracts_two_numbers():
    assert subtract(10, 4) == 6


def test_multiplies_two_numbers():
    assert multiply(6, 7) == 42


def test_divides_two_numbers():
    assert divide(9, 3) == 3


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
