"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.
"""


def containsDuplicate(nums):
    exist = set()
    for num in nums:
        if num in exist:
            return True
        else:
            exist.add(num)
    return False


if '__main__' == __name__:
    assert containsDuplicate([1, 2, 3, 1]) == True
    assert containsDuplicate([1, 2, 3, 4]) == False
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    print('All tests passed!')
