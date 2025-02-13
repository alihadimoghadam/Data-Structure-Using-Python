from BinarySearch_Algorithm import binary_search

if __name__ == "__main__":
    # Example 1: Searching in a sorted list
    arr_1 = [10, 20, 30, 40, 50, 60, 70]
    target_1 = 40
    print("Example 1:")
    print(f"List: {arr_1}")
    print(f"Searching for {target_1}: Index {binary_search(arr_1, target_1)}")

    # Example 2: Searching in another sorted list
    arr_2 = [1, 3, 5, 7, 9, 11, 13]
    target_2 = 7
    print("\nExample 2:")
    print(f"List: {arr_2}")
    print(f"Searching for {target_2}: Index {binary_search(arr_2, target_2)}")

    # Example 3: Searching for an element not in the list
    arr_3 = [2, 4, 6, 8, 10]
    target_3 = 5
    print("\nExample 3:")
    print(f"List: {arr_3}")
    print(f"Searching for {target_3}: Index {binary_search(arr_3, target_3)}")
