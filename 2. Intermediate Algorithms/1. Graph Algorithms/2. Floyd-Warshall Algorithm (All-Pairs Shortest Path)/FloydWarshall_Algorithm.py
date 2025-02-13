def floyd_warshall(graph):
    """
    Perform the Floyd-Warshall Algorithm to find the shortest paths between all pairs of nodes.

    The Floyd-Warshall Algorithm is a dynamic programming approach that:
    1. Initializes a distance matrix with direct edge weights.
    2. Iteratively updates shortest paths using intermediate nodes.
    3. Computes the shortest distance between all pairs in O(V^3) time.

    Characteristics:
    - Time Complexity: O(V^3) (where V = number of vertices).
    - Space Complexity: O(V^2) (to store the distance matrix).
    - Works with **negative weights** but NOT with negative weight cycles.

    Args:
    graph (dict): An adjacency matrix representation of a weighted graph.

    Returns:
    list: A matrix where result[i][j] represents the shortest distance from node i to node j.
    """
    # Number of vertices
    nodes = list(graph.keys())
    n = len(nodes)

    # Initialize distance matrix
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}

    # Set distance to itself as 0 and existing edges as given weights
    for u in nodes:
        dist[u][u] = 0
        for v, weight in graph[u].items():
            dist[u][v] = weight

    # Apply Floyd-Warshall Algorithm
    for k in nodes:  # Intermediate node
        for i in nodes:  # Start node
            for j in nodes:  # End node
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
