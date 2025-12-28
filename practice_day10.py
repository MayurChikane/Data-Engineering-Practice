print("-------------- Day 10 Practice ----------")

# advanced functions and concepts
# lambda functions, map, filter, reduce

# 1. Lambda Function to Square a Number
square = lambda x: x * x
print(square(6))  # Output: 36

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
print(count_vowels("Lambda Functions are cool"))  # Output: 10

# 2. Using map() to Convert Celsius to Fahrenheit
celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(fahrenheit_temps)  # Output: [32.0, 68.0, 98.6, 212.0]

# 3. Using filter() to Get Even Numbers from a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# 4. Using reduce() to Calculate the Product of a List
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

print("-------------- Practice Day 10 ----------------")