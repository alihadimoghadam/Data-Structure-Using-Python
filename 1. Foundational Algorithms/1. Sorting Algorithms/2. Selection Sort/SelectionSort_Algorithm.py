def selection_sort(arr):
    """
    Perform Selection Sort on a list.

    Selection Sort is a simple sorting algorithm that divides the input list into two parts:
    the sorted part and the unsorted part. It repeatedly selects the smallest (or largest) element
    from the unsorted part and moves it to the sorted part.

    Characteristics:
    - Time Complexity: O(n^2) for all cases (best, average, worst).
    - Space Complexity: O(1) (in-place sorting).
    - Not Stable: May change the relative order of equal elements.

    Args:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Assume the current index holds the smallest value
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                # Update the index of the smallest element
                min_index = j
        # Swap the smallest element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
