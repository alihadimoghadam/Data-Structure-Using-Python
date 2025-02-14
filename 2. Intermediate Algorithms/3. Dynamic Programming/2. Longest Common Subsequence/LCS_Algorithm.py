def lcs_memo(X, Y, m, n, memo=None):
    """
    Compute the Length of Longest Common Subsequence (LCS) using Memoization (Top-Down).

    The LCS is the longest subsequence present in both strings in the same order but not necessarily contiguous.

    Characteristics:
    - Time Complexity: O(m * n) (avoids recomputation).
    - Space Complexity: O(m * n) (due to recursion and memoization table).

    Args:
    X (str): First string.
    Y (str): Second string.
    m (int): Length of X.
    n (int): Length of Y.
    memo (dict): Dictionary to store computed LCS values.

    Returns:
    int: The length of the longest common subsequence.
    """
    if memo is None:
        memo = {}

    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0 or n == 0:
        return 0

    if X[m - 1] == Y[n - 1]:
        memo[(m, n)] = 1 + lcs_memo(X, Y, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = max(lcs_memo(X, Y, m - 1, n, memo), lcs_memo(X, Y, m, n - 1, memo))

    return memo[(m, n)]


def lcs_tab(X, Y):
    """
    Compute the Length of Longest Common Subsequence (LCS) using Tabulation (Bottom-Up).

    Characteristics:
    - Time Complexity: O(m * n) (iterative DP approach).
    - Space Complexity: O(m * n) (uses a 2D DP table).

    Args:
    X (str): First string.
    Y (str): Second string.

    Returns:
    int: The length of the longest common subsequence.
    """
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table iteratively
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
