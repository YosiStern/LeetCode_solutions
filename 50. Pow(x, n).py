"""
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


def my_pow(x: float, n: int) -> float:
    return x ** n


if '__main__' == __name__:
    assert my_pow(2, 10) == 1024
    assert my_pow(2.1, 3) == 9.261000000000001
    assert my_pow(2, -2) == 0.25000
    print('All tests passed!')
