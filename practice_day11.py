print("-------------- Day 11 Practice ----------")

# oops day 1

# 1. Define a Class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# 2. Create an Object
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())  # Output: 2020 Toyota Corolla

# 3. Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} with a {self.battery_size}-kWh battery"
# 4. Create an Object of the Subclass
my_electric_car = ElectricCar("Tesla", "Model 3", 2021, 75)
print(my_electric_car.display_info())  # Output: 2021 Tesla Model 3

# 5. Abstraction
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
rect = Rectangle(5, 10)
print(rect.area())  # Output: 50

print("-------------- Practice Day 11 ----------------")