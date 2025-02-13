from MergeSort_Algorithm import merge_sort

if __name__ == "__main__":
    # Example 1: Sorting a list of numbers
    arr_1 = [38, 27, 43, 3, 9, 82, 10]
    print("Example 1:")
    print(f"Unsorted List: {arr_1}")
    print(f"Sorted List: {merge_sort(arr_1)}")

    # Example 2: Sorting a reversed list
    arr_2 = [5, 4, 3, 2, 1]
    print("\nExample 2:")
    print(f"Unsorted List: {arr_2}")
    print(f"Sorted List: {merge_sort(arr_2)}")

    # Example 3: Sorting an already sorted list
    arr_3 = [1, 2, 3, 4, 5]
    print("\nExample 3:")
    print(f"Unsorted List: {arr_3}")
    print(f"Sorted List: {merge_sort(arr_3)}")
