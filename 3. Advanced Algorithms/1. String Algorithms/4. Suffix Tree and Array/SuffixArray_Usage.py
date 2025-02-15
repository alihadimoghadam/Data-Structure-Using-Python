from SuffixArray_Algorithm import build_suffix_array

if __name__ == "__main__":
    # Example 1: Basic String
    s1 = "banana"
    print("Example 1: Suffix Array")
    print(f"Suffix Array for '{s1}': {build_suffix_array(s1)}")

    # Example 2: Different String
    s2 = "mississippi"
    print("\nExample 2: Suffix Array for another string")
    print(f"Suffix Array for '{s2}': {build_suffix_array(s2)}")
