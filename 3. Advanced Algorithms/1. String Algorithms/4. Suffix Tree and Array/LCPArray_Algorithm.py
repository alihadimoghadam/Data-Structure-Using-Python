def build_lcp_array(s, suffix_array):
    """
    Construct the Longest Common Prefix (LCP) array.

    LCP Array helps in efficient substring searching and longest repeated substring problems.

    Characteristics:
    - Time Complexity: O(n) (single pass).
    - Space Complexity: O(n) (storing suffix ranks and LCP).

    Args:
    s (str): The input string.
    suffix_array (list): The suffix array of the string.

    Returns:
    list: The LCP array.
    """
    n = len(s)
    rank = [0] * n
    lcp = [0] * n

    # Compute the rank of each suffix in the suffix array
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i

    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while (i + h < n) and (j + h < n) and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1

    return lcp
