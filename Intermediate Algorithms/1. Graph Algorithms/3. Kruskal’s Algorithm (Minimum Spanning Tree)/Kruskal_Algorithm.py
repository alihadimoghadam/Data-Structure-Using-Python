class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure with path compression and union by rank.

    Used to efficiently manage connected components in Kruskal’s Algorithm.
    """
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, node):
        """
        Find the representative (root) of a node's set with path compression.
        """
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        """
        Perform union of two sets using rank to balance the tree.
        """
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Attach smaller rank tree under larger rank tree
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(graph):
    """
    Perform Kruskal's Algorithm to find the Minimum Spanning Tree (MST).

    Kruskal’s Algorithm is a greedy algorithm that:
    1. Sorts edges by weight.
    2. Adds edges to the MST while avoiding cycles using the Disjoint Set (Union-Find).
    3. Stops when the MST contains (V - 1) edges.

    Characteristics:
    - Time Complexity: O(E log E) (due to sorting edges) where E = edges.
    - Space Complexity: O(V + E) (for storing sets and edges).
    - Finds the Minimum Spanning Tree (MST) efficiently.

    Args:
    graph (list): A list of edges represented as (weight, node1, node2).

    Returns:
    list: The Minimum Spanning Tree (MST) as a list of edges.
    """
    mst = []  # Store the MST edges
    edges = sorted(graph, key=lambda edge: edge[0])  # Sort edges by weight

    # Extract unique vertices
    vertices = set()
    for edge in edges:
        vertices.update(edge[1:])

    ds = DisjointSet(vertices)  # Initialize disjoint set

    for weight, u, v in edges:
        if ds.find(u) != ds.find(v):  # Check if adding the edge forms a cycle
            ds.union(u, v)
            mst.append((u, v, weight))

    return mst
