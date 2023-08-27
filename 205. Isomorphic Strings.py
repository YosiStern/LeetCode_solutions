"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""


def is_isomorphic(s: str, t: str) -> bool:
    list_of = zip(s, t)
    dic_translate, used_value = {}, []
    for s_char, t_char in list_of:
        if dic_translate.get(s_char) is None and t_char not in used_value:
            dic_translate[s_char] = t_char
            used_value += [t_char]
        elif t_char != dic_translate.get(s_char):
            return False
    list_of = zip(s, t)
    for s_char, t_char in list_of:
        if t_char != dic_translate[s_char]:
            return False
    return True


if '__main__' == __name__:
    assert is_isomorphic("egg", "add")
    assert not is_isomorphic("foo", "bar")
    assert is_isomorphic("paper", "title")
    print('All tests passed!')
