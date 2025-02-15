class SegmentTree:
    """
    Implementation of Segment Tree for range queries and updates.

    Supports:
    - Range Sum Query
    - Point Updates

    Characteristics:
    - Time Complexity:
        - Build: O(n)
        - Query: O(log n)
        - Update: O(log n)
    - Space Complexity: O(n) (for storing the segment tree).
    """

    def __init__(self, arr):
        """
        Initialize the Segment Tree.

        Args:
        arr (list): The input array.
        """
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Segment tree size (4n for safety)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """
        Build the Segment Tree recursively.

        Args:
        arr (list): The input array.
        node (int): Current tree node index.
        start (int): Start index of the segment.
        end (int): End index of the segment.
        """
        if start == end:
            self.tree[node] = arr[start]  # Leaf node
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index, value, node=0, start=0, end=None):
        """
        Update an element in the array and the Segment Tree.

        Args:
        index (int): Index to update.
        value (int): New value.
        node (int): Current tree node.
        start (int): Start index of segment.
        end (int): End index of segment.
        """
        if end is None:
            end = self.n - 1

        if start == end:
            self.tree[node] = value  # Update leaf node
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            if index <= mid:
                self.update(index, value, left_child, start, mid)
            else:
                self.update(index, value, right_child, mid + 1, end)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def range_query(self, left, right, node=0, start=0, end=None):
        """
        Query the sum in a given range.

        Args:
        left (int): Left index of query.
        right (int): Right index of query.
        node (int): Current tree node.
        start (int): Start index of segment.
        end (int): End index of segment.

        Returns:
        int: Sum in the given range.
        """
        if end is None:
            end = self.n - 1

        # Out of range
        if right < start or left > end:
            return 0

        # Completely inside the range
        if left <= start and end <= right:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_sum = self.range_query(left, right, left_child, start, mid)
        right_sum = self.range_query(left, right, right_child, mid + 1, end)

        return left_sum + right_sum
