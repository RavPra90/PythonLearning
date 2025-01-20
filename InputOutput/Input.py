# Python offers versatile ways to take input from users,
# including handling simple inputs, handling multiple inputs,
# type casting, and advanced techniques.
# Below is a comprehensive explanation with code examples.

# 1. Using `input()` for Single Input
# By default The input() function always returns a string

# Single input
name = input("Enter your name: ")
print(f"Hello, {name}!")  # Output depends on user input

# Integer input , converting string to int
age = int(input("Enter your age: "))
print(f"Your age is {age}")  # Input: 25 -> Output: Your age is 25

# Float input
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters")  # Input: 1.75 -> Output: Your height is 1.75 meters



# Taking Multiple Inputs (Space-Separated)
# Use `split()` to handle multiple inputs on a single line.

# Multiple space-separated inputs
a, b, c = input("Enter three numbers separated by space: ").split()
print(f"a: {a}, b: {b}, c: {c}")  # Input: 10 20 30 -> Output: a: 10, b: 20, c: 30

# Convert space-separated input to integers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Numbers: {numbers}")  # Input: 1 2 3 4 -> Output: Numbers: [1, 2, 3, 4]

# Input list of strings
colors = input("Enter colors separated by commas: ").split(",")
print(f"Colors: {colors}")  # Input: red,blue,green -> Output: Colors: ['red', 'blue', 'green']

# Input list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Numbers: {numbers}")  # Input: 5 10 15 -> Output: Numbers: [5, 10, 15]



# Input with Default Values
# Set a default value when the user provides no input.

# Input with default value
name = input("Enter your name (default: Anonymous): ") or "Anonymous"
print(f"Hello, {name}!")  # Input: (Press Enter) -> Output: Hello, Anonymous!



# Using `sys.stdin` for Faster Input
# Useful when handling a large amount of input (e.g., competitive programming).

import sys

# Reading multiple lines of input
print("Enter multiple lines of text (Ctrl+D to stop):")
data = sys.stdin.read()
print("You entered:")
print(data)



# Advanced Input with `input()` and Conditions
# Validate inputs inline and re-prompt for valid data.

# Re-prompt until valid input
while True:
    value = input("Enter a positive number: ")
    if value.isdigit() and int(value) > 0:
        print(f"Valid input: {value}")
        break
    else:
        print("Invalid input. Try again.")




# Using `json.loads` for JSON Input
# Parse JSON input directly.

import json

# JSON input
data = input("Enter JSON data: ")  # Input: {"name": "Alice", "age": 25}
parsed = json.loads(data)
print(parsed)  # Output: {'name': 'Alice', 'age': 25}



# Input with Multi-Line String
# Read multi-line strings using `"""` or line breaks.

# Multi-line input
print("Enter multi-line text (type 'END' to finish):")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)
print("\n".join(lines))  # Output: Multi-line text as entered




# Advanced Mapping for Input Transformation
# Use `map()` to perform advanced input transformations.

# Mapping input to a tuple of squared values
numbers = map(int, input("Enter numbers: ").split())
squared = tuple(x**2 for x in numbers)
print(squared)  # Input: 1 2 3 -> Output: (1, 4, 9)



# Using `itertools` for Infinite Input
# Create infinite input iterators.
from itertools import count

# Infinite input iterator (break manually)
for i in count(1):
    value = input(f"Enter value #{i} (type 'stop' to exit): ")
    if value.lower() == "stop":
        break
    print(f"You entered: {value}")



# Input and Environment Variables
# Retrieve inputs via environment variables (useful in deployments).
import os

# Set an environment variable and access it
os.environ["USERNAME"] = "Alice"
name = os.getenv("USERNAME", "DefaultUser")
print(f"Hello, {name}!")  # Output: Hello, Alice!

