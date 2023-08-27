"""
289. Game of Life
According to Wikipedia's article: "The Game of Life, also known simply as Life,
 is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state:
 live (represented by a 1) or dead (represented by a 0).
  Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules
  (taken from the above Wikipedia article):

    1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
"""


def game_of_life(board: list[list[int]]) -> None:
    m, n = len(board), len(board[0])
    for row in range(m):
        for col in range(n):
            neighbors = 0
            neighbors += int(board[row - 1][col - 1]) % 10 if row - 1 >= 0 and col - 1 >= 0 else 0
            neighbors += int(board[row - 1][col]) % 10 if row - 1 >= 0 and col >= 0 else 0
            neighbors += int(board[row - 1][col + 1]) % 10 if row - 1 >= 0 and col + 1 < n else 0
            neighbors += int(board[row][col - 1]) % 10 if row >= 0 and col - 1 >= 0 else 0
            neighbors += int(board[row][col + 1]) % 10 if row >= 0 and col + 1 < n else 0
            neighbors += int(board[row + 1][col - 1]) % 10 if row + 1 < m and col - 1 >= 0 else 0
            neighbors += int(board[row + 1][col]) % 10 if row + 1 < m and col >= 0 else 0
            neighbors += int(board[row + 1][col + 1]) % 10 if row + 1 < m and col + 1 < n else 0
            if board[row][col] == 1 or board[row][col] == '01' or board[row][col] == '11':
                if 1 < neighbors < 4:
                    board[row][col] = '11'
                else:
                    board[row][col] = '01'
            else:
                if neighbors == 3:
                    board[row][col] = '10'
                else:
                    board[row][col] = '00'
    for row in range(m):
        for col in range(n):
            board[row][col] = 1 if board[row][col][0] == '1' else 0
    return board


if '__main__' == __name__:
    assert game_of_life([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]) == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    assert game_of_life([[1, 1], [1, 0]]) == [[1, 1], [1, 1]]
    print('All tests passed!')
