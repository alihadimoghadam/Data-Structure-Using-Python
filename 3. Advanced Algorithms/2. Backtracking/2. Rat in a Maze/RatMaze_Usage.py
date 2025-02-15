from RatMaze_Algorithm import solve_maze

if __name__ == "__main__":
    # Example 1: 4x4 Maze
    maze1 = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    print("Example 1: Rat in a Maze Solution")
    solution1 = solve_maze(maze1)
    if solution1:
        for row in solution1:
            print(row)
    else:
        print("No solution exists")

    # Example 2: Larger Maze
    maze2 = [
        [1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1]
    ]
    print("\nExample 2: Larger Maze")
    solution2 = solve_maze(maze2)
    if solution2:
        for row in solution2:
            print(row)
    else:
        print("No solution exists")
