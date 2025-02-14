from LCS_Algorithm import lcs_memo, lcs_tab

if __name__ == "__main__":
    # Example 1: Finding LCS length
    X1, Y1 = "AGGTAB", "GXTXAYB"
    print("Example 1: LCS using Memoization")
    print(f"LCS length of '{X1}' and '{Y1}': {lcs_memo(X1, Y1, len(X1), len(Y1))}")

    print("\nExample 1: LCS using Tabulation")
    print(f"LCS length of '{X1}' and '{Y1}': {lcs_tab(X1, Y1)}")

    # Example 2: Shorter strings
    X2, Y2 = "ABC", "AC"
    print("\nExample 2: Shorter Strings")
    print(f"LCS length of '{X2}' and '{Y2}': {lcs_tab(X2, Y2)}")

    # Example 3: No common subsequence
    X3, Y3 = "XYZ", "PQR"
    print("\nExample 3: No Common Subsequence")
    print(f"LCS length of '{X3}' and '{Y3}': {lcs_tab(X3, Y3)}")
