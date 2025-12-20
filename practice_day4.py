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

print("----------- End of Day 4 -----------------")