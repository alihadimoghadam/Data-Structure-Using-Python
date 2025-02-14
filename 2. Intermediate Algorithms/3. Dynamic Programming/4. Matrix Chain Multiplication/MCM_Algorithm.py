import sys

def mcm_memo(p, i, j, memo=None):
    """
    Solve Matrix Chain Multiplication using Memoization (Top-Down).

    The Matrix Chain Multiplication problem finds the optimal way to multiply a sequence of matrices
    to minimize the number of scalar multiplications.

    Characteristics:
    - Time Complexity: O(n^3) (avoids recomputation).
    - Space Complexity: O(n^2) (due to recursion and memoization table).

    Args:
    p (list): List of matrix dimensions (length n+1 for n matrices).
    i (int): Starting index of the matrix sequence.
    j (int): Ending index of the matrix sequence.
    memo (dict): Dictionary to store computed results.

    Returns:
    int: Minimum number of scalar multiplications needed.
    """
    if memo is None:
        memo = {}

    if i == j:
        return 0

    if (i, j) in memo:
        return memo[(i, j)]

    min_operations = sys.maxsize

    for k in range(i, j):
        left = mcm_memo(p, i, k, memo)
        right = mcm_memo(p, k + 1, j, memo)
        cost = p[i - 1] * p[k] * p[j] + left + right
        min_operations = min(min_operations, cost)

    memo[(i, j)] = min_operations
    return min_operations


def mcm_tab(p):
    """
    Solve Matrix Chain Multiplication using Tabulation (Bottom-Up).

    Characteristics:
    - Time Complexity: O(n^3) (iterative DP approach).
    - Space Complexity: O(n^2) (uses a 2D DP table).

    Args:
    p (list): List of matrix dimensions (length n+1 for n matrices).

    Returns:
    int: Minimum number of scalar multiplications needed.
    """
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):  # Chain length
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = sys.maxsize

            for k in range(i, j):
                cost = p[i - 1] * p[k] * p[j] + dp[i][k] + dp[k + 1][j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]
