from SegmentTree_Algorithm import SegmentTree

if __name__ == "__main__":
    # Example 1: Build and Query Segment Tree
    arr1 = [1, 3, 5, 7, 9, 11]
    seg_tree1 = SegmentTree(arr1)

    print("Example 1: Segment Tree Queries")
    print(f"Sum from index 1 to 3: {seg_tree1.range_query(1, 3)}")  # Output: 3+5+7 = 15
    print(f"Sum from index 0 to 5: {seg_tree1.range_query(0, 5)}")  # Output: 1+3+5+7+9+11 = 36

    # Example 2: Update and Query
    seg_tree1.update(2, 10)  # Update arr[2] from 5 to 10
    print("\nExample 2: After Update")
    print(f"Sum from index 1 to 3: {seg_tree1.range_query(1, 3)}")  # Output: 3+10+7 = 20
