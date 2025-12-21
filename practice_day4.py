# Day 4

print("----------- Day 4 -----------------")
# Function practice
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

# Lambda functions
square = lambda x: x * x
print("Square of 5:", square(5))

# List comprehensions
squares = [x * x for x in range(10)]
print("Squares from 0 to 9:", squares)

# Set practice
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print("Updated Set:", my_set)
my_set.remove(3)
print("Set after removing 3:", my_set)
print("Is 4 in Set?", 4 in my_set)
my_set.clear()
print("Cleared Set:", my_set)

# list map with lambda
data = [1, 2, 3, 4, 5]
squared_data = list(map(lambda x: x * x, data))
print("Squared Data using map and lambda:", squared_data)

# high-order functions
def apply_function(func, value):
    return func(value)
result = apply_function(lambda x: x + 10, 5)
print("Result of applying function:", result)

def outer_function(msg):
    def inner_function():
        return f"Inner says: {msg}"
    return inner_function
inner = outer_function("Hello from inside!")
print(inner())

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught an exception:", e)

# File operations
with open("sample.txt", "w") as file:
    file.write("This is a sample file.\nDay 4 practice.")
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

print("----------- End of Day 4 -----------------")