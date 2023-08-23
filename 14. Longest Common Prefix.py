"""
14. Longest Common Prefix
"""


def longest_common_prefix(strs):
    longest_prefix = strs[0]
    stop = len(strs[0])
    for check_str in strs:
        i = 0
        for letter in check_str:
            if stop == i or letter != longest_prefix[i]:
                longest_prefix = check_str[0:i]
                stop = i
                break
            i += 1
        if stop > i:
            longest_prefix = check_str[0:i]
            stop = i
    return longest_prefix


if '__main__' == __name__:
    assert longest_common_prefix(["flower","flow","flight"]) == "fl"
    assert longest_common_prefix(["dog","racecar","car"]) == ""
    print('All tests passed!')
