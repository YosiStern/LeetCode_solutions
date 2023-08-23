"""
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""


def rotate(nums, k) -> None:
    length = len(nums) - k
    if length < 0:
        length = len(nums) - k % len(nums)
    nums[:] = nums[length:] + nums[:length]
    return nums


if '__main__' == __name__:
    assert rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    print('All tests passed!')
