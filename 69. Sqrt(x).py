"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


def my_sqrt(x: int) -> int:
    p, n = 1, x / 2
    while p != n:
        p = n
        d = x / (n if n > 0 else 1)
        n = (n + d) / 2
    return int(p)


if '__main__' == __name__:
    assert my_sqrt(4) == 2
    assert my_sqrt(8) == 2
    print('All tests passed!')
