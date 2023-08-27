"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""


def permute(nums: list[int]) -> list[list[int]]:
    ret = []
    length = len(nums)
    for i1 in range(0, length):
        if length == 1:
            ret += [[nums[i1]]]
        for i2 in range(0, length):
            if i2 == i1:
                continue
            if length == 2:
                ret += [[nums[i1], nums[i2]]]
            for i3 in range(0, length):
                if i3 in [i2, i1]:
                    continue
                if length == 3:
                    ret += [[nums[i1], nums[i2], nums[i3]]]
                for i4 in range(0, length):
                    if i4 in [i3, i2, i1]:
                        continue
                    if length == 4:
                        ret += [[nums[i1], nums[i2], nums[i3], nums[i4]]]
                    for i5 in range(0, length):
                        if i5 in [i4, i3, i2, i1]:
                            continue
                        if length == 5:
                            ret += [[nums[i1], nums[i2], nums[i3], nums[i4], nums[i5]]]
                        for i6 in range(0, length):
                            if i6 in [i5, i4, i3, i2, i1]:
                                continue
                            if length == 6:
                                ret += [[nums[i1], nums[i2], nums[i3], nums[i4], nums[i5], nums[i6]]]
    return ret


if '__main__' == __name__:
    assert permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert permute([0, 1]) == [[0, 1], [1, 0]]
    assert permute([1]) == [[1]]
    print('All tests passed!')
