def binary_search(arr, target):
    """
    Perform Binary Search on a sorted list.

    Binary Search is an efficient searching algorithm that:
    1. Divides the list into two halves.
    2. Compares the middle element with the target.
    3. If the target is smaller, search in the left half; if larger, search in the right half.
    4. Repeats this process until the target is found or the list is exhausted.

    Characteristics:
    - Time Complexity: O(log n) in all cases (best, average, worst).
    - Space Complexity: O(1) (iterative) or O(log n) (recursive).
    - Works only on sorted lists.

    Args:
    arr (list): A sorted list of elements to search in.
    target (int or float): The value to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow in large lists

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found
