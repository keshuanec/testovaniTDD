import pytest

from p01_BasicCalculator import BasicCalculator


parametres = [(5,5,10), ("5",5,None), (-3,-7,-10)]

@pytest.mark.parametrize("num1, num2, result", parametres)
def test_add(num1,num2,result):
    calc = BasicCalculator()
    assert calc.add(num1,num2) == result