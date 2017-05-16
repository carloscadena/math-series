"""
Tests for the fibonacci sequence
"""
import pytest

params_table = [
    (1, 0), (2, 1), (3, 1), (8, 13)
]

lucas_params_table = [
    (1, 2), (2, 1), (3, 3), (4, 4), (5, 7), (6, 11),
]

sum_series_table = [
    (5, 3, 2, 12), (7, 5, 10, 105)
]


@pytest.mark.parametrize("n, result", params_table)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize("n, result", lucas_params_table)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize("n, a, b, result", sum_series_table)
def test_sum_series(n, a, b, result):
    from series import sum_series
    assert sum_series(n, a, b) == result
