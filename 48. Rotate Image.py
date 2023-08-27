"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""


def rotate(matrix: list[list[int]]) -> list[list[int]]:
    length = len(matrix)
    for i_row in range(length):
        for i_col in range(0, length):
            matrix[i_row] += [matrix[i_col][i_row]]
    for i_row in range(length):
        matrix[i_row] = matrix[i_row][:length - 1:-1]
    return matrix


if '__main__' == __name__:
    assert rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])\
           == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    print('All tests passed!')
