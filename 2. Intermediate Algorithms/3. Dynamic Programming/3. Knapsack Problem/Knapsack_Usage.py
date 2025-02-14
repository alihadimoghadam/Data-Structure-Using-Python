from Knapsack_Algorithm import knapsack_memo, knapsack_tab

if __name__ == "__main__":
    # Example 1: Standard knapsack problem
    W1 = 50
    weights1 = [10, 20, 30]
    values1 = [60, 100, 120]
    n1 = len(weights1)

    print("Example 1: Knapsack using Memoization")
    print(f"Max Value: {knapsack_memo(W1, weights1, values1, n1)}")

    print("\nExample 1: Knapsack using Tabulation")
    print(f"Max Value: {knapsack_tab(W1, weights1, values1, n1)}")

    # Example 2: Smaller capacity
    W2 = 10
    weights2 = [1, 4, 8]
    values2 = [10, 40, 50]
    n2 = len(weights2)

    print("\nExample 2: Knapsack with Small Capacity")
    print(f"Max Value: {knapsack_tab(W2, weights2, values2, n2)}")

    # Example 3: Large knapsack capacity
    W3 = 100
    weights3 = [20, 30, 40, 50]
    values3 = [100, 120, 150, 200]
    n3 = len(weights3)

    print("\nExample 3: Large Capacity Knapsack")
    print(f"Max Value: {knapsack_tab(W3, weights3, values3, n3)}")
