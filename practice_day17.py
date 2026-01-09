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

print("----------------- End of Mini Projects -----------------")