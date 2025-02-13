class TreeNode:
    """
    A node in a Binary Search Tree (BST).
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A Binary Search Tree (BST) supporting insertion, search, and deletion operations.

    Characteristics:
    - Time Complexity:
      - Insertion: O(log n) (on average), O(n) (worst case, if unbalanced)
      - Search: O(log n) (on average), O(n) (worst case)
      - Deletion: O(log n) (on average), O(n) (worst case)
    - Space Complexity: O(n) (for storing nodes)
    - Works well when data is **sorted or nearly sorted**.

    """

    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Insert a new key into the BST.
        """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """Helper function to insert a key recursively."""
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """
        Search for a key in the BST.

        Returns:
        - True if key is found, otherwise False.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """Helper function to search for a key recursively."""
        if node is None or node.key == key:
            return node is not None
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        """
        Delete a key from the BST.
        """
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        """Helper function to delete a key recursively."""
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node with one or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in right subtree)
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        """Helper function to find the node with the smallest key."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """
        Perform inorder traversal of the BST (Left-Root-Right).
        Returns the elements in sorted order.
        """
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        """Helper function for inorder traversal."""
        return self._inorder_recursive(node.left) + [node.key] + self._inorder_recursive(node.right) if node else []
