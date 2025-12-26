print("-------------- Practice Day 8 ----------------")

# Map questions
# 1. Word Frequency Counter
def word_frequency_counter(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
sample_text = "Hello world! Hello everyone. Welcome to the world of Python."
print(word_frequency_counter(sample_text))

# 2. word with maximum length
def word_with_max_length(words):
    if not words:
        return None
    max_word = words[0]
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word
print(word_with_max_length(["apple", "banana", "cherry", "watermelon", "kiwi"]))  # Output: "watermelon"

# 3. Remove Duplicates from List
def remove_duplicates(nums):
    return list(set(nums))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

# 4. Check Anagram
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  # Output: True

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

print("-------------- Practice Day 7 ----------------")