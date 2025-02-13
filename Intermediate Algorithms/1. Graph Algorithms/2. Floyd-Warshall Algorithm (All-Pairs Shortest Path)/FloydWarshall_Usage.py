from FloydWarshall_Algorithm import floyd_warshall

if __name__ == "__main__":
    # Example 1: Graph with 4 nodes
    graph_1 = {
        'A': {'B': 3, 'C': 8, 'E': -4},
        'B': {'D': 1, 'E': 7},
        'C': {'B': 4},
        'D': {'A': 2, 'C': -5},
        'E': {'D': 6}
    }
    print("Example 1:")
    print(f"Graph: {graph_1}")
    result_1 = floyd_warshall(graph_1)
    print("Shortest distance matrix:")
    for row in result_1:
        print(row, result_1[row])

    # Example 2: Another graph with different weights
    graph_2 = {
        1: {2: 2, 3: 5},
        2: {3: 1, 4: 7},
        3: {4: 3},
        4: {1: 2}
    }
    print("\nExample 2:")
    print(f"Graph: {graph_2}")
    result_2 = floyd_warshall(graph_2)
    print("Shortest distance matrix:")
    for row in result_2:
        print(row, result_2[row])

    # Example 3: Graph with no direct connections
    graph_3 = {
        'X': {'Y': 10},
        'Y': {'Z': 5},
        'Z': {'X': 2}
    }
    print("\nExample 3:")
    print(f"Graph: {graph_3}")
    result_3 = floyd_warshall(graph_3)
    print("Shortest distance matrix:")
    for row in result_3:
        print(row, result_3[row])
