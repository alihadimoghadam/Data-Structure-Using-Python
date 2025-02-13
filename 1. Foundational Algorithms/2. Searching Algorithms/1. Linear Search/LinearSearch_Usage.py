from LinearSearch_Algorithm import linear_search

if __name__ == "__main__":
    # Example 1: Searching in an unsorted list
    arr_1 = [64, 34, 25, 12, 22, 11, 90]
    target_1 = 22
    print("Example 1:")
    print(f"List: {arr_1}")
    print(f"Searching for {target_1}: Index {linear_search(arr_1, target_1)}")

    # Example 2: Searching in a small list
    arr_2 = [5, 3, 8, 4, 2]
    target_2 = 8
    print("\nExample 2:")
    print(f"List: {arr_2}")
    print(f"Searching for {target_2}: Index {linear_search(arr_2, target_2)}")

    # Example 3: Searching for an element not in the list
    arr_3 = [1, 2, 3, 4, 5]
    target_3 = 10
    print("\nExample 3:")
    print(f"List: {arr_3}")
    print(f"Searching for {target_3}: Index {linear_search(arr_3, target_3)}")
