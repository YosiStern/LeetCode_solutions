"""
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.
"""


def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


if '__main__' == __name__:
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"

    print('All tests passed!')
