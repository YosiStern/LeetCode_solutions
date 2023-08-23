"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""


def remove_element(nums, val):
    length = len(nums)
    i, k, = 0, 0
    while k + i < length:
        if nums[i] == val:
            nums[i] = nums[length - k - 1]
            k += 1
        else:
            i += 1
    return nums[:i]


if '__main__' == __name__:
    assert remove_element([3,2,2,3], 3) == [2, 2]
    assert remove_element([0,1,2,2,3,0,4,2], 2) == [0,1,4,0,3]
    print('All tests passed!')
