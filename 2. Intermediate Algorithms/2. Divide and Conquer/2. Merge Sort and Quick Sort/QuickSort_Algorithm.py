def quick_sort(arr):
    """
    Perform Quick Sort using the Divide and Conquer approach.

    Quick Sort is a recursive sorting algorithm that:
    1. Selects a pivot element.
    2. Partitions the list into elements smaller and greater than the pivot.
    3. Recursively sorts the left and right partitions.

    Characteristics:
    - Time Complexity:
        - Best & Average: O(n log n)
        - Worst: O(n^2) (if pivot selection is poor)
    - Space Complexity: O(log n) (recursive calls).
    - Not Stable: May change the relative order of equal elements.
    - Efficient for **large datasets** and **in-place sorting**.

    Args:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        return arr  # Base case: A single element is already sorted

    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and combine
