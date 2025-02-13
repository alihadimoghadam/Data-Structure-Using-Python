from InsertionSort_Algorithm import insertion_sort

if __name__ == "__main__":
    # Example 1: A moderately unsorted list
    unsorted_list_1 = [64, 34, 25, 12, 22, 11, 90]
    print("Example 1:")
    print("Unsorted List:", unsorted_list_1)
    sorted_list_1 = insertion_sort(unsorted_list_1)
    print("Sorted List:", sorted_list_1)

    # Example 2: A random list of small numbers
    unsorted_list_2 = [5, 3, 8, 4, 2]
    print("\nExample 2:")
    print("Unsorted List:", unsorted_list_2)
    sorted_list_2 = insertion_sort(unsorted_list_2)
    print("Sorted List:", sorted_list_2)

    # Example 3: An already sorted list
    unsorted_list_3 = [1, 2, 3, 4, 5]
    print("\nExample 3:")
    print("Unsorted List:", unsorted_list_3)
    sorted_list_3 = insertion_sort(unsorted_list_3)
    print("Sorted List:", sorted_list_3)
