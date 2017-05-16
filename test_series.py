"""
Tests for the fibonacci sequence
"""
import pytest

params_table = [
    (0, 0), (1, 0), (2, 1), (3, 1), (8, 13)
]


@pytest.mark.parametrize("n, result", params_table)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result
