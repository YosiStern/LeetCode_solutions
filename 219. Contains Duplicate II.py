"""
219. Contains Duplicate II
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    elements = {}
    for i in range(len(nums)):
        if nums[i] in elements:
            elements[nums[i]] += [i]
        else:
            elements[nums[i]] = [i]
    for num in elements:
        for i in range(len(elements[num]) - 1):
            if (elements[num][i + 1] - elements[num][i]) <= k:
                return True
    return False


if '__main__' == __name__:
    assert contains_nearby_duplicate([1,2,3,1], 3) == True
    assert contains_nearby_duplicate([1,0,1,1], 1) == True
    assert contains_nearby_duplicate([1,2,3,1,2,3], 2) == False
    print('All tests passed!')
