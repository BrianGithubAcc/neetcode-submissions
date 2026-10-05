from math import sin, cos, radians

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        result = [[0] * n for _ in range(n)]

        angle = radians(90)
        center = (n - 1) / 2

        for i in range(n):
            for j in range(n):
                x = j - center
                y = i - center

                new_x = x * cos(angle) - y * sin(angle)
                new_y = x * sin(angle) + y * cos(angle)

                new_j = round(new_x + center)
                new_i = round(new_y + center)

                result[new_i][new_j] = matrix[i][j]

        matrix[:] = result