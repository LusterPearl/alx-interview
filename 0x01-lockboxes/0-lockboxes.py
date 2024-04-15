#!/usr/bin/python3
from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.
    
    Args:
        boxes: A list of lists where each inner list represents a box containing keys.
        
    Returns:
        True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    if n == 0:
        return False
    
    """Initialize a set to keep track of visited boxes"""
    visited = set()
    visited.add(0)
    
    """Initialize a queue to perform BFS """
    queue = [0]
    
    """BFS algorithm to traverse through boxes and keys"""
    while queue:
        current_box = queue.pop(0)
        
        """ Check all the keys in the current box """
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)
    
    """Check if all boxes have been visited"""
    return len(visited) == n