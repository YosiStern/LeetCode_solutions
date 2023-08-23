"""
283. Move Zeroes
Given an integer array nums,
move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


def move_zeroes(nums):
    start_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[start_zero], nums[i] = nums[i], nums[start_zero]
            start_zero += 1
    return nums


if '__main__' == __name__:
    assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]
    assert move_zeroes([0]) == [0]
    print('All tests passed!')
