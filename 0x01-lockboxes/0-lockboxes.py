#!/usr/bin/python3
"""
lockboxes module
"""

from collections import deque


def canUnlockAll(boxes):
    """
    method for unlocking boxes
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])

    while queue:
        currentBox = queue.popleft()

        for key in boxes[currentBox]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)
    return all(visited)
