"""---- problem 733 in LeetCode----"""
def flood_fill(image, sr: int, sc: int, color: int):
    """
    ---Flood Fill Algorithm---
    This function performs a flood fill operation on the given image, starting from the pixel at position (sr, sc).
    A flood fill is a technique used to fill connected regions in an image with a specified color.

    :param image: The input image represented as a 2D grid of integers.
    :param sr: The row index of the starting pixel for flood fill.
    :param sc: The column index of the starting pixel for flood fill.
    :param color: The new color to be used for the flood-filled area.

    The flood fill process works as follows:
    - The starting pixel at position (sr, sc) is considered, and its color is changed to the new specified color.
    - The algorithm checks the four adjacent pixels (up, down, left, and right) to the starting pixel:
      - If any of these adjacent pixels have the same color as the starting pixel, they are considered part of the
        connected region and are also changed to the new color.
    - The algorithm recursively continues this process for each of the connected pixels, ensuring that all connected
      pixels of the same original color are changed to the new color.
    - This process continues until there are no more connected pixels of the same original color.

    After the flood fill is complete, the modified image is returned.

    :return: The modified image after the flood fill operation.
    """
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


# tests
if __name__ == '__main__':
    # Test case 1: Basic test with a simple 2x2 image
    image1 = [[1, 1],
              [1, 1]]
    print("Test case 1:", flood_fill(image1, 0, 0, 2) == [[2, 2], [2, 2]])

    # Test case 2: Image with a single pixel
    image2 = [[3]]
    print("Test case 2:", flood_fill(image2, 0, 0, 4) == [[4]])

    # Test case 3: Image with already filled region, no changes expected
    image3 = [[2, 2, 2],
              [2, 2, 2],
              [2, 2, 2]]
    print("Test case 3:", flood_fill(image3, 1, 1, 2) == image3)

    # Test case 4: Image with multiple connected regions
    image4 = [[1, 2, 3, 1],
              [1, 3, 2, 1],
              [3, 3, 3, 3],
              [2, 1, 1, 1]]
    print("Test case 4:", flood_fill(image4, 2, 1, 4) == [[1, 2, 3, 1], [1, 4, 2, 1], [4, 4, 4, 4], [2, 1, 1, 1]])

    # Test case 5: Image with large connected region
    image5 = [[5] * 10 for _ in range(10)]
    print("Test case 5:", flood_fill(image5, 5, 5, 6) == [[6] * 10 for _ in range(10)])

    # Test case 6: Image with a single row
    image6 = [[1, 2, 1, 2]]
    print("Test case 6:", flood_fill(image6, 0, 2, 3) == [[1, 2, 3, 2]])

    # Test case 7: Image with a single column
    image7 = [[4],
              [3],
              [3],
              [4]]
    print("Test case 7:", flood_fill(image7, 3, 0, 5) == [[4], [3], [3], [5]])

    # Test case 8: Image with a large region and multiple colors
    image8 = [[1, 2, 3, 2],
              [1, 2, 3, 3],
              [3, 3, 2, 1],
              [2, 1, 1, 1]]
    print("Test case 8:", flood_fill(image8, 0, 1, 4) == [[1, 4, 3, 2], [1, 4, 3, 3], [3, 3, 2, 1], [2, 1, 1, 1]])
