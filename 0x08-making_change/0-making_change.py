#!/usr/bin/python3

"""Change making module.
"""


def makeChange(coins, total):

    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    
    if total <= 0:
        return 0
    
    # Initialize the dp array with infinity for all amounts except 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    # Iterate over each coin
    for coin in coins:
        # Update the dp array for all amounts from coin to total
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still infinity, it means total can't be reached
    return dp[total] if dp[total] != float('inf') else -1