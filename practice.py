print("Hello World")

# this is a simple python comment

''' this is  a multi line comment
    this is another line of the comment
'''

# Variable
x=25
print(type(x))
print(x)

x="string value"
print(type(x))
print(x)

# Type casting
x=56
x=str(x)
print(type(x))
print(x)

# rules for variable
# 1. variable name should start with a letter or underscore
# 2. variable name can only contain alpha numeric characters and underscores (A-z, 0-9, and _ )
# 3. variable names are case sensitive
# 4. variable name should not be a reserved word
# 5. variable name should not contain spaces

# Camel Case
myVariableName = "Camel Case"
# Pascal Case
MyVariableName = "Pascal Case"
# Snake Case
my_variable_name = "Snake Case"

# Multiple Assignment
a = b = c = 10
x,y,z = "Orange", "Banana", 20

print(a , b , c)
print(x , y , z)

# Global variable
x = "Global Variable"
def myfunc():
    x = "fantastic"   # local variable
    print("x is " + x)
myfunc()
print("x is " +x)

# Global keyword
def myfunc1():
    global x         # making x as global variable
    x = "Wonderful"
    print("x is " + x)
myfunc1()
print("x is " + x)

# Data Types
x = "Hello World"   # string
x = 20              # int
x = 20.5            # float
x = 1j              # complex
x = ["apple", "banana", "cherry"]   # list
x = ("apple", "banana", "cherry")   # tuple
x = range(6)                       # range
x = {"name" : "John", "age" : 36}   # dict
x = {"apple", "banana", "cherry"}    # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True            # bool
x = b"Hello"       # bytes
x = bytearray(5)   # bytearray
x = memoryview(bytes(5))  # memoryview


# indexing and slicing
mystring = "Hello, World!"
print(mystring[0])        # H
print(mystring[7:12])    # World
print(mystring[-6:-1])   # World
print(mystring[:5])      # Hello
print(mystring[::2])     # Hlo ol!
print(mystring[::-1])    # !dlroW ,olleH
print(len(mystring))      # 13
print(mystring.upper())   # HELLO, WORLD!
print(mystring.lower())   # hello, world!
print(mystring.replace("World", "Python"))  # Hello, Python!
print(mystring.split(", "))  # ['Hello', 'World!']
print(mystring.strip())  # Hello, World!

# f-strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

statement = " this is a sample statement "
print("free" not in statement)  # True


# Project 1: Number Guessing Game
import random
x= random.randint(1,30)

while True:
    y= int(input("Guess a number between 1 to 30: "))
    if y < x:
        print("Sorry! Try a larger number")
    elif y > x:
        print("Sorry! Try a smaller number")
    else:
        print("Congratulations! You have guessed the number correctly")
        break

# Project 2: Simple Calculator
def operation():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice(1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == '4':
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input")
        
operation()

# Project 3: Invoice Generator
def generate_invoice(customer_name, items):
    print("Invoice for:", customer_name)
    print("----------------------------")
    total = 0
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")
        total += price
    print("----------------------------")
    print(f"Total: ${total:.2f}")

customer_name = "John Doe"
items = {
    "Item A": 29.99,
    "Item B": 49.99,
    "Item C": 19.99
}
generate_invoice(customer_name, items)

# Project 4: To-Do List Application
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f'Task "{task}" added to the list.')
    
def view_tasks():
    print("To-Do List:")
    for idx, task in enumerate(todo_list, start=1): 
        print(f"{idx}. {task}")

def remove_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f'Task "{removed_task}" removed from the list.')
    else:
        print("Invalid task number.")

add_task("Buy groceries")
add_task("Read a book")
view_tasks()
remove_task(1)
view_tasks()

