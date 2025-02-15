def build_suffix_array(s):
    """
    Build a Suffix Array using sorting.

    A Suffix Array is an array of indices representing lexicographically sorted suffixes of a string.

    Characteristics:
    - Time Complexity: O(n log n) (due to sorting).
    - Space Complexity: O(n) (storing suffixes).

    Args:
    s (str): The input string.

    Returns:
    list: The suffix array containing starting indices of sorted suffixes.
    """
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()  # Sort based on suffixes
    return [suffix[1] for suffix in suffixes]
