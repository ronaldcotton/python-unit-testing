# test_calculator.py
# from https://github.com/python-frederick/python-testing-101/blob/master/test_calculator.py
# youtube: https://www.youtube.com/watch?v=etosV2IWBF0

import pytest

from calculator import Calculator, CalculatorError


def test_add():
    calculator = Calculator()

    result = calculator.add(2, 3)

    assert result == 5


def test_add_weird_stuff():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.add("two", 3)


def test_add_weirder_stuff():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.add("two", "three")


def test_subtract():
    calculator = Calculator()

    result = calculator.subtract(9, 3)

    assert result == 6


def test_multiply():
    calculator = Calculator()

    result = calculator.multiply(9, 3)

    assert result == 27


def test_divide():
    calculator = Calculator()

    result = calculator.divide(9, 3)

    assert result == 3


def test_divide_by_zero():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.divide(9, 0)