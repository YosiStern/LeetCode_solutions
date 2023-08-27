"""
36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""


def is_valid_sudoku(board):
    dic_row, dic_col, dic_square = {}, {}, {}
    for i_row in range(len(board)):
        for i_col in range(len(board[i_row])):
            if board[i_row][i_col] == '.':
                continue
            i_square = i_row // 3, i_col // 3
            if i_row in dic_row:
                if board[i_row][i_col] in dic_row[i_row]:
                    return False
                dic_row[i_row] += board[i_row][i_col]
            else:
                dic_row[i_row] = board[i_row][i_col]
            if i_col in dic_col:
                if board[i_row][i_col] in dic_col[i_col]:
                    return False
                dic_col[i_col] += board[i_row][i_col]
            else:
                dic_col[i_col] = board[i_row][i_col]
            if i_square in dic_square:
                if board[i_row][i_col] in dic_square[i_square]:
                    return False
                dic_square[i_square] += board[i_row][i_col]
            else:
                dic_square[i_square] = board[i_row][i_col]
    return True


if '__main__' == __name__:
    assert is_valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                            [".", "9", "8", ".", ".", ".", ".", "6", "."],
                            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                            [".", "6", ".", ".", ".", ".", "2", "8", "."],
                            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) == True

    assert is_valid_sudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                            [".", "9", "8", ".", ".", ".", ".", "6", "."],
                            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                            [".", "6", ".", ".", ".", ".", "2", "8", "."],
                            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) == False
    print('All tests passed!')
