# 1. Find the largest number in a list
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example list
print(numbers := [12, 35, 9, 56, 24])

# Call function and print result
print("1. Largest number in the list:", find_largest(numbers))
  
# 2. Find the second largest number in a list
def find_second_largest(numbers):
    largest = second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest

# Example list
numbers: [12, 35, 9, 56, 24]
print("2. Second largest number in the list:", find_second_largest(numbers))

# 3. Print Largest Even and Largest Odd Number in a List
def find_largest_even_odd(numbers):
    largest_even = float('-inf')
    largest_odd = float('-inf')
    
    for num in numbers:
        if num % 2 == 0 and num > largest_even:
            largest_even = num
        elif num % 2 != 0 and num > largest_odd:
            largest_odd = num
    
    return largest_even, largest_odd

# Example list
numbers = [12, 35, 9, 56, 24, 87, 45]

largest_even, largest_odd = find_largest_even_odd(numbers)

print("3. Largest Even Number:", largest_even)
print("Largest Odd Number:", largest_odd)

# 4. Find Average of a List
def find_average(numbers):
    return sum(numbers) / len(numbers)

# 5. Count Occurrences of Element in List
def count_occurrences(numbers, element):
    return numbers.count(element)

# 6. Remove Duplicates from a List
def remove_duplicates(numbers):
    return list(set(numbers))

# 7. Find the Number Occurring Odd Number of Times
def find_odd_occurrence(numbers):
    result = 0
    for num in numbers:
        result ^= num  # XOR method
    return result

# 8. Find the Union of Two Lists
def union_lists(list1, list2):
    return list(set(list1) | set(list2))

# 9. Swap the First and Last Element in a List
def swap_first_last(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# 10. Return the Length of the Longest Word
def longest_word_length(words):
    longest = max(words, key=len)
    return longest, len(longest)

# 11. Generate Random Numbers and Append to List
import random
def generate_random_list(n):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(1, 20))
    return numbers


# ----------------- Example Testing -----------------
numbers = [12, 35, 9, 56, 24, 87, 45, 24, 35, 9]
words = ["apple", "banana", "cherry", "watermelon"]

print("4. Average of list:", find_average(numbers))
print("5. Occurrences of 24:", count_occurrences(numbers, 24))
print("6. Remove duplicates:", remove_duplicates(numbers))
print("7. Number occurring odd number of times:", find_odd_occurrence([1, 2, 3, 2, 3, 1, 3]))
print("8. Union of two lists:", union_lists([1, 2, 3], [3, 4, 5]))
print("9. Swap first and last:", swap_first_last(numbers.copy()))
print("10. Longest word:", longest_word_length(words))
print("11. Random list:", generate_random_list(10))

print("--------------------dictionary operation--------------------")
# 1. Check if a Key Exists in a Dictionary
def check_key_exists(d, key):
    return key in d

# 2. Add a Key-Value Pair to the Dictionary
def add_key_value(d, key, value):
    d[key] = value
    return d

# 3. Find the Sum of All the Items in a Dictionary
def sum_dictionary(d):
    return sum(d.values())

# 4. Multiply All the Items in a Dictionary
def multiply_dictionary(d):
    result = 1
    for value in d.values():
        result *= value
    return result

# 5. Create Dictionary that Contains Number (x, x*x)
def create_square_dict(n):
    return {x: x*x for x in range(1, n+1)}

# 6. Concatenate Two Dictionaries
def concatenate_dicts(d1, d2):
    d3 = d1.copy()
    d3.update(d2)
    return d3


# ----------------- Example Testing -----------------
d = {"a": 10, "b": 20, "c": 30}

print("1. Key exists:", check_key_exists(d, "b"))
print("2. After adding:", add_key_value(d.copy(), "d", 40))
print("3. Sum of items:", sum_dictionary(d))
print("4. Multiply items:", multiply_dictionary(d))
print("5. Square dictionary:", create_square_dict(5))
print("6. Concatenate:", concatenate_dicts({"x": 1, "y": 2}, {"z": 3, "w": 4}))

print("--------------------tuple operation--------------------")

# Program 1: Create List of Tuples with Number and its Square

def number_square_tuples(start, end):
    return [(x, x**2) for x in range(start, end+1)]


# Example
print("List of Tuples (Number, Square):")
print(number_square_tuples(1, 5))


# Program 2: Remove All Tuples in a List Outside the Given Range

def filter_usn_tuples(prefix, lower, upper, usn_list):
    # Filter USNs within given range
    return [(prefix + str(num), num) for num in usn_list if lower <= num <= upper]


# Example
usn_numbers = [101, 102, 103, 104, 105, 110, 120]   # Example roll numbers
prefix = "USN"
lower = 102
upper = 110

filtered_list = filter_usn_tuples(prefix, lower, upper, usn_numbers)

print("Filtered USN Tuples:")
print(filtered_list)
