import pytest
from cviceni4_data import get_avg
from unittest.mock import patch, MagicMock

@pytest.mark.skip
@pytest.mark.parametrize("number, result", [(1, 1), (2, 1.5), (3, 2), (4, 2.5), (5, 3), (6, 3.5), (7, 4),(8,4.5),(9,5)])
def test_get_avg(number, result):
    assert get_avg(number) == result


def test_get_avg_mock():
    magic_mock = MagicMock(return_value = "1")
    with patch("cviceni4_data._get_data", magic_mock):
        assert get_avg(1) == 1