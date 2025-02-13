def merge_sort(arr):
    """
    Perform Merge Sort using the Divide and Conquer approach.

    Merge Sort is a recursive sorting algorithm that:
    1. Divides the array into two halves until each half contains a single element.
    2. Recursively sorts each half.
    3. Merges the sorted halves back together in sorted order.

    Characteristics:
    - Time Complexity: O(n log n) in all cases (best, average, worst).
    - Space Complexity: O(n) (requires additional space for merging).
    - Stable Sorting: Maintains the relative order of equal elements.
    - Works well for **large datasets** and **linked lists**.

    Args:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        return arr  # Base case: A single element is already sorted

    mid = len(arr) // 2  # Divide step
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    return merge(left_half, right_half)  # Conquer step: Merge sorted halves


def merge(left, right):
    """
    Merge two sorted subarrays into a single sorted array.

    Args:
    left (list): The left sorted subarray.
    right (list): The right sorted subarray.

    Returns:
    list: The merged and sorted array.
    """
    sorted_list = []
    i, j = 0, 0

    # Merge elements while both lists have elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements from both lists
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list
