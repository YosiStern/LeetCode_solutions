"""
169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""


def majority_element(nums):
    majority = len(nums) / 2
    exist = dict()
    for element in nums:
        if element in exist:
            exist[element] = exist[element] + 1
        else:
            exist[element] = 1
        if exist[element] > majority:
            return element


if '__main__' == __name__:
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    print('All tests passed!')
