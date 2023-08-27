"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""


def longest_palindrome(s: str) -> int:
    dual, single = 0, 0
    s_iter = iter(sorted(s))
    val = next(s_iter, 1)
    while val != 1:
        next_val = next(s_iter, 1)
        if next_val == val:
            dual += 1
            val = next(s_iter, 1)
        else:
            single = 1
            val = next_val
    return dual * 2 + single


if '__main__' == __name__:
    assert longest_palindrome("abccccdd") == 7
    assert longest_palindrome("a") == 1
    print('All tests passed!')
