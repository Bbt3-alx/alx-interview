#!/usr/bin/python3
"""0. Rottate 2d Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix, rotate it 90 degrees clockwise."""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
