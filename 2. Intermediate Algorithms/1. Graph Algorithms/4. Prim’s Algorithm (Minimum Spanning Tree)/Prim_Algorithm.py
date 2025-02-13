import heapq

def prim(graph, start):
    """
    Perform Prim's Algorithm to find the Minimum Spanning Tree (MST).

    Prim’s Algorithm is a greedy algorithm that:
    1. Starts with an arbitrary node.
    2. Grows the MST by adding the smallest weight edge that connects a visited node to an unvisited node.
    3. Repeats until all nodes are included in the MST.

    Characteristics:
    - Time Complexity: O(E log V) using a priority queue (E = edges, V = vertices).
    - Space Complexity: O(V) (to store visited nodes and priority queue).
    - Ensures that the Minimum Spanning Tree (MST) is connected and minimal.

    Args:
    graph (dict): An adjacency list representation of a weighted graph {node: [(neighbor, weight), ...]}.
    start (any): The starting node.

    Returns:
    list: The Minimum Spanning Tree (MST) as a list of edges.
    """
    mst = []  # Store the MST edges
    visited = set()  # Track visited nodes
    priority_queue = [(0, start, None)]  # (weight, current_node, parent)

    while priority_queue:
        weight, node, parent = heapq.heappop(priority_queue)

        if node not in visited:
            visited.add(node)
            if parent is not None:  # Exclude the first picked node
                mst.append((parent, node, weight))

            # Add all edges from the current node to the priority queue
            for neighbor, edge_weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (edge_weight, neighbor, node))

    return mst
