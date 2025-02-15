def is_valid(board, row, col, num):
    """
    Check if placing a number in a given cell follows Sudoku rules.

    Args:
    board (list of lists): The Sudoku board (9x9 grid).
    row (int): Row index.
    col (int): Column index.
    num (int): Number to place (1-9).

    Returns:
    bool: True if valid placement, False otherwise.
    """
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    """
    Solve a 9x9 Sudoku puzzle using Backtracking.

    Args:
    board (list of lists): The Sudoku board (9x9 grid).

    Returns:
    bool: True if solution exists, False otherwise.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try placing numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False  # No valid number found
    return True  # Puzzle solved
