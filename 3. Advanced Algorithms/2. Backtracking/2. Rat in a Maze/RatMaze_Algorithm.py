def is_safe(maze, x, y, n):
    """
    Check if (x, y) is a valid move within the maze.

    Args:
    maze (list of lists): The maze grid.
    x (int): Current row.
    y (int): Current column.
    n (int): Size of the maze.

    Returns:
    bool: True if (x, y) is within bounds and open (1), False otherwise.
    """
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1


def solve_maze_util(maze, x, y, n, solution):
    """
    Recursive function to solve the maze using backtracking.

    Args:
    maze (list of lists): The maze grid.
    x (int): Current row.
    y (int): Current column.
    n (int): Size of the maze.
    solution (list of lists): The solution path.

    Returns:
    bool: True if a path is found, False otherwise.
    """
    if x == n - 1 and y == n - 1:  # Destination reached
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y, n):
        solution[x][y] = 1  # Mark as part of solution path

        # Move Right
        if solve_maze_util(maze, x, y + 1, n, solution):
            return True
        # Move Down
        if solve_maze_util(maze, x + 1, y, n, solution):
            return True

        # Backtrack
        solution[x][y] = 0
        return False

    return False


def solve_maze(maze):
    """
    Solve the Rat in a Maze problem using backtracking.

    Args:
    maze (list of lists): The maze grid.

    Returns:
    list of lists: Solution matrix with the path, or empty if no solution exists.
    """
    n = len(maze)
    solution = [[0] * n for _ in range(n)]

    if not solve_maze_util(maze, 0, 0, n, solution):
        return []  # No solution exists

    return solution
