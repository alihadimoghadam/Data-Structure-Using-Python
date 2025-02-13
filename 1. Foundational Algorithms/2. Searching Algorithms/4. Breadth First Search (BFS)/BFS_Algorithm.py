from collections import deque

def bfs(graph, start):
    """
    Perform Breadth First Search (BFS) on a graph.

    BFS is a traversal algorithm that explores all neighbors at the present depth
    before moving on to nodes at the next level.

    Characteristics:
    - Time Complexity: O(V + E) (V = vertices, E = edges).
    - Space Complexity: O(V) (due to queue storage).
    - Useful for shortest path problems, network broadcasting, and level-order traversal.

    Args:
    graph (dict): An adjacency list representation of a graph.
    start (any): The starting node.

    Returns:
    list: A list of nodes visited in BFS order.
    """
    visited = set()  # Track visited nodes
    queue = deque([start])  # Initialize queue with the start node
    traversal = []  # Store traversal order

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            queue.extend(graph.get(node, []))  # Add unvisited neighbors to the queue

    return traversal
