from Kruskal_Algorithm import kruskal

if __name__ == "__main__":
    # Example 1: Graph with 5 nodes
    graph_1 = [
        (2, 'A', 'B'),
        (3, 'A', 'D'),
        (3, 'B', 'C'),
        (4, 'B', 'D'),
        (5, 'C', 'D'),
        (1, 'D', 'E')
    ]
    print("Example 1:")
    print(f"Graph edges: {graph_1}")
    print(f"Minimum Spanning Tree: {kruskal(graph_1)}")

    # Example 2: Graph with 4 nodes
    graph_2 = [
        (1, 1, 2),
        (4, 1, 3),
        (3, 2, 3),
        (2, 2, 4),
        (5, 3, 4)
    ]
    print("\nExample 2:")
    print(f"Graph edges: {graph_2}")
    print(f"Minimum Spanning Tree: {kruskal(graph_2)}")

    # Example 3: Graph with 6 nodes
    graph_3 = [
        (4, 'X', 'Y'),
        (2, 'X', 'Z'),
        (1, 'Y', 'Z'),
        (6, 'Y', 'W'),
        (5, 'Z', 'W')
    ]
    print("\nExample 3:")
    print(f"Graph edges: {graph_3}")
    print(f"Minimum Spanning Tree: {kruskal(graph_3)}")
