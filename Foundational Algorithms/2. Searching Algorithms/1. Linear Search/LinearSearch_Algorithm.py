def linear_search(arr, target):
    """
    Perform Linear Search on a list.

    Linear Search is a simple searching algorithm that:
    1. Iterates through the list one element at a time.
    2. Compares each element with the target value.
    3. Returns the index of the target if found, otherwise returns -1.

    Characteristics:
    - Time Complexity: O(n) in the worst and average cases, O(1) in the best case (if the target is the first element).
    - Space Complexity: O(1) (in-place search).
    - Works on both sorted and unsorted lists.

    Args:
    arr (list): The list of elements to search in.
    target (int or float): The value to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if target is not found
