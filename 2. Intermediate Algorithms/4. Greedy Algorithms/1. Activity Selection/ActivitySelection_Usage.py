from ActivitySelection_Algorithm import activity_selection

if __name__ == "__main__":
    # Example 1: Standard case
    activities1 = [(1, 3), (2, 5), (3, 9), (0, 6), (5, 7), (8, 9)]
    print("Example 1: Activity Selection")
    print(f"Selected Activities: {activity_selection(activities1)}")

    # Example 2: All activities can be selected
    activities2 = [(1, 2), (3, 4), (5, 6), (7, 8)]
    print("\nExample 2: All Activities Fit")
    print(f"Selected Activities: {activity_selection(activities2)}")

    # Example 3: Only one activity fits
    activities3 = [(1, 10), (2, 5), (3, 7), (4, 6)]
    print("\nExample 3: Only One Activity Fits")
    print(f"Selected Activities: {activity_selection(activities3)}")
