from QuickSort_Algorithm import quick_sort

if __name__ == "__main__":
    # Example 1: Sorting a list of numbers
    arr_1 = [64, 25, 12, 22, 11, 90]
    print("Example 1:")
    print(f"Unsorted List: {arr_1}")
    print(f"Sorted List: {quick_sort(arr_1)}")

    # Example 2: Sorting a reversed list
    arr_2 = [5, 4, 3, 2, 1]
    print("\nExample 2:")
    print(f"Unsorted List: {arr_2}")
    print(f"Sorted List: {quick_sort(arr_2)}")

    # Example 3: Sorting an already sorted list
    arr_3 = [1, 2, 3, 4, 5]
    print("\nExample 3:")
    print(f"Unsorted List: {arr_3}")
    print(f"Sorted List: {quick_sort(arr_3)}")
