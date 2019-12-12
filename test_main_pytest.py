from main import cal_addition
import pytest

@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (3, 5, 8), (5, 8, 13), (10, 10, 20), (20, 20, 40)])
def test_addition(a, b, expected):
    assert cal_addition(a, b) == expected
