"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""


def length_of_last_word(s: str) -> int:
    word, i = False, 0
    for char in s[::-1]:
        if ' ' != char:
            word = True
        if word:
            if char == ' ':
                return i
            else:
                i += 1
    return i


if '__main__' == __name__:
    assert length_of_last_word("Hello World") == 5
    assert length_of_last_word("   fly me   to   the moon  ") == 4
    assert length_of_last_word("luffy is still joyboy") == 6
    print('All tests passed!')
