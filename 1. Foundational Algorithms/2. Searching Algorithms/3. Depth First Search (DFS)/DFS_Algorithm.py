def dfs(graph, start, visited=None):
    """
    Perform Depth First Search (DFS) on a graph.

    DFS is a traversal algorithm that explores as far as possible along each branch before backtracking.

    Characteristics:
    - Time Complexity: O(V + E) (V = vertices, E = edges).
    - Space Complexity: O(V) (due to recursion stack or explicit stack).
    - Useful for solving maze problems, cycle detection, and topological sorting.

    Args:
    graph (dict): An adjacency list representation of a graph.
    start (any): The starting node.
    visited (set): A set to track visited nodes.

    Returns:
    list: A list of nodes visited in DFS order.
    """
    if visited is None:
        visited = set()  # Initialize visited set if not provided

    visited.add(start)
    traversal = [start]  # Store the order of traversal

    for neighbor in graph.get(start, []):  # Get neighbors of the current node
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))  # Recursive DFS call

    return traversal
