# Creating Strings

# Single and double quotes
string1 = 'Hello'
string2 = "World"

# Multi-line string
multiline_string = '''This is 
a multi-line 
string.'''

print(string1, string2)
print(multiline_string)

string3 = "i'm learning python"
print(string3)

# Accessing Characters in Strings

"""
Because strings are ordered sequences
it means we can using indexing and slicing to grab sub-sections of the string

Slicing allows you to grab a subsection of multiple characters, a “slice” of the string.
This has the following syntax:
[start:stop:step]
    start is a numerical index for the slice start
    stop is the index you will go up to (but not include)
    step is the size of the “jump” you take.

"""

# Accessing by index
string = "Python"
print(string[0])  # Output: P
print(string[-1])  # Output: n (last character)

# Slicing
print(string[1:4])  # Output: yth
print(string[:3])  # Output: Pyt
print(string[3:])  # Output: hon

# Immutable -Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)
name = 'Python'
# name[0]= 'L'  #it's not allowed in Python
# print(name) #TypeError: 'str' object does not support item assignment.

# We can do this by Concatenation
name = 'L' + name
print(name)  # LPython

#3.String Methods

# a. Basic String Methods

string = "Hello, World!"

# Length of the string
print(len(string))  # Output: 13

# Convert to uppercase and lowercase
print(string.upper())  # Output: HELLO, WORLD!
print(string.lower())  # Output: hello, world!

# Remove whitespace
whitespace_string = "   Trim me!   "
print(whitespace_string.strip())  # Output: "Trim me!"

# Check start or end
print(string.startswith("Hello"))  # Output: True
print(string.endswith("!"))  # Output: True

string = 'core java'
print(string.endswith(('txt', 'xml', 'java', 'orld')))  # Output: True

# b. Searching and Replacing

# Find substring
print(string.find("World"))  # Output: 7 (index of substring)

# Replace substring
new_string = string.replace("World", "Python")
print(new_string)  # Output: Hello, Python!

# Count occurrences of a character or substring
print(string.count("l"))  # Output: 3

# c. Splitting and Joining

# Split a string
sentence = "Split this into words"
words = sentence.split()  # Default split by space
print(words)  # Output: ['Split', 'this', 'into', 'words']

# Join a list of strings
joined = "-".join(words)
print(joined)  # Output: Split-this-into-words

# concatenation operator, '+'.
str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)


# d. String Case Manipulations

string = "python programming"

# Capitalize the first letter
print(string.capitalize())  # Output: Python programming

# Title case (capitalize first letter of each word)
print(string.title())  # Output: Python Programming

# Swap case
print(string.swapcase())  # Output: PYTHON PROGRAMMING

# e. Checking String Content

string = "Python123"

# Check if alphanumeric
print(string.isalnum())  # Output: True

# Check if alphabetic
print(string.isalpha())  # Output: False

# Check if numeric
print("12345".isnumeric())  # Output: True

# Check if all characters are lowercase or uppercase
print(string.islower())  # Output: False
print(string.isupper())  # Output: False

# index vs find
# index(): Returns the lowest index of the substring if it is found. Raises a ValueError if the substring is not found.
# find(): Also returns the lowest index of the substring if it is found. Returns -1 if the substring is not found

sub = 'Learning Python'
print(sub.find("n"))  # it will give me the first occurence of n  here o/p is 4
print(sub.find("z"))  # it will show -1 when the string is not present.
print(sub.index("n"))  # 4
# print(sub.index("z")) # it will throw an error ValueError: substring not found
