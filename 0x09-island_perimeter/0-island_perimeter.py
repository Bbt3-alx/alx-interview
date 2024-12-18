#!/usr/bin/python3
"""The Island Perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Up neighbor
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # Down neighbor
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                # Left neighbor
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # Right neighbor
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
