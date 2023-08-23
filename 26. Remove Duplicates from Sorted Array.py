"""
26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were
present in nums initially. The remaining elements of nums are not important as well as the size of nums.

Return k.
"""


def remove_duplicates(nums):
    dif = len(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = '_'
            dif -= 1
    nums.sort(key=lambda a: 1000 if a == '_' else a)
    return nums[:dif]


if '__main__' == __name__:
    assert remove_duplicates([1, 1, 2]) == [1, 2]
    assert remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == [0, 1, 2, 3]
    assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == [0, 1, 2, 3, 4]
    print('All tests passed!')
