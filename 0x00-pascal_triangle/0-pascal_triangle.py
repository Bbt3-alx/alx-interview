#!/usr/bin/python3


"""A module that perferm the Pascal's triangle operation"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers
    representing the pascal triangle of n
    args:
        n -> the number of row
    """
    if n <= 0:
        return []

    pascal_t = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal_t[i-1][j-1] + pascal_t[i-1][j])
        row.append(1)
        pascal_t.append(row)

    return pascal_t
