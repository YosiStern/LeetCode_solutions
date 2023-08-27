"""
11. Container With Most Water
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""


def max_area(height):
    i, j, contain = 0, len(height)-1, 0
    while i < j:
        if contain < min(height[i], height[j])*(j-i):
            contain = min(height[i], height[j])*(j-i)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return contain


if '__main__' == __name__:
    assert max_area([1, 1]) == 1
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    print('All tests passed!')
