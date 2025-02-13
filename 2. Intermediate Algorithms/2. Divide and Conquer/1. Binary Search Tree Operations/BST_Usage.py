from BST_Algorithm import BinarySearchTree

if __name__ == "__main__":
    bst = BinarySearchTree()

    # Example 1: Insert elements and perform inorder traversal
    elements = [50, 30, 70, 20, 40, 60, 80]
    for elem in elements:
        bst.insert(elem)

    print("Example 1: BST Inorder Traversal (Sorted Order):")
    print(bst.inorder_traversal())

    # Example 2: Search for elements
    search_keys = [40, 90]
    print("\nExample 2: Searching for elements in BST")
    for key in search_keys:
        print(f"Search {key}: {'Found' if bst.search(key) else 'Not Found'}")

    # Example 3: Delete elements and print inorder traversal
    delete_keys = [20, 30, 50]
    print("\nExample 3: Deleting elements from BST")
    for key in delete_keys:
        bst.delete(key)
        print(f"Deleted {key}, Updated Inorder Traversal: {bst.inorder_traversal()}")
