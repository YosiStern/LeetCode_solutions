"""
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


def str_str(haystack: str, needle: str) -> int:
    return haystack.find(needle)


if '__main__' == __name__:
    assert str_str("sadbutsad", "sad") == 0
    assert str_str("leetcode", "leeto") == -1
    print('All tests passed!')
