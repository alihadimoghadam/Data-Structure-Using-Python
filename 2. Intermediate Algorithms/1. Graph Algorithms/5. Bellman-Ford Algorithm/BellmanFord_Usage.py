from BellmanFord_Algorithm import bellman_ford

if __name__ == "__main__":
    # Example 1: Graph with 5 nodes (No negative cycle)
    graph_1 = [
        ('A', 'B', 4), ('A', 'C', 1),
        ('B', 'C', 2), ('B', 'D', 5),
        ('C', 'D', 8), ('D', 'E', 2),
        ('E', 'C', -10)
    ]
    start_1 = 'A'
    print("Example 1:")
    print(f"Graph: {graph_1}")
    distances_1, has_cycle_1 = bellman_ford(graph_1, start_1)
    print(f"Shortest paths from {start_1}: {distances_1}")
    print(f"Negative Cycle Detected: {has_cycle_1}")

    # Example 2: Graph with a negative weight cycle
    graph_2 = [
        (1, 2, 4), (2, 3, -3), (3, 4, 2),
        (4, 2, 1), (4, 5, 3)
    ]
    start_2 = 1
    print("\nExample 2:")
    print(f"Graph: {graph_2}")
    distances_2, has_cycle_2 = bellman_ford(graph_2, start_2)
    print(f"Shortest paths from {start_2}: {distances_2}")
    print(f"Negative Cycle Detected: {has_cycle_2}")

    # Example 3: Simple graph with no negative weights
    graph_3 = [
        ('X', 'Y', 7), ('X', 'Z', 6),
        ('Y', 'Z', 3), ('Z', 'W', 5)
    ]
    start_3 = 'X'
    print("\nExample 3:")
    print(f"Graph: {graph_3}")
    distances_3, has_cycle_3 = bellman_ford(graph_3, start_3)
    print(f"Shortest paths from {start_3}: {distances_3}")
    print(f"Negative Cycle Detected: {has_cycle_3}")
