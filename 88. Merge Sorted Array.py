"""
88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


def merge(nums1, m, nums2, n):
    i1, i2 = 0, 0
    while i1 < m and i2 < n:
        if nums1[i1] > nums2[i2]:
            nums1[i1:m + 1] = [nums2[i2]] + nums1[i1:m]
            i2, m = i2 + 1, m + 1
        i1 += 1
    while i2 < n:
        nums1[i1] = nums2[i2]
        i1, i2 = i1 + 1, i2 + 1
    return nums1


if '__main__' == __name__:
    assert merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert merge([1], 1, [], 0) == [1]
    assert merge([0], 0, [1], 1) == [1]
    print('All tests passed!')
