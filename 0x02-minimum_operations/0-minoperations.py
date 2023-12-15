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
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j], + 1 // j)
    return dp[n] if dp[n] != float('inf') else 0
