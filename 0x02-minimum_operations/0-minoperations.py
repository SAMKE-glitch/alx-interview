#!/usr/bin/python3
"""
min operations module
"""


def minOperations(n):
    """
    method that calculates min operations
    returns: integer
    """
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
