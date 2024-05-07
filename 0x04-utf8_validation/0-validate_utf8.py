#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            if (num >> 7) == 0b0:
                continue
            while (num >> (7 - num_bytes)) & 1:
                num_bytes += 1
            if num_bytes == 0 or num_bytes > 4:
                return False
            num_bytes = max(num_bytes - 1, 0)
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
