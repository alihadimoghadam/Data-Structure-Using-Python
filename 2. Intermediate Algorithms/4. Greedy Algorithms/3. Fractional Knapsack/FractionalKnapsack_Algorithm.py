def fractional_knapsack(capacity, items):
    """
    Solve the Fractional Knapsack Problem using a Greedy Algorithm.

    The problem involves selecting items to maximize total value while fitting within a weight limit.
    Unlike the 0/1 Knapsack, items can be broken into fractional parts.

    Characteristics:
    - Time Complexity: O(n log n) (due to sorting).
    - Space Complexity: O(1) (only uses variables for tracking).

    Args:
    capacity (int): Maximum weight capacity of the knapsack.
    items (list of tuples): List of items represented as (value, weight).

    Returns:
    float: Maximum total value that can be obtained.
    """
    # Calculate value-to-weight ratio and sort items in descending order
    items.sort(key=lambda item: item[0] / item[1], reverse=True)

    total_value = 0.0
    for value, weight in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)  # Take fraction of the item
            break  # Knapsack is full

    return total_value
