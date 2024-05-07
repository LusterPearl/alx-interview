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
    bytes_to_check = 0

    for num in data:
        if bytes_to_check == 0:
            if num >> 7 == 0:
                continue
            elif num >> 5 == 0b110:
                bytes_to_check = 1
            elif num >> 4 == 0b1110:
                bytes_to_check = 2
            elif num >> 3 == 0b11110:
                bytes_to_check = 3
            else:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            bytes_to_check -= 1

    return bytes_to_check == 0