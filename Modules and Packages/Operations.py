"""

What is a Module?
A module is a single Python file (with .py extension) that contains definitions
of functions, classes, or variables.
"""

"""
I have already created math python file math_op and here i am importing the same. 
"""

# main.py
import math_op

print(math_op.add(5, 3))        # Output: 8
print(math_op.subtract(10, 4)) # Output: 6
print(math_op.PI)              # Output: 3.14159



#Importing Specific Functions/Classes

from math_op import add, subtract

print(add(10, 20))      # Output: 30
print(subtract(50, 15)) # Output: 35


#Executing a Module Directly
#Use __name__ == "__main__" to allow a module to be executed as a script or
# imported without executing its code.

#Contents of math_op.py:
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(5, 5))  # Only runs if the file is executed directly


"""

What is a Package?
A package is a collection of modules organized into directories with a 
special __init__.py file (can be empty). 
This structure allows you to create a hierarchical module namespace.

Creating a Package
Directory structure for the package:

Below is the pacakge I have defined 
my_package/
    __init__.py
    math_op.py
    string_op.py
    
"""

#Contents of __init__.py:

# __init__.py
from .math_op import add
from .string_op import capitalize_words


#Using the Package

# main.py
from my_package import add, capitalize_words

print(add(4, 5))  # Output: 9
print(capitalize_words("hello world"))  # Output: Hello World