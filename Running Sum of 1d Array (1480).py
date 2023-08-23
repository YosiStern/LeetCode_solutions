def runningSum(nums):
    sum_num, ret_list = 0, []
    for num in nums:
        sum_num += num
        ret_list.append(sum_num)
    return ret_list


if '__main__' == __name__:
    assert runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    print('All tests passed!')
