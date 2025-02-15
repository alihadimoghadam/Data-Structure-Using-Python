class FenwickTree:
    """
    Implementation of Fenwick Tree (Binary Indexed Tree) for range queries and updates.

    Supports:
    - Prefix Sum Queries
    - Point Updates

    Characteristics:
    - Time Complexity:
        - Build: O(n)
        - Query: O(log n)
        - Update: O(log n)
    - Space Complexity: O(n) (for storing the BIT array).
    """

    def __init__(self, n):
        """
        Initialize the Fenwick Tree.

        Args:
        n (int): Size of the input array.
        """
        self.n = n
        self.tree = [0] * (n + 1)  # 1-based index

    def update(self, index, value):
        """
        Update an index by adding value.

        Args:
        index (int): Index to update (0-based, converted to 1-based internally).
        value (int): Value to add.
        """
        index += 1  # Convert to 1-based index
        while index <= self.n:
            self.tree[index] += value
            index += index & -index  # Move to the next index

    def prefix_sum(self, index):
        """
        Compute prefix sum from index 0 to given index.

        Args:
        index (int): Query index (0-based, converted to 1-based internally).

        Returns:
        int: Sum from index 0 to given index.
        """
        index += 1  # Convert to 1-based index
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index  # Move to the parent index
        return total

    def range_sum(self, left, right):
        """
        Compute sum in the range [left, right].

        Args:
        left (int): Left index of the range.
        right (int): Right index of the range.

        Returns:
        int: Sum of the range [left, right].
        """
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
