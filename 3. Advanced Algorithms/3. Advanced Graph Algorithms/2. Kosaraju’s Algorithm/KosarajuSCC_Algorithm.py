from collections import defaultdict

class KosarajuSCC:
    """
    Implementation of Kosaraju’s Algorithm to find Strongly Connected Components (SCCs).

    Characteristics:
    - Time Complexity: O(V + E) (DFS-based approach).
    - Space Complexity: O(V) (for storing visited nodes and SCCs).
    """

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.transposed_graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Add a directed edge from u to v.

        Args:
        u (int): Source vertex.
        v (int): Destination vertex.
        """
        self.graph[u].append(v)

    def _dfs(self, v, visited, stack):
        """
        Perform DFS and push nodes onto a stack.

        Args:
        v (int): Current node.
        visited (set): Set of visited nodes.
        stack (list): Stack to store finishing order.
        """
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, stack)
        stack.append(v)

    def _transpose_graph(self):
        """
        Create the transposed graph (reversed edges).
        """
        for node in self.graph:
            for neighbor in self.graph[node]:
                self.transposed_graph[neighbor].append(node)

    def _dfs_transposed(self, v, visited, scc):
        """
        Perform DFS on the transposed graph to find SCCs.

        Args:
        v (int): Current node.
        visited (set): Set of visited nodes.
        scc (list): Current SCC being formed.
        """
        visited.add(v)
        scc.append(v)
        for neighbor in self.transposed_graph[v]:
            if neighbor not in visited:
                self._dfs_transposed(neighbor, visited, scc)

    def find_sccs(self):
        """
        Compute Strongly Connected Components (SCCs) using Kosaraju’s Algorithm.

        Returns:
        list: List of SCCs (each SCC is a list of vertices).
        """
        stack = []
        visited = set()

        # Step 1: Fill stack with finishing order from first DFS
        for i in range(self.V):
            if i not in visited:
                self._dfs(i, visited, stack)

        # Step 2: Transpose the graph
        self._transpose_graph()

        # Step 3: Perform DFS on transposed graph in order of stack
        visited.clear()
        sccs = []
        while stack:
            node = stack.pop()
            if node not in visited:
                scc = []
                self._dfs_transposed(node, visited, scc)
                sccs.append(scc)

        return sccs
