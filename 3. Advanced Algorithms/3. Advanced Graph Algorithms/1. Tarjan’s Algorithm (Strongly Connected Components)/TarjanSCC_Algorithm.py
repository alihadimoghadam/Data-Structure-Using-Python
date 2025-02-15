from collections import defaultdict

class TarjanSCC:
    """
    Implementation of Tarjan's Algorithm to find Strongly Connected Components (SCCs).

    Characteristics:
    - Time Complexity: O(V + E) (Depth-First Search based).
    - Space Complexity: O(V) (for tracking discovery times, low links, and stack).

    """

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0  # Global counter for discovery time
        self.stack = []
        self.in_stack = set()
        self.discovery = [-1] * vertices
        self.low = [-1] * vertices
        self.sccs = []

    def add_edge(self, u, v):
        """
        Add a directed edge from u to v.

        Args:
        u (int): Source vertex.
        v (int): Destination vertex.
        """
        self.graph[u].append(v)

    def _tarjan_util(self, u):
        """
        Recursive helper function for Tarjan's Algorithm.

        Args:
        u (int): Current vertex being visited.
        """
        self.discovery[u] = self.low[u] = self.time
        self.time += 1
        self.stack.append(u)
        self.in_stack.add(u)

        # Explore all neighbors
        for v in self.graph[u]:
            if self.discovery[v] == -1:  # If v is not visited
                self._tarjan_util(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif v in self.in_stack:  # If v is in stack, update low-link
                self.low[u] = min(self.low[u], self.discovery[v])

        # If u is the root of an SCC
        if self.low[u] == self.discovery[u]:
            scc = []
            while True:
                node = self.stack.pop()
                self.in_stack.remove(node)
                scc.append(node)
                if node == u:
                    break
            self.sccs.append(scc)

    def find_sccs(self):
        """
        Compute Strongly Connected Components (SCCs) using Tarjan's Algorithm.

        Returns:
        list: List of SCCs (each SCC is a list of vertices).
        """
        for i in range(self.V):
            if self.discovery[i] == -1:
                self._tarjan_util(i)
        return self.sccs
