# Exception Handling Practice

print("----------- Day 5 -----------------")

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return f"The result is {result}"
    finally:
        print("Execution of divide_numbers is complete.")
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return "Error: The file was not found."
    except IOError:
        return "Error: An I/O error occurred."
    else:
        return content
print(read_file("non_existent_file.txt"))

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: List index out of range."
my_list = [10, 20, 30]
print(access_list_element(my_list, 1))
print(access_list_element(my_list, 5))

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return "Error: Cannot convert to integer."
print(convert_to_int("123"))
print(convert_to_int("abc"))

# Custom Exception
class NegativeNumberError(Exception):
    pass
def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    return f"{num} is a positive number."
try:
    print(check_positive_number(10))
    print(check_positive_number(-5))
except NegativeNumberError as e:
    print("Caught an exception:", e)
    print("File read operation is complete.")

# File Operations with Exception Handling
def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError:
        return "Error: Could not write to file."
    else:
        return "File written successfully."
    
print(write_to_file("output.txt", "This is a test."))

# Reading from file with exception handling
def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: Could not read file."
print(read_from_file("output.txt"))

print("----------- End of Day 5 -----------------")