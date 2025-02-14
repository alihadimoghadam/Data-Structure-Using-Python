from MCM_Algorithm import mcm_memo, mcm_tab

if __name__ == "__main__":
    # Example 1: Standard case
    p1 = [1, 2, 3, 4]
    print("Example 1: Matrix Chain Multiplication using Memoization")
    print(f"Minimum multiplications: {mcm_memo(p1, 1, len(p1) - 1)}")

    print("\nExample 1: Matrix Chain Multiplication using Tabulation")
    print(f"Minimum multiplications: {mcm_tab(p1)}")

    # Example 2: Another sequence of matrices
    p2 = [10, 20, 30, 40, 30]
    print("\nExample 2: Larger Matrices")
    print(f"Minimum multiplications: {mcm_tab(p2)}")

    # Example 3: More matrices
    p3 = [5, 10, 3, 12, 5, 50, 6]
    print("\nExample 3: More Complex Case")
    print(f"Minimum multiplications: {mcm_tab(p3)}")
