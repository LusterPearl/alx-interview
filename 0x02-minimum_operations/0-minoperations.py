#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed. If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    # Initialize the number of operations needed to reach each position with 0
    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        operations[i] = operations[i - 1] + 1  # Default to pasting one character

        # Check if we can optimize by copying all and pasting
        for j in range(2, i):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + i // j)
                
                return operations[n]
