# Day 6 Practice
print("----------- Day 6 -----------------")

# custom exception for invalid age
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    return f"Valid age: {age}"
try:
    print(validate_age(25))
    print(validate_age(-5))
    print(validate_age(130))
except InvalidAgeError as e:
    print("Caught an exception:", e)
finally:
    print("Age validation is complete.")
    
# function to open a file and read its content
def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: An I/O error occurred."
    else:
        return content
print(read_file_content("example.txt"))

# function to access dictionary key
def access_dict_key(dct, key):
    try:
        return dct[key]
    except KeyError:
        return "Error: Key not found in dictionary."
    
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(access_dict_key(my_dict, 'b'))
print(access_dict_key(my_dict, 'z'))

# function to convert string to float
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return "Error: Cannot convert to float."
print(convert_to_float("12.34"))

# Nested exception handling
def nested_exception_handling(value):
    try:
        try:
            result = 100 / value
        except ZeroDivisionError:
            return "Error: Division by zero."
        return f"Result is {result}"
    except TypeError:
        return "Error: Invalid input type."
    
print(nested_exception_handling(0))
print(nested_exception_handling("abc"))

print("----------- End of Day 6 -----------------")