from SuffixArray_Algorithm import build_suffix_array
from LCPArray_Algorithm import build_lcp_array

if __name__ == "__main__":
    # Example 1: Basic String
    s1 = "banana"
    suffix_array1 = build_suffix_array(s1)
    print("Example 1: Longest Common Prefix Array")
    print(f"LCP Array for '{s1}': {build_lcp_array(s1, suffix_array1)}")

    # Example 2: Different String
    s2 = "mississippi"
    suffix_array2 = build_suffix_array(s2)
    print("\nExample 2: LCP Array for another string")
    print(f"LCP Array for '{s2}': {build_lcp_array(s2, suffix_array2)}")
