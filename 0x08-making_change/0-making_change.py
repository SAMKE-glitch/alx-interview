#!/usr/bin/python3
"""
A module that defines a method makeChange
"""


def makeChange(coins, total):
    """
    method that determines fewest number of coins
    needed to meet a given amount of total
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Create a list to store the fewest number of coins
    # needed for each total from 0 to the target total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
            else:
                break
    return dp[total] if dp[total] != float('inf') else -1
