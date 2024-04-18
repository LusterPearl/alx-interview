#!/usr/bin/python3
"""
Module for Lockboxes
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    if not boxes:
        return False

    # Initialize sets to keep track of opened boxes and keys
    opened_boxes = {0}
    keys = set(boxes[0])

    # Iterate through keys until no new key can be added to the set
    while keys:
        new_keys = set()
        for key in keys:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                new_keys.update(boxes[key])

        # If no new key is found, break the loop
        if len(opened_boxes) == len(boxes):
            return True

        keys = new_keys.difference(opened_boxes)

    return len(opened_boxes) == len(boxes)