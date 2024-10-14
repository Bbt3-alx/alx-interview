#!/usr/bin/env python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Lockboxes"""
    n = len(boxes)
    opened = set([0])
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in opened:
                opened.add(key)
                keys.append(key)
    return len(opened) == n
