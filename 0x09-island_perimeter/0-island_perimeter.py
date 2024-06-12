#!/usr/bin/python3
"""
Module to cal the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.
    Parameters:
    grid (list of list of int): A rectangular grid
    0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
