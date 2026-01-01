print("--------------Practice Day 14--------------")

# Inheritance and Method Overriding
class Animal:
    def sound(self):
        return "Some sound"
class Dog(Animal):  
    def sound(self):
        return "Bark"
dog = Dog()
print(dog.sound())  # Output: Bark  

# Multiple Inheritance
class Flyer:
    def fly(self):
        return "Flying" 
class Swimmer:
    def swim(self):
        return "Swimming"
class Duck(Flyer, Swimmer):
    pass
duck = Duck()   
print(duck.fly())   # Output: Flying
print(duck.swim())  # Output: Swimming

# Polymorphism
class Cat:
    def sound(self):
        return "Meow"
def animal_sound(animal):
    return animal.sound()
cat = Cat()
print(animal_sound(cat))  # Output: Meow 

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# singleton pattern
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Output: True

print("--------------End of Practice Day 14--------------")
