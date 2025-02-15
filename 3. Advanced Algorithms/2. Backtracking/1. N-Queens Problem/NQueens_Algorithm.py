def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
    board (list of lists): The chessboard.
    row (int): The current row.
    col (int): The current column.
    n (int): The size of the board.

    Returns:
    bool: True if it's safe to place a queen, False otherwise.
    """
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, n, solutions):
    """
    Solve the N-Queens problem using backtracking.

    Args:
    board (list of lists): The chessboard.
    row (int): The current row.
    n (int): The size of the board.
    solutions (list): List to store solutions.

    Returns:
    None
    """
    if row == n:
        solutions.append(["".join("Q" if cell else "." for cell in row) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack


def nqueens(n):
    """
    Generate all possible solutions for the N-Queens problem.

    Args:
    n (int): The size of the chessboard.

    Returns:
    list: A list of solutions, where each solution is represented as a list of strings.
    """
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    return solutions
