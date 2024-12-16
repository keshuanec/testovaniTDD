import pytest
from p01_BasicCalculator import BasicCalculator

def test_addition():
    basic_calculator = BasicCalculator()
    result = basic_calculator.add(3,5)
    assert result == 8
    assert basic_calculator.add(5,5) == 10

def test_multiply():
    basic_calculator = BasicCalculator()
    assert basic_calculator.multiply(5,3) == 15

