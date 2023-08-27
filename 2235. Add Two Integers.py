"""
2235. Add Two Integers

Given two integers num1 and num2, return the sum of the two integers.
"""


def sum(self, num1, num2):
    return num1 + num2


if '__main__' == __name__:
    assert sum(12, 5) == 17
    assert sum(-10, 4) == -6
    print('All tests passed!')
