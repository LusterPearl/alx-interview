#!/usr/bin/python3
"""
N queens puzzle solver.

This script solves the N queens puzzle, which is the challenge of placing
N non-attacking queens on an N×N chessboard. The script uses a backtracking
algorithm to find all possible solutions.

Usage:
    ./0-nqueens.py N

Where N is the size of the chessboard
"""

import sys


def print_usage_and_exit():
    """Print usage message and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The chessboard.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    """Check left side of the row"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    """Check upper diagonal on left side"""
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    """Check lower diagonal on left side"""
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col):
    """
    Use backtracking to find all solutions for the N queens problem.

    Args:
        board (list): The chessboard.
        col (int): The current column index to place a queen.

    Returns:
        list: A list of all possible solutions, where each solution
              as a list of tuples (row, col).
    """
    if col >= len(board):
        return [[(i, row.index(1)) for i, row in enumerate(board)]]

    solutions = []
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            for solution in solve_nqueens(board, col + 1):
                solutions.append(solution)
            board[i][col] = 0

    return solutions


def main():
    """Main function to handle command-line arguments"""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = solve_nqueens(board, 0)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
