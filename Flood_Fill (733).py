"""  ---Flood Fill--- (problem 733)
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color.
You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same
color), and so on. Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.
"""


def flood_fill(image, sr: int, sc: int, color: int):
    start_color = image[sr][sc]  # for the stopping condition of the recursion
    image[sr][sc] = color
    if start_color == color:
        return image
    if sr-1 >= 0 and start_color == image[sr-1][sc]:
        flood_fill(image, sr-1, sc, color)
    if sc-1 >= 0 and start_color == image[sr][sc-1]:
        flood_fill(image, sr, sc-1, color)
    if sr+1 < len(image) and start_color == image[sr+1][sc]:
        flood_fill(image, sr+1, sc, color)
    if sc+1 < len(image[0]) and start_color == image[sr][sc+1]:
        flood_fill(image, sr, sc+1, color)
    return image


if __name__ == '__main__':
    print(flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
    print(flood_fill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]])
