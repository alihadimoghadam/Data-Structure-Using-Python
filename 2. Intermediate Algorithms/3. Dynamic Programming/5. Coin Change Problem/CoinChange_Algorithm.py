import sys

def coin_change_memo(coins, amount, memo=None):
    """
    Solve the Coin Change Problem using Memoization (Top-Down).

    The problem determines the minimum number of coins needed to make up a given amount.

    Characteristics:
    - Time Complexity: O(n * amount) (avoids recomputation).
    - Space Complexity: O(amount) (due to recursion and memoization table).

    Args:
    coins (list): List of available coin denominations.
    amount (int): Target amount.
    memo (dict): Dictionary to store computed results.

    Returns:
    int: Minimum number of coins needed, or -1 if not possible.
    """
    if memo is None:
        memo = {}

    if amount in memo:
        return memo[amount]
    
    if amount == 0:
        return 0

    if amount < 0:
        return sys.maxsize  # Return a large number to represent an impossible case.

    min_coins = sys.maxsize
    for coin in coins:
        result = coin_change_memo(coins, amount - coin, memo)
        if result != sys.maxsize:
            min_coins = min(min_coins, 1 + result)

    memo[amount] = min_coins
    return min_coins if min_coins != sys.maxsize else -1


def coin_change_tab(coins, amount):
    """
    Solve the Coin Change Problem using Tabulation (Bottom-Up).

    Characteristics:
    - Time Complexity: O(n * amount) (iterative DP approach).
    - Space Complexity: O(amount) (uses a 1D DP table).

    Args:
    coins (list): List of available coin denominations.
    amount (int): Target amount.

    Returns:
    int: Minimum number of coins needed, or -1 if not possible.
    """
    dp = [sys.maxsize] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != sys.maxsize:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != sys.maxsize else -1
