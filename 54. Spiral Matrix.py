"""
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
"""


def spiral_order(matrix):
    max_row, min_row, max_col, min_col, row, col, mask = len(matrix[0]), 0, len(matrix), 0, 0, 0, (0, 1)
    status, ans, p = 0, [], max_row * max_col
    while p > 0:
        p -= 1
        ans += [matrix[row][col]]
        row, col = row + mask[0], col + mask[1]
        if col >= max_row and status == 0:
            col -= 1
            row += 1
            mask = (1, 0)
            max_row -= 1
            status = 1
        elif row >= max_col and status == 1:
            row -= 1
            col -= 1
            mask = (0, -1)
            max_col -= 1
            status = 0
        elif col < min_row and status == 0:
            col += 1
            row -= 1
            mask = (-1, 0)
            min_row += 1
            status = 1
        elif row <= min_col and status == 1:
            row += 1
            col += 1
            mask = (0, 1)
            min_col += 1
            status = 0
    return ans


if '__main__' == __name__:
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    print('All tests passed!')