from collections import deque

class EdmondsKarp:
    """
    Implementation of the Edmonds-Karp Algorithm for computing Maximum Flow.

    Characteristics:
    - Time Complexity: O(VE²) (where V = vertices, E = edges).
    - Space Complexity: O(V²) (for storing the capacity graph).
    """

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]  # Capacity graph

    def add_edge(self, u, v, capacity):
        """
        Add an edge with a given capacity to the flow network.

        Args:
        u (int): Source vertex.
        v (int): Destination vertex.
        capacity (int): Maximum capacity of the edge.
        """
        self.graph[u][v] = capacity

    def _bfs(self, source, sink, parent):
        """
        Perform BFS to find an augmenting path in the residual graph.

        Args:
        source (int): Source node.
        sink (int): Sink node.
        parent (list): Stores the path found.

        Returns:
        bool: True if there is an augmenting path, False otherwise.
        """
        visited = [False] * self.V
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v in range(self.V):
                if not visited[v] and self.graph[u][v] > 0:  # Check capacity
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True  # Found path to sink

        return False  # No more augmenting paths

    def max_flow(self, source, sink):
        """
        Compute the Maximum Flow in the flow network using Edmonds-Karp.

        Args:
        source (int): Source node.
        sink (int): Sink node.

        Returns:
        int: The maximum flow from source to sink.
        """
        parent = [-1] * self.V
        max_flow = 0

        while self._bfs(source, sink, parent):  # While there is an augmenting path
            path_flow = float("Inf")
            v = sink

            # Find the minimum residual capacity in the augmenting path
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = u

            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow  # Reduce capacity in forward direction
                self.graph[v][u] += path_flow  # Increase capacity in reverse direction
                v = u

            max_flow += path_flow  # Add path flow to total max flow

        return max_flow
