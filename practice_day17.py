# Mini Projects

print("----------------- Mini Projects -----------------")

# 1. Basic Calculator
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
calc = Calculator()
print(calc.add(10, 5))        # Output: 15
print(calc.subtract(10, 5))   # Output: 5
print(calc.multiply(10, 5))   # Output: 50
print(calc.divide(10, 5))     # Output: 2.0
print(calc.divide(10, 0))     # Output: Error! Division by zero.

# 2. Guess the Number Game
import random
class GuessTheNumber:
    def __init__(self, lower=1, upper=100):
        self.number_to_guess = random.randint(lower, upper)
        self.attempts = 0

    def guess(self, user_guess):
        self.attempts += 1
        if user_guess < self.number_to_guess:
            return "Too low!"
        elif user_guess > self.number_to_guess:
            return "Too high!"
        else:
            return f"Congratulations! You've guessed the number {self.number_to_guess} in {self.attempts} attempts."
game = GuessTheNumber()
print(game.guess(50))  # Example guess
print(game.guess(75))  # Example guess
print(game.guess(88))  # Example guess

# 3. To-Do List Application
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f'Task "{task}" added.'

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f'Task "{task}" removed.'
        else:
            return f'Task "{task}" not found.'

    def view_tasks(self):
        return self.tasks if self.tasks else "No tasks available."
    
todo = ToDoList()
print(todo.add_task("Buy groceries"))  # Output: Task "Buy groceries" added.
print(todo.add_task("Read a book"))     # Output: Task "Read a book" added.
print(todo.view_tasks())                 # Output: ['Buy groceries', 'Read a book']
print(todo.remove_task("Buy groceries")) # Output: Task "Buy groceries" removed.
print(todo.view_tasks())                 # Output: ['Read a book']

# Tic Tac Toe
# Tic Tac Toe Game in Python

board = [" " for _ in range(9)]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_conditions)

def is_draw():
    return " " not in board

def play_game():
    current_player = "X"

    while True:
        print_board()
        move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()



# 8 Queen Gameplay
N = 8

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i] == j:
            return False

    return True


def solve_queens(board, row):
    if row == N:
        print_solution(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(board, row + 1)
            board[row] = -1  # backtrack

    return False


def print_solution(board):
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print("\n")


# Driver code
board = [-1] * N
solve_queens(board, 0)



print("----------------- End of Mini Projects -----------------")
