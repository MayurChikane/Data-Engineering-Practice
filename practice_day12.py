print("-------------- Day 12 Practice ----------")

# oops day 2

# 1. Polymorphism
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
def animal_sound(animal):
    return animal.speak()
dog = Dog()
cat = Cat()
print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!

# 2. Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300

# 3. Method Overriding
class Parent:
    def greet(self):
        return "Hello from Parent"
class Child(Parent):
    def greet(self):
        return "Hello from Child"
child = Child()
print(child.greet())  # Output: Hello from Child

# 4. method  overloading using default arguments
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c
math_ops = MathOperations()
print(math_ops.add(2, 3))      # Output: 5
print(math_ops.add(2, 3, 4))   # Output: 9

print("-------------- Practice Day 12 ----------------")