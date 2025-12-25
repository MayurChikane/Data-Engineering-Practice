# Day 7 Practice

print("----------- Day 7 -----------------")

# Problem solving exercises:

# 1. Two Sum Problem
def two_sum(nums, target):
    nmap= {}
    for i in range(len(nums)):
        complement= target - nums[i]
        if complement in nmap:
            return (nmap[complement], i)
        nmap[nums[i]]= i
    return None
print(two_sum([3,2,4], 6))  # Output: (1, 2)
        
# 2. Maximum in a List
def find_maximum(nums):
    if not nums:
        return None
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
print(find_maximum([1, 3, 2, 8, 5]))  # Output: 8

# 3. Reverse a String
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))  # Output: "olleh"

#4 . Fibonacci Sequence
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):  
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
print(fibonacci(7))  # Output: [0, 1, 1, 2, 3, 5, 8]

# 4. Palindrome Check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(is_palindrome("A man a plan a canal Panama"))  # Output: True

# 5. Factorial Calculation
def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))  # Output: 120

# 6. Prime Number Check
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(29))  # Output: True

# 7. 2nd Largest Element in a List
def second_largest(nums):
    if len(nums) < 2:
        return None
    first = second = 0
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second 
print(second_largest([3, 5, 1, 4, 2]))  # Output: 4

#8. Occurrence Count
def count_occurrences(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count
print(count_occurrences([1, 2, 3, 2, 4, 2], 2))  # Output: 3

#9. find Missing Number
def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
print(find_missing_number([1, 2, 4, 5], 5))  # Output: 3

#10. Find Duplicate in List
def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None
print(find_duplicate([1, 2, 3, 4, 2]))  # Output: 2

print("----------- End of Day 7 -----------------")