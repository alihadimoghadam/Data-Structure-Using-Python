def fibonacci_memo(n, memo={}):
    """
    Compute the nth Fibonacci number using Memoization (Top-Down Approach).

    Memoization stores previously computed results to avoid redundant calculations.

    Characteristics:
    - Time Complexity: O(n) (linear, avoids recomputation).
    - Space Complexity: O(n) (due to recursion stack).
    
    Args:
    n (int): The position in the Fibonacci sequence.
    memo (dict): Dictionary to store computed Fibonacci values.

    Returns:
    int: The nth Fibonacci number.
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_tab(n):
    """
    Compute the nth Fibonacci number using Tabulation (Bottom-Up Approach).

    Tabulation avoids recursion by storing Fibonacci numbers iteratively.

    Characteristics:
    - Time Complexity: O(n) (linear).
    - Space Complexity: O(1) (constant, only stores last two values).

    Args:
    n (int): The position in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr  # Iteratively compute Fibonacci numbers

    return curr
