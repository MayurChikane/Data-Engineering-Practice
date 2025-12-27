print("----------- Day 9 Practice Problems ----------")

# 10 Problems for practice

# 1. Factorial of a Number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# 2. Check Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(29))  # Output: True

# 3. Fibonacci Sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 4. Palindrome Check
def is_palindrome(s):
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_s == cleaned_s[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True

# 5. Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))     
print(sum_of_digits(-12345))  # Output: 15

# 6. Merge Two Sorted Lists
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]

# 7. Count Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))  # Output: 3

# 8. Find Second Largest Number
def find_second_largest(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None
print(find_second_largest([10, 20, 4, 45, 99]))  # Output: 45

# 9. Reverse Words in a Sentence
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
print(reverse_words("Hello World from Python"))  # Output: "Python from World Hello"

# 10. Check Perfect Number
def is_perfect_number(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
print(is_perfect_number(28))  # Output: True

print("-------------- Practice Day 9 ----------------")