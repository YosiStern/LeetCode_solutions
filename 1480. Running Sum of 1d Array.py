"""
1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""


def running_sum(nums: list[int]) -> list[int]:
    sum_num, ret_list = 0, []
    for num in nums:
        sum_num += num
        ret_list.append(sum_num)
    return ret_list


if '__main__' == __name__:
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    print('All tests passed!')
