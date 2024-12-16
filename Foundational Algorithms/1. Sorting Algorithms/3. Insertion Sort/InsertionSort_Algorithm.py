def insertion_sort(arr):
    """
    Perform Insertion Sort on a list.

    Insertion Sort is a simple sorting algorithm that works similarly to the way
    we sort playing cards in our hands. The list is virtually split into a sorted
    and an unsorted part. Values from the unsorted part are picked and placed at
    the correct position in the sorted part.

    Characteristics:
    - Time Complexity: O(n^2) in the worst and average cases, O(n) in the best case (when the list is already sorted).
    - Space Complexity: O(1) (in-place sorting).
    - Stable Sorting: Maintains the relative order of equal elements.

    Args:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
