class UnionFind:
    """
    Implementation of Union-Find (Disjoint Set Union, DSU) with path compression and union by rank.

    Supports:
    - Union operation (merge sets).
    - Find operation (determine the set of an element).

    Characteristics:
    - Time Complexity:
        - Find: O(α(n)) (Inverse Ackermann, nearly constant)
        - Union: O(α(n)) (Inverse Ackermann, nearly constant)
    - Space Complexity: O(n) (for storing parent and rank arrays).
    """

    def __init__(self, size):
        """
        Initialize Union-Find data structure.

        Args:
        size (int): Number of elements.
        """
        self.parent = list(range(size))  # Parent array for each node
        self.rank = [1] * size  # Rank array for union by rank

    def find(self, x):
        """
        Find the root of the set containing x with path compression.

        Args:
        x (int): The element to find.

        Returns:
        int: The representative/root of the set.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """
        Merge two sets containing x and y.

        Args:
        x (int): First element.
        y (int): Second element.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        """
        Check if x and y are in the same set.

        Args:
        x (int): First element.
        y (int): Second element.

        Returns:
        bool: True if x and y are connected, False otherwise.
        """
        return self.find(x) == self.find(y)
