#!/usr/bin/python3
"""
Prime Game Module
Maria and Ben are playinginvolving prime.
Given a set of consecutive integers,
and removing that number and its multiples from
cannot make a move loses the game.

This module determines the winner
the player who won the most rounds.
"""

import math


def sieve(n):
    """Return a list of primes up to n using the Sieve."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i, prime in enumerate(is_prime) if prime]


def prime_count(n):
    """Return the number of primes less than or equal to n."""
    primes = sieve(n)

    count = [0] * (n + 1)

    for prime in primes:
        for i in range(prime, n + 1):
            count[i] += 1

    return count


def isWinner(x, nums):
    """
    Determine the winner of each game.
    Arguments:
    x number of rounds
    nums array of integers representing
    Returns:
    Name of the player that won the ("Maria" or "Ben").
    If the winner cannot be determined, return None.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    prime_counts = prime_count(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
