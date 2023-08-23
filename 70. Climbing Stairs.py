"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
import math


def climb_stairs(n):
    sum_comb, k = 0, 0
    while 2*k <= n*2:
        sum_comb += math.comb(n-k, k)
        k += 1
    return sum_comb


if '__main__' == __name__:
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(27) == 317811
    print('All tests passed!')
