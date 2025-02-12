def merge_sort(arr):
    """
    Perform Merge Sort on a list.

    Merge Sort is a divide-and-conquer algorithm that:
    1. Recursively splits the list into two halves until each half contains a single element.
    2. Merges the sorted halves back together in the correct order.

    Characteristics:
    - Time Complexity: O(n log n) in all cases (best, average, worst).
    - Space Complexity: O(n) (requires additional space for merging).
    - Stable Sorting: Maintains the relative order of equal elements.

    Args:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    # Split the array into left and right halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.

    Args:
    left (list): The left sorted list.
    right (list): The right sorted list.

    Returns:
    list: The merged and sorted list.
    """
    sorted_list = []
    i = j = 0

    # Merge while there are elements in both lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements from both lists
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list
