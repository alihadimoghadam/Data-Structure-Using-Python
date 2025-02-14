def activity_selection(activities):
    """
    Solve the Activity Selection Problem using a Greedy Algorithm.

    The problem involves selecting the maximum number of non-overlapping activities 
    that can be scheduled given their start and end times.

    Characteristics:
    - Time Complexity: O(n log n) (due to sorting).
    - Space Complexity: O(1) (only uses variables for tracking).

    Args:
    activities (list of tuples): List of activities represented as (start_time, end_time).

    Returns:
    list: The maximum set of non-overlapping activities.
    """
    # Sort activities based on their finish time
    activities.sort(key=lambda x: x[1])

    selected_activities = []
    last_end_time = 0

    for start, end in activities:
        if start >= last_end_time:
            selected_activities.append((start, end))
            last_end_time = end

    return selected_activities
