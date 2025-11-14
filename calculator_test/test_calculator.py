import pytest
from calculator import sum, substract, multiply, divide

def test_sum():
    assert sum(3, 5) == 8
    assert sum(-1, 1) == 0
    assert sum(-2, -3) == -5
    assert sum(0, 0) == 0