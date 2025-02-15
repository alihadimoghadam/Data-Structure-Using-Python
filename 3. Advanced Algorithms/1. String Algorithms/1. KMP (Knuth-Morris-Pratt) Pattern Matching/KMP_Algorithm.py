def compute_lps(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array for the KMP algorithm.

    The LPS array helps in skipping unnecessary character comparisons while searching.

    Characteristics:
    - Time Complexity: O(m) (where m is the length of the pattern).
    - Space Complexity: O(m) (for storing LPS values).

    Args:
    pattern (str): The pattern for which LPS is computed.

    Returns:
    list: LPS array.
    """
    lps = [0] * len(pattern)
    j = 0  # Length of the previous longest prefix suffix

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]  # Reset j using LPS

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j  # Store length of LPS for position i

    return lps


def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt (KMP) Pattern Matching.

    KMP improves search efficiency by using the LPS array to skip unnecessary comparisons.

    Characteristics:
    - Time Complexity: O(n + m) (where n = text length, m = pattern length).
    - Space Complexity: O(m) (for storing LPS values).

    Args:
    text (str): The text where the pattern is searched.
    pattern (str): The pattern to search.

    Returns:
    list: A list of starting indices where the pattern occurs in the text.
    """
    if not pattern or not text:
        return []

    lps = compute_lps(pattern)
    result = []
    j = 0  # Index for pattern

    for i in range(len(text)):  # i is index for text
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]  # Reset j using LPS

        if text[i] == pattern[j]:
            j += 1

        if j == len(pattern):
            result.append(i - j + 1)  # Found pattern at index (i - j + 1)
            j = lps[j - 1]  # Reset j using LPS

    return result
