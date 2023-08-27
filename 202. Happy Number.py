"""
202. Happy Number
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
 or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


def is_happy(n: int) -> bool:
    n = str(n)
    while len(n) != 1:
        number = 0
        for digit in n:
            number += int(digit) ** 2
        n = str(number)
    if n == '1' or n == '7':
        return True
    return False


if '__main__' == __name__:
    assert is_happy(19) == True
    assert is_happy(2) == False
    print('All tests passed!')
