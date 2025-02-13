from Prim_Algorithm import prim

if __name__ == "__main__":
    # Example 1: Graph with 5 nodes
    graph_1 = {
        'A': [('B', 2), ('D', 3)],
        'B': [('A', 2), ('C', 3), ('D', 4)],
        'C': [('B', 3), ('D', 5)],
        'D': [('A', 3), ('B', 4), ('C', 5), ('E', 1)],
        'E': [('D', 1)]
    }
    start_1 = 'A'
    print("Example 1:")
    print(f"Graph: {graph_1}")
    print(f"Minimum Spanning Tree: {prim(graph_1, start_1)}")

    # Example 2: Graph with 4 nodes
    graph_2 = {
        1: [(2, 1), (3, 4)],
        2: [(1, 1), (3, 3), (4, 2)],
        3: [(1, 4), (2, 3), (4, 5)],
        4: [(2, 2), (3, 5)]
    }
    start_2 = 1
    print("\nExample 2:")
    print(f"Graph: {graph_2}")
    print(f"Minimum Spanning Tree: {prim(graph_2, start_2)}")

    # Example 3: Graph with 6 nodes
    graph_3 = {
        'X': [('Y', 4), ('Z', 2)],
        'Y': [('X', 4), ('Z', 1), ('W', 6)],
        'Z': [('X', 2), ('Y', 1), ('W', 5)],
        'W': [('Y', 6), ('Z', 5)]
    }
    start_3 = 'X'
    print("\nExample 3:")
    print(f"Graph: {graph_3}")
    print(f"Minimum Spanning Tree: {prim(graph_3, start_3)}")
