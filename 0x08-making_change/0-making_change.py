#!/usr/bin/python3
"""
Module 0-making_change
Contains a function to determine.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins.

    Args:
    coins (list of ints): the values of the coins.
    total (int): the amount to be met with coins.

    Returns:
    int: fewest number of coins needed to met.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total %= coin

    if total != 0:
        return -1

    return num_coins
