"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


def is_anagram(s: str, t: str) -> bool:
    d = {}
    for letter in s:
        if letter in d:
            d[letter] = d[letter] + 1
        else:
            d[letter] = 1
    for letter in t:
        if letter in d:
            d[letter] = d[letter] - 1
        else:
            return False
    for val in d.values():
        if val != 0:
            return False
    return True


if '__main__' == __name__:
    assert is_anagram("anagram", "nagaram")
    assert not is_anagram("rat", "car")
    print('All tests passed!')
