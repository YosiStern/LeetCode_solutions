"""
228. Summary Ranges
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
"""


def add_to_ans(start, end):
    if end == start:
        return [str(end)]
    return [f"{start}->{end}"]


def summary_ranges(nums: list[int]) -> list[str]:
    n, i = len(nums), 1
    if n == 0:
        return []
    start = end = nums[0]
    ans = []
    while i < n:
        if nums[i] == end + 1:
            end = nums[i]
        else:
            ans += add_to_ans(start, end)
            if i < n:
                end = start = nums[i]
        i += 1
    ans += add_to_ans(start, end)
    return ans


if '__main__' == __name__:
    assert summary_ranges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert summary_ranges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    print('All tests passed!')
