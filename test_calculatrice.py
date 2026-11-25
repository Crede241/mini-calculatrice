import pytest

from calculatrice import addition, division, multiplication

def test_addition():
    assert addition(2, 3) == 5


def test_division():
    assert division(10, 2) == 5


def test_division_par_zero():
    with pytest.raises(ValueError):
        division(1, 0)


def test_multiplication():
    assert multiplication(3, 4) == 12