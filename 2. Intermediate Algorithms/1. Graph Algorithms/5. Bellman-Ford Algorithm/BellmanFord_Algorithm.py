def bellman_ford(graph, start):
    """
    Perform the Bellman-Ford Algorithm to find the shortest path from a start node to all other nodes.

    The Bellman-Ford Algorithm is a dynamic programming approach that:
    1. Iterates V-1 times (where V = number of vertices) to relax all edges.
    2. Detects negative weight cycles in a final iteration.
    3. Works even with negative edge weights (unlike Dijkstra’s Algorithm).

    Characteristics:
    - Time Complexity: O(V * E) (V = vertices, E = edges).
    - Space Complexity: O(V) (to store distances).
    - Works with **negative weights** and **detects negative cycles**.

    Args:
    graph (list): A list of edges represented as (source, destination, weight).
    start (any): The starting node.

    Returns:
    tuple: A dictionary with shortest distances and a boolean indicating if a negative cycle is detected.
    """
    # Extract unique vertices
    vertices = set()
    for edge in graph:
        vertices.update(edge[:2])
    vertices = list(vertices)

    # Initialize distances
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            return distances, True  # A negative cycle exists

    return distances, False  # No negative cycle found
