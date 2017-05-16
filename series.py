"""
Math Series: Fibonacci and Lucas Numbers
"""


def fibonacci(num):
    """
    returns the nth number in the Fibonacci sequence
    """
    if num == 0 or num == 1:
        return 0
    if num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
    return ""


def lucas(num=5):
    """
    returns the nth number in the Lucas series
    """
    # do stuff
    return ""


if __name__ == '__main__':
    lucas()
    fibonacci()
