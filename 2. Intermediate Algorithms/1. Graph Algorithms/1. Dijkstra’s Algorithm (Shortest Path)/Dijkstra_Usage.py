from Dijkstra_Algorithm import dijkstra

if __name__ == "__main__":
    # Example 1: Graph with 5 nodes
    graph_1 = {
        'A': [('B', 4), ('C', 1)],
        'B': [('A', 4), ('C', 2), ('D', 5)],
        'C': [('A', 1), ('B', 2), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    start_1 = 'A'
    print("Example 1:")
    print(f"Graph: {graph_1}")
    print(f"Shortest paths from {start_1}: {dijkstra(graph_1, start_1)}")

    # Example 2: Another graph with different weights
    graph_2 = {
        1: [(2, 7), (3, 9), (6, 14)],
        2: [(1, 7), (3, 10), (4, 15)],
        3: [(1, 9), (2, 10), (4, 11), (6, 2)],
        4: [(2, 15), (3, 11), (5, 6)],
        5: [(4, 6), (6, 9)],
        6: [(1, 14), (3, 2), (5, 9)]
    }
    start_2 = 1
    print("\nExample 2:")
    print(f"Graph: {graph_2}")
    print(f"Shortest paths from {start_2}: {dijkstra(graph_2, start_2)}")

    # Example 3: Graph with only two nodes
    graph_3 = {
        'X': [('Y', 5)],
        'Y': [('X', 5)]
    }
    start_3 = 'X'
    print("\nExample 3:")
    print(f"Graph: {graph_3}")
    print(f"Shortest paths from {start_3}: {dijkstra(graph_3, start_3)}")
