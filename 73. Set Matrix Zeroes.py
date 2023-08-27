"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
"""


def set_zeroes(matrix):
    n, m = len(matrix), len(matrix[0])
    rows, cols = set(), set()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in rows:
        for j in range(m):
            matrix[i][j] = 0
    for i in range(n):
        for j in cols:
            matrix[i][j] = 0
    return matrix


if '__main__' == __name__:
    assert set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert set_zeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    print('All tests passed!')
