"""
55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""


def can_jump(nums):
    ok = 0
    for i in reversed(nums):
        ok = 1 if i >= ok else ok + 1
    if ok > 1:
        return False
    return True


if '__main__' == __name__:
    assert can_jump([2, 3, 1, 1, 4]) == True
    assert can_jump([3, 2, 1, 0, 4]) == False
    print('All tests passed!')
