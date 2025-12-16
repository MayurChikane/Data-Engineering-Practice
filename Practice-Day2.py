print("----------- Day 2 -----------------")

# Operators
# + addition
# - subtraction
# * multiply
# / divide
# % modulus
# ** power

# loops 
for i in range(0,10):
    print(i)

my_list = [1,"apple", 7, "books", True]
# a,b,c,*d=my_list
# print(a,b,c,d)
# print(my_list)

for items in my_list:
    print(items)
    
# List : ordered , modify and allows duplicate
test=[1,4,7,8,9,2,2,6]
print(test)

test[2]="Mango"
test[5]="Apple"
print(test)


# Tuple: ordered , unmodifiable and allows duplicate
my_tuple=(1,4,7,8,9,2,2,6)
print(my_tuple)
# my_tuple[2]="Mango"  # This will raise an error
# print(my_tuple)


# Sets : unordered , unmodifiable and no duplicates
my_set={1,4,7,8,9,2,2,6}
print(my_set)
my_set.add(10)
print(my_set)

# Dictionary : key-value pairs , unordered , modifiable and no duplicate keys
my_dict={
    "name":"John",
    "age":30,
    "city":"New York"
}   
print(my_dict)
my_dict["age"]=31
print(my_dict)
my_dict["job"]="Engineer"
print(my_dict)  
print("----------- End of Day 2 -----------------")
