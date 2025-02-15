def rabin_karp_search(text, pattern, prime=101):
    """
    Perform Rabin-Karp Pattern Matching using Rolling Hash.

    The algorithm uses a rolling hash function to efficiently search for a pattern in a text.

    Characteristics:
    - Time Complexity:
        - Best/Average Case: O(n + m) (efficient with good hash function)
        - Worst Case: O(n * m) (if many hash collisions occur)
    - Space Complexity: O(1) (constant extra space usage)

    Args:
    text (str): The text where the pattern is searched.
    pattern (str): The pattern to search.
    prime (int): A prime number for hashing.

    Returns:
    list: A list of starting indices where the pattern occurs in the text.
    """
    n, m = len(text), len(pattern)
    d = 256  # Number of characters in the input alphabet
    result = []

    if m > n or not pattern:
        return result

    # Compute hash for pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1  # Multiplier for highest place value

    # Compute h = d^(m-1) % prime
    for _ in range(m - 1):
        h = (h * d) % prime

    # Compute initial hash values
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime

    # Slide over text
    for i in range(n - m + 1):
        if pattern_hash == text_hash:  # Check if hash matches
            if text[i:i + m] == pattern:  # Verify actual substring match
                result.append(i)

        if i < n - m:  # Compute next window hash
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:  # Ensure non-negative hash
                text_hash += prime

    return result
