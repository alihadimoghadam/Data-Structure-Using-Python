def knapsack_memo(W, weights, values, n, memo=None):
    """
    Solve the 0/1 Knapsack Problem using Memoization (Top-Down).

    The 0/1 Knapsack Problem determines the maximum value that can be obtained
    given a weight capacity, a set of items with weights, and corresponding values.

    Characteristics:
    - Time Complexity: O(n * W) (avoids recomputation).
    - Space Complexity: O(n * W) (due to recursion and memoization table).

    Args:
    W (int): Maximum weight capacity of the knapsack.
    weights (list): List of item weights.
    values (list): List of item values.
    n (int): Number of items.
    memo (dict): Dictionary to store computed values.

    Returns:
    int: Maximum value that can be obtained.
    """
    if memo is None:
        memo = {}

    if (n, W) in memo:
        return memo[(n, W)]

    if n == 0 or W == 0:
        return 0

    if weights[n - 1] > W:
        memo[(n, W)] = knapsack_memo(W, weights, values, n - 1, memo)
    else:
        include_item = values[n - 1] + knapsack_memo(W - weights[n - 1], weights, values, n - 1, memo)
        exclude_item = knapsack_memo(W, weights, values, n - 1, memo)
        memo[(n, W)] = max(include_item, exclude_item)

    return memo[(n, W)]


def knapsack_tab(W, weights, values, n):
    """
    Solve the 0/1 Knapsack Problem using Tabulation (Bottom-Up).

    Characteristics:
    - Time Complexity: O(n * W) (iterative DP approach).
    - Space Complexity: O(n * W) (uses a 2D DP table).

    Args:
    W (int): Maximum weight capacity of the knapsack.
    weights (list): List of item weights.
    values (list): List of item values.
    n (int): Number of items.

    Returns:
    int: Maximum value that can be obtained.
    """
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table iteratively
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]
