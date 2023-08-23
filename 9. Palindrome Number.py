"""
9. Palindrome Number
Given an integer x, return true if x is a
palindrome
, and false otherwise.
"""


def is_palindrome(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[-i - 1]:
            return False
    return True


if '__main__' == __name__:
    assert is_palindrome(121) == True
    assert is_palindrome(-121) == False
    assert is_palindrome(10) == False
    print('All tests passed!')
