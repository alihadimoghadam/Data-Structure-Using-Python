def bubble_sort(arr):
    """
    Perform Bubble Sort on a list.

    Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order. This
    process is repeated until the list is sorted.

    Characteristics:
    - Time Complexity: O(n^2) in the worst and average cases, O(n) in the best case (when the list is already sorted).
    - Space Complexity: O(1) (in-place sorting).
    - Stable Sorting: Maintains the relative order of equal elements.

    Args:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Track if any swapping happens
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Optimization: Stop if no swapping happened
        if not swapped:
            break
    return arr
