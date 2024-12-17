from cviceni2_data import odd_indexes
from p03_BasicCalculator_test_parametrize import parametres
import pytest

def test_odd_indexes():
    assert odd_indexes("elephant") == "lpat"
    assert odd_indexes("computer") == "optr"
    assert odd_indexes("auto") == "uo"
    assert odd_indexes("bagr") == "ar"
    assert odd_indexes("") == ""
    assert odd_indexes("a") == ""
    assert odd_indexes(123) == "2"
    assert odd_indexes(123456789) == "2468"
    assert odd_indexes(-5) == "5"

stringy = [("elephant","lpat"),("computer","optr"),("auto","uo"),("bagr","ar"),("",""),("a",""),(123,"2"),(123456789,"2468"),(-5,"5")]
@pytest.mark.parametrize("string, result", stringy)
def test_odd_indexes_para(string,result):
    assert odd_indexes(string) == result

