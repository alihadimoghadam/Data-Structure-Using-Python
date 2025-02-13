def quick_sort(arr):
    """
    Perform Quick Sort on a list.

    Quick Sort is a divide-and-conquer algorithm that:
    1. Selects a pivot element from the list.
    2. Partitions the list into two halves: elements smaller than the pivot and elements greater than the pivot.
    3. Recursively sorts both halves.

    Characteristics:
    - Time Complexity:
        - Best & Average: O(n log n)
        - Worst: O(n^2) (if the pivot selection is poor)
    - Space Complexity: O(log n) (recursive stack space)
    - Not Stable: May change the relative order of equal elements.

    Args:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)
