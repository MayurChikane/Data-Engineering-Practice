print("------------------------ Practice Day 18 ------------------------")

# Mini projects Continued from Day 17

# Sudoku small solver
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print()
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
def is_safe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True
def solve_sudoku(board):
    empty_loc = find_empty_location(board)
    if not empty_loc:
        return True
    row, col = empty_loc
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # backtrack
    return False

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 1, 2, 5, 4, 8, 9, 3, 6],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9, 1]
]
print("Sudoku Puzzle:")
print_board(sudoku_board)
if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print("--------------------------")
    print_board(sudoku_board)

# 8 Queens solver
N = 8
def solve_queens(board, row):
    if row >= N:
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
            board[row] = -1  # backtrack
    return False

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def print_queens(board):
    for i in range(N):
        row = ["."] * N
        if board[i] != -1:
            row[board[i]] = "Q"
        print(" ".join(row))
    print()

board = [-1] * N
if solve_queens(board, 0):
    print("8 Queens Solution:")
    print_queens(board)

print("--------------------End of Practice Day 18 --------------------")    