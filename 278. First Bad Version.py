"""
278. First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately,
the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""
from math import ceil

FIRST_BAD = 4


def is_bad_version(version: int) -> bool:
    first_bad = FIRST_BAD
    return version >= first_bad


def first_bad_version(n: int) -> int:
    low, high = 1, n
    while low < high:
        i = ceil((high - low) / 2)
        if is_bad_version(low + i):
            high = high - i
        else:
            low = low + i + 1
    if not is_bad_version(high):
        return high + 1
    return high


if '__main__' == __name__:
    FIRST_BAD = 1
    assert first_bad_version(1) == 1
    FIRST_BAD = 2
    assert first_bad_version(2) == 2
    FIRST_BAD = 4
    assert first_bad_version(5) == 4
    print('All tests passed!')
