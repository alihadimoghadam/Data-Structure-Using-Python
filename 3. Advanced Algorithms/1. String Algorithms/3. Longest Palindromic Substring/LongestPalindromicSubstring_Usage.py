from LongestPalindromicSubstring_Algorithm import longest_palindromic_substring_dp, longest_palindromic_substring_center

if __name__ == "__main__":
    # Example 1: Standard case
    s1 = "babad"
    print("Example 1: Longest Palindromic Substring (DP)")
    print(f"Longest palindrome in '{s1}': {longest_palindromic_substring_dp(s1)}")

    print("\nExample 1: Longest Palindromic Substring (Expand Around Center)")
    print(f"Longest palindrome in '{s1}': {longest_palindromic_substring_center(s1)}")

    # Example 2: Another test case
    s2 = "cbbd"
    print("\nExample 2: Another Test Case")
    print(f"Longest palindrome in '{s2}': {longest_palindromic_substring_center(s2)}")

    # Example 3: A single character
    s3 = "a"
    print("\nExample 3: Single Character")
    print(f"Longest palindrome in '{s3}': {longest_palindromic_substring_dp(s3)}")
