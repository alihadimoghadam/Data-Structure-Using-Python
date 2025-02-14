from FractionalKnapsack_Algorithm import fractional_knapsack

if __name__ == "__main__":
    # Example 1: Standard case
    items1 = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
    capacity1 = 50
    print("Example 1: Fractional Knapsack")
    print(f"Maximum value: {fractional_knapsack(capacity1, items1)}")

    # Example 2: Exact weight match
    items2 = [(100, 10), (200, 20), (300, 30)]
    capacity2 = 60
    print("\nExample 2: Knapsack with Exact Weight")
    print(f"Maximum value: {fractional_knapsack(capacity2, items2)}")

    # Example 3: Items exceed capacity
    items3 = [(500, 50), (200, 20), (100, 10)]
    capacity3 = 30
    print("\nExample 3: Knapsack with Limited Capacity")
    print(f"Maximum value: {fractional_knapsack(capacity3, items3)}")
