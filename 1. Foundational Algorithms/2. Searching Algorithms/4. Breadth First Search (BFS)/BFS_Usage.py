from BFS_Algorithm import bfs

if __name__ == "__main__":
    # Example 1: Simple graph traversal
    graph_1 = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    start_1 = 'A'
    print("Example 1:")
    print(f"Graph: {graph_1}")
    print(f"BFS traversal from {start_1}: {bfs(graph_1, start_1)}")

    # Example 2: A different graph structure
    graph_2 = {
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [6],
        5: [],
        6: []
    }
    start_2 = 1
    print("\nExample 2:")
    print(f"Graph: {graph_2}")
    print(f"BFS traversal from {start_2}: {bfs(graph_2, start_2)}")

    # Example 3: A cyclic graph
    graph_3 = {
        'X': ['Y', 'Z'],
        'Y': ['X', 'Z'],
        'Z': ['X', 'Y']
    }
    start_3 = 'X'
    print("\nExample 3:")
    print(f"Graph: {graph_3}")
    print(f"BFS traversal from {start_3}: {bfs(graph_3, start_3)}")
