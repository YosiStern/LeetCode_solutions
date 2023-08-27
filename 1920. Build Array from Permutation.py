"""
1920. Build Array from Permutation
Given a zero-based permutation nums (0-indexed),
build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
"""


def build_array(nums: list[int]) -> list[int]:
        i, ans = 0, nums[:]
        lenght = len(nums)
        while i < lenght:
            ans[i] = nums[nums[i]]
            i += 1
        return ans


if '__main__' == __name__:
    assert build_array([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]
    assert build_array([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]
    print('All tests passed!')
