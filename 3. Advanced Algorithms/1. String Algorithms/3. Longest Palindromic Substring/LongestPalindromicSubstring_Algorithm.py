def longest_palindromic_substring_dp(s):
    """
    Find the longest palindromic substring using Dynamic Programming.

    Characteristics:
    - Time Complexity: O(n^2) (due to filling DP table).
    - Space Complexity: O(n^2) (for storing DP table).

    Args:
    s (str): The input string.

    Returns:
    str: The longest palindromic substring.
    """
    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    # All single-character substrings are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check two-character substrings
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_length = i, 2

    # Check substrings longer than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start, max_length = i, length

    return s[start:start + max_length]


def expand_around_center(s, left, right):
    """
    Expand Around Center to find the longest palindrome.

    Args:
    s (str): The input string.
    left (int): Left index.
    right (int): Right index.

    Returns:
    str: The longest palindrome found.
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


def longest_palindromic_substring_center(s):
    """
    Find the longest palindromic substring using Expand Around Center.

    Characteristics:
    - Time Complexity: O(n^2) (due to expanding from each center).
    - Space Complexity: O(1) (no extra storage needed).

    Args:
    s (str): The input string.

    Returns:
    str: The longest palindromic substring.
    """
    if len(s) == 0:
        return ""

    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        palindrome1 = expand_around_center(s, i, i)
        # Even length palindrome
        palindrome2 = expand_around_center(s, i, i + 1)

        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest
