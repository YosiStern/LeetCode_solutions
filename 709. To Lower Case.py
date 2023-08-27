"""
709. To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
"""


def to_lower_case(s: str) -> str:
    return s.lower()


if '__main__' == __name__:
    assert to_lower_case("Hello") == "hello"
    assert to_lower_case("here") == "here"
    assert to_lower_case("LOVELY") == "lovely"
    print('All tests passed!')

