from SudokuSolver_Algorithm import solve_sudoku

def print_sudoku(board):
    """
    Print the Sudoku board in a readable format.
    """
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

if __name__ == "__main__":
    # Example: Partially filled Sudoku board (0 represents an empty cell)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Board:")
    print_sudoku(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Board:")
        print_sudoku(sudoku_board)
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")
