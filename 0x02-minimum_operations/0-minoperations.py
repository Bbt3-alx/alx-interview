#!/usr/bin/python3
"""0. Minimum Operations"""


def minOperations(n: int) -> int:
    """Minimun Operation"""
    if n <= 0:
        return 0

    operation: int = 0
    factor: int = 2

    while n > 1:
        while n % factor == 0:
            operation += factor
            n //= factor
        factor += 1

    return operation
