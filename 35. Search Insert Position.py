"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""


def search_insert(nums, target):
    i = 0
    for element in nums:
        if target <= element:
            return i
        i += 1
    return i


if '__main__' == __name__:
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    print('All tests passed!')
