#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place
    Args:
        matrix (list of list of int): The 2D matrix to rotate.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            top = matrix[first][i]

            matrix[first][i] = matrix[last - (i - first)][first]

            matrix[last - (i - first)][first] = matrix[
                   last][last - (i - first)]

            matrix[last][last - (i - first)] = matrix[i][last]

            matrix[i][last] = top
