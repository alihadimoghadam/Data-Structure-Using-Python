from FenwickTree_Algorithm import FenwickTree

if __name__ == "__main__":
    # Example 1: Construct Fenwick Tree and Query
    arr1 = [1, 3, 5, 7, 9, 11]
    fenwick1 = FenwickTree(len(arr1))

    # Build Fenwick Tree
    for i, val in enumerate(arr1):
        fenwick1.update(i, val)

    print("Example 1: Fenwick Tree Queries")
    print(f"Prefix sum up to index 3: {fenwick1.prefix_sum(3)}")  # Output: 1+3+5+7 = 16
    print(f"Range sum from index 1 to 4: {fenwick1.range_sum(1, 4)}")  # Output: 3+5+7+9 = 24

    # Example 2: Update and Query
    fenwick1.update(2, 5)  # Increase arr[2] from 5 to 10
    print("\nExample 2: After Update")
    print(f"Prefix sum up to index 3: {fenwick1.prefix_sum(3)}")  # Output: 1+3+10+7 = 21
