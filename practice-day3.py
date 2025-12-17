# Loops If else and switch case practice

# loops
print("----------- Day 3 -----------------")
for i in range(5):
    print("Iteration:", i)

# If-Else
num = 10
if num > 0:
    print(num, "is a positive number.")
elif num == 0:
    print(num, "is zero.")
else:
    print(num, "is a negative number.")

# Switch Case using dictionary mapping
def switch_case(case):
    switcher = {
        1: "You selected case 1",
        2: "You selected case 2",
        3: "You selected case 3"
    }
    return switcher.get(case, "Invalid case")
case_number = 2
print(switch_case(case_number))
print("----------- End of Day 3 -----------------")