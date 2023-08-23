"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


def roman_to_int(s):
    dic_roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

    len1 = len(s)
    i, num, reduce = 1, 0, 0
    for char in s:
        if i < len1 and dic_roman[char] < dic_roman[s[i]]:
            reduce = dic_roman[char]
        else:
            num += dic_roman[char] - reduce
            reduce = 0
        i += 1
    return num


if '__main__' == __name__:
    assert roman_to_int("III") == 3
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
    print('All tests passed!')
