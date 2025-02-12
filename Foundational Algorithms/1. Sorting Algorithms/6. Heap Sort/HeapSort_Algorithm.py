def heap_sort(arr):
    """
    Perform Heap Sort on a list.

    Heap Sort is a comparison-based sorting algorithm that:
    1. Builds a max heap from the input data.
    2. Extracts the largest element (root of the heap) and moves it to the end of the array.
    3. Re-heapifies the heap and repeats until all elements are sorted.

    Characteristics:
    - Time Complexity: O(n log n) in all cases (best, average, worst).
    - Space Complexity: O(1) (in-place sorting).
    - Not Stable: May change the relative order of equal elements.

    Args:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """

    def heapify(arr, n, i):
        """
        Helper function to maintain the heap property.

        Args:
        arr (list): The list representing the heap.
        n (int): Size of the heap.
        i (int): Index of the current root node.

        Returns:
        None (modifies arr in-place).
        """
        largest = i  # Assume root is largest
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest is not the root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)  # Recursively heapify the affected subtree

    n = len(arr)

    # Build a max heap (rearrange the array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr
