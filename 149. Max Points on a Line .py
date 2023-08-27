"""
149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.
"""


def max_points(points: list[list[int]]) -> int:
    maximum = 1
    for i in range(len(points)):
        count = 1
        for k in range(i + 1, len(points)):
            if points[i][0] == points[k][0]:
                count += 1
            if count > maximum:
                maximum = count
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        for j in range(i + 1, len(points)):
            if (points[i][0] - points[j][0]) != 0:
                m = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
            else:
                continue
            count = 2
            n = y - m * x
            for k in range(j + 1, len(points)):
                if round(points[k][1], 5) == round(points[k][0] * m + n, 5):
                    count += 1
            if count > maximum:
                maximum = count
    return maximum


if '__main__' == __name__:
    assert max_points([[1, 1], [2, 2], [3, 3]]) == 3
    assert max_points([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
    print('All tests passed!')
