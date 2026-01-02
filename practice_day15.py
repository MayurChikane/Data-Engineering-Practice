print("--------------Practice Day 15--------------")

# Abstract Base Classes
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
rectangle = Rectangle(5, 10)
print(rectangle.area())  # Output: 50

# Decorators
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper
@uppercase_decorator
def greet():
    return "hello world"
print(greet())  # Output: HELLO WORLD

# Generators
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci(5):
    print(num)  # Output: 0 1 1 2 3
    
# Context Managers
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
with FileManager('test.txt', 'r') as f:
    content = f.read()
    print(content)  # Output: Hello, World!
    
# Lambda Functions and Map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# List Comprehensions
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

print("--------------End of Practice Day 15--------------")