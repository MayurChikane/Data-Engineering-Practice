print("------------------ Day 16 Practice ------------------")

#after learning oops concepts in day 15, now we will learn some advanced concepts in python

#1. Multiple Inheritance
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"  
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Hybrid(Dog, Cat):
    def speak(self):
        return f"Hybrid says: {Dog.speak(self)} and {Cat.speak(self)}"
hybrid = Hybrid()
print(hybrid.speak())  # Output: Hybrid says: Woof! and Meow!

#2. Method Resolution Order (MRO)
class A:
    def show(self):
        return "A"
class B(A):
    def show(self):
        return "B"
class C(A):
    def show(self):
        return "C"
class D(B, C):
    pass
d = D()
print(d.show())  # Output: B
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

#3. Super() Function
class Parent:
    def greet(self):
        return "Hello from Parent"
class Child(Parent):
    def greet(self):
        parent_greet = super().greet()
        return f"{parent_greet} and Hello from Child"
child = Child()
print(child.greet())  # Output: Hello from Parent and Hello from Child

#4. Class Methods and Static Methods
class MathOperations:
    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
print(MathOperations.add(5, 10))       # Output: 15
print(MathOperations.multiply(5, 10))  # Output: 50

#5. Property Decorators
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * (self._radius ** 2)
circle = Circle(5)
print(circle.radius)  # Output: 5
print(circle.area)    # Output: 78.53981633974483
circle.radius = 10
print(circle.area)    # Output: 314.1592653589793

#6. Data Classes
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
point = Point(10, 20)
print(point.x)  # Output: 10
print(point.y)  # Output: 20
print(point)    # Output: Point(x=10, y=20)

#7. Named Tuples
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
person = Person(name='Alice', age=30)
print(person.name)  # Output: Alice
print(person.age)   # Output: 30

# 8. Abstract Base Classes
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

# 9. Mixins
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
class User(JsonMixin):
    def __init__(self, username, email):
        self.username = username
        self.email = email
user = User('john_doe', 'john@example.com')
print(user.to_json())  # Output: {"username": "john_doe", "email": "john@example.com"}

#10. Slots
class PointWithSlots:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
point_slots = PointWithSlots(1, 2)
print(point_slots.x)  # Output: 1
print(point_slots.y)  # Output: 2


print("--------------End of Day 16 Practice--------------")