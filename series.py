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


if __name__ == '__main__':
    lucas()
    fibonacci()
