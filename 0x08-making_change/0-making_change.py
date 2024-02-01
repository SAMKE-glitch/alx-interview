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
    noOfCoins = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        noOfCoins += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return noOfCoins
