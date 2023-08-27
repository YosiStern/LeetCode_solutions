"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def bracket_fits(open_b, close_b):
    if (open_b == "(" and close_b == ')') or (open_b == "[" and close_b == ']') or (open_b == "{" and close_b == '}'):
        return True
    return False


def is_valid(s: str) -> bool:
    check_list = []
    bracket_opens = ("(", "[", "{")
    bracket_close = (")", "}", "]")
    for bracket in s:
        if bracket in bracket_opens:
            check_list.append(bracket)
        elif bracket in bracket_close:
            if len(check_list) == 0 or not bracket_fits(check_list.pop(), bracket):
                return False
        else:
            return False
    if len(check_list) == 0:
        return True
    return False


if '__main__' == __name__:
    assert is_valid("()")
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    print('All tests passed!')

