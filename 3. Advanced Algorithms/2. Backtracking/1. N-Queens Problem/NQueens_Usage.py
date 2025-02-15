from NQueens_Algorithm import nqueens

if __name__ == "__main__":
    # Example 1: Solve 4-Queens problem
    n1 = 4
    print(f"Example 1: {n1}-Queens Solutions")
    solutions1 = nqueens(n1)
    for solution in solutions1:
        for row in solution:
            print(row)
        print()

    # Example 2: Solve 8-Queens problem
    n2 = 8
    print(f"\nExample 2: {n2}-Queens Solutions (Showing First 2)")
    solutions2 = nqueens(n2)
    for solution in solutions2[:2]:  # Show only first 2 solutions
        for row in solution:
            print(row)
        print()
