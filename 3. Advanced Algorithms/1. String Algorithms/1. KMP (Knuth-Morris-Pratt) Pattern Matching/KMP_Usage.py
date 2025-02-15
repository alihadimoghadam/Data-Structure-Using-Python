from KMP_Algorithm import kmp_search

if __name__ == "__main__":
    # Example 1: Standard case
    text1 = "ababcabcabababd"
    pattern1 = "ababd"
    print("Example 1: KMP Pattern Matching")
    print(f"Pattern found at indices: {kmp_search(text1, pattern1)}")

    # Example 2: Pattern occurs multiple times
    text2 = "AABAACAADAABAABA"
    pattern2 = "AABA"
    print("\nExample 2: Multiple Occurrences")
    print(f"Pattern found at indices: {kmp_search(text2, pattern2)}")

    # Example 3: Pattern not found
    text3 = "hello world"
    pattern3 = "abc"
    print("\nExample 3: Pattern Not Found")
    print(f"Pattern found at indices: {kmp_search(text3, pattern3)}")
