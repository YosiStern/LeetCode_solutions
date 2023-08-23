"""
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
 of the characters without disturbing the relative positions of the remaining characters. (i.e.,
 "ace" is a subsequence of "abcde" while "aec" is not).
"""


def is_subsequence(s: str, t: str) -> bool:
    len_s = len(s)
    len_t = len(t)
    i, j = 0, 0
    while j < len_t and i < len_s:
        if s[i] == t[j]:
            i += 1
        j += 1
    if i == len_s:
        return True
    return False


if '__main__' == __name__:
    assert is_subsequence("abc", "ahbgdc") == True
    assert is_subsequence("axc", "ahbgdc") == False
    print('All tests passed!')
