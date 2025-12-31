print("-------------- Day 13 practice ----------")

# oops day 3
 
# Constructor basics
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person = Person("Alice", 30)
print(person.introduce())  # Output: Hello, my name is Alice and I am 30 years old.

# Inheritance
class Vehicle:
    def start_engine(self):
        return "Engine started"
class Car(Vehicle):
    def honk(self):
        return "Beep beep!"
car = Car()
print(car.start_engine())  # Output: Engine started
print(car.honk())          # Output: Beep beep!

# Abstract Classes
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

# Static Methods
class Utility:
    @staticmethod
    def add(a, b):
        return a + b
print(Utility.add(5, 10))  # Output: 15

# Class Methods
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count
print(Counter.increment())  # Output: 1
print(Counter.increment())  # Output: 2

# Composition
class Engine:
    def start(self):
        return "Engine started"
class CarWithEngine:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        return self.engine.start()
car_with_engine = CarWithEngine()
print(car_with_engine.start_car())  # Output: Engine started

# error handling with OOP
class CustomError(Exception):
    pass
def risky_method(value):
    if value < 0:
        raise CustomError("Negative value not allowed")
    return value * 2
try:
    print(risky_method(-5))
except CustomError as e:
    print(f"Caught an error: {e}")  # Output: Caught an error: Negative value not allowed
    
print("-------------- End of Day 13 practice ----------")