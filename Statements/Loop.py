# Python Loop Concepts: Basic and Advanced (with Code Snippets)

# Loops are a fundamental concept in Python that allow repetitive execution of a block of code.
# Below, we'll explore basic and advanced concepts of Python loops with practical code snippets.

# Basic Concepts

# `for` Loop
# The `for` loop iterates over a sequence (like a list, string, or range).
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for letter in "Python":
    print(letter)    #Output p y t h o n in each letter in a new line .


# `while` Loop
# The `while` loop continues until a condition is false.
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1


#Loop with `range()`
# The `range()` function generates a sequence of numbers.
for i in range(1, 6):
    print(i)


# Loop Control Statements:

# Break - exits the loop entirely
for number in range(10):
    if number == 5:
        break  # Stop when we hit 5
    print(number)

# Continue - skips the rest of the current iteration
for number in range(5):
    if number == 2:
        continue  # Skip printing 2
    print(number)

# Pass - does nothing, used as a placeholder
for number in range(3):
    if number == 1:
        pass  # Placeholder for future code
    else:
        print(number)



# `else` with Loops
# The `else` block executes after the loop completes, unless the loop is terminated by `break`.

# The else clause executes when the loop completes normally
# (not through a break statement)
for num in range(5):
    if num == 10:  # This will never be True
        break
    print(num)
else:
    print("Loop completed without breaking!")



 # Advanced Concepts

#Nested Loops
# A loop inside another loop.
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")


#Advanced Iteration Techniques:
from itertools import zip_longest

# Enumerate - when you need both index and value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors, start=1):  # start=1 begins counting at 1
    print(f"Color #{index}: {color}")

# Zip - parallel iteration
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# zip_longest - parallel iteration with different length sequences
extra_ages = [25, 30, 35, 40]
for name, age in zip_longest(names, extra_ages, fillvalue="Unknown"):
    print(f"{name} is {age} years old")



#  Looping Over Dictionaries
# Iterate over keys, values, or both in a dictionary.
student = {"name": "John", "age": 20, "grade": "A"}

for key, value in student.items():
    print(f"{key}: {value}")
# Output
# name: John
# age: 20
# grade: A

s= {'k1':'v1', 'k2':'v2', 'k3':'v3'}
for i in s:
    print(i)  # by default iterate over dictionary result in keys only
# Output
# k1
# k2
# k3

for i in s.items():
    print(i)
# Output
# ('k1', 'v1')
# ('k2', 'v2')
# ('k3', 'v3')

#Comprehensions - A Pythonic Way to Loop:

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}

# Generator Expressions - Memory Efficient Loops:

# Instead of creating a full list in memory
# Use a generator expression for large sequences

#sum_squares = sum(x**2 for x in range(100000))

# Custom generator function
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for fib in fibonacci_generator(10):
    print(fib)


# 15. Loop with Conditional Expression
# Add conditions directly within the loop.
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4]


# 16. Loop with `try` and `except`
# Handle exceptions inside a loop.
numbers = [1, 2, 0, 3]

for num in numbers:
    try:
        result = 10 / num
        print(f"10 / {num} = {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero!")


# 18. Unpacking Values in a Loop
# Unpack elements while iterating.
# Unpacking in a loop
pairs = [(1, "one"), (2, "two"), (3, "three")]
for number, name in pairs:
    print(f"{number}: {name}")


# Loop Performance Optimization
# Use `map()` or generator expressions for better performance.
# Using map for performance
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)
print(list(squares))  # Output: [1, 4, 9, 16, 25]
