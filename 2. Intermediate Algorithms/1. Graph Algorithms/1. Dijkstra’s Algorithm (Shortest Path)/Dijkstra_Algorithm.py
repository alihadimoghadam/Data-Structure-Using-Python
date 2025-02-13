import heapq

def dijkstra(graph, start):
    """
    Perform Dijkstra's Algorithm to find the shortest path from a start node to all other nodes.

    Dijkstra’s Algorithm is a greedy algorithm used to find the shortest path in a weighted graph with non-negative edges.

    Characteristics:
    - Time Complexity: O((V + E) log V) using a priority queue (V = vertices, E = edges).
    - Space Complexity: O(V) (to store distances and priority queue).
    - Works for graphs with non-negative weights.

    Args:
    graph (dict): An adjacency list representation of a weighted graph {node: [(neighbor, weight), ...]}.
    start (any): The starting node.

    Returns:
    dict: Shortest distance from start node to each node.
    """
    priority_queue = []  # Min-heap for selecting the shortest distance node
    heapq.heappush(priority_queue, (0, start))  # (distance, node)
    
    distances = {node: float('inf') for node in graph}  # Initialize distances
    distances[start] = 0

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if we already found a shorter path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path is found, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
