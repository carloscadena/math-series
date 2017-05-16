"""
Tests for the fibonacci sequence
"""
import pytest

params_table = [
    (0, 0), (1, 0), (2, 1), (3, 1), (8, 13)
]

lucas_params_table = [
    (0, 2), (1, 2), (2, 1), (3, 3), (4, 4), (5, 7), (6, 11),
]


@pytest.mark.parametrize("n, result", params_table)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize("n, result", lucas_params_table)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result
