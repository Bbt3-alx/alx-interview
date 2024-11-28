#!/usr/bin/python3
"""change commes from within"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    # Initialize dp array with infinity for all values except 0
    dp = [float("inf")] * (total + 1)
    dp[0] = 0  # 0 coins needed for total 0

    # Populate dp array
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:  # Coin can contribute to total
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1
