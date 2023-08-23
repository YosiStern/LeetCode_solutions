"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest
substring
 without repeating characters.
"""


def lengthOfLongestSubstring(s: str) -> int:
    max_len, end, len_s = 0, 0, len(s)
    for i in range(len_s):
        sub_s = s[i]
        while end + 1 < len_s:
            end += 1
            if s[end] in s[i:end]:
                end -= 1
                break
        end += 1
        if len(s[i:end]) > max_len:
            max_len = len(s[i:end])
        end = i
    return max_len


if '__main__' == __name__:
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    print('All tests passed!')
