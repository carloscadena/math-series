"""
Math Series: Fibonacci and Lucas Numbers
"""


def fibonacci(num):
    """
    returns the nth number in the Fibonacci sequence
    """
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


def lucas(num):
    """
    returns the nth number in the Lucas series
    """
    if num == 1:
        return 2
    if num == 2:
        return 1
    return lucas(num - 1) + lucas(num - 2)


def sum_series(n_th_element, a=0, b=1):
    """
    return the nth number of the series starting with value in a and b
    """
    if a == 0 and b == 1:
        return fibonacci(n_th_element)
    if a == 2 and b == 1:
        return lucas(n_th_element)
    if n_th_element == 1:
        return a
    if n_th_element == 2:
        return b

    return sum_series(n_th_element-2, a, b) + sum_series(n_th_element-1, a, b)


if __name__ == '__main__':
    lucas()
    fibonacci()
    sum_series()
