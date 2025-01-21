#Basic Function Definition and Calling

# Basic function with no parameters
def say_hello():
    print("Hello, World!")

# Calling the function
say_hello()  # Output: Hello, World!

# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!


# Return Values
#we can assign the return values to a variable in Python and then can reuse .

# Function returning a single value
def square(number):
    return number * number

result = square(5)
print(result+10)  # Output: 35

# Function returning multiple values
def get_coordinates():
    x = 10
    y = 20
    return x, y

x_pos, y_pos = get_coordinates()
print(f"X: {x_pos}, Y: {y_pos}")  # Output: X: 10, Y: 20


#return vs print
# Use print() when you want to display information to the user
# Use return when you need to use the function's result in other parts of your code
# A function without a return statement automatically returns None
# You can have multiple print statements in a function, but once a return is executed, the function ends

def add_with_print(a, b):
    print(a + b)

def add_with_return(a, b):
    return a + b

# Can't use the printed value in calculations
result_print = add_with_print(5, 3)  # Prints: 8
# result_print is None

# Can use the returned value
result_return = add_with_return(5, 3)  # Returns: 8
final_result = result_return * 2  # Can use result_return: 16


# Function Continuation:
def demonstrate_print():
    print("First line")
    print("Second line")  # Function continues after print
    print("Third line")

def demonstrate_return():
    return "First line"
    print("Second line")  # This will never execute
    print("Third line")   # This will never execute



# Default Parameters and Optional Arguments

def greet_user(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

greet_user("Bob")                  # Output: Hello, Bob!
greet_user("Bob", "Hi")           # Output: Hi, Bob!
greet_user("Bob", "Hey", "...")   # Output: Hey, Bob...

# *args and **kwargs for Variable Arguments

# *args for variable positional arguments
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))      # Output: 6
print(sum_numbers(1, 2, 3, 4))   # Output: 10

# **kwargs for variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York


#Lambda Functions (Anonymous Functions)
# Regular function
def double(x):
    return x * 2

# Equivalent lambda function
double_lambda = lambda x: x * 2

print(double(5))        # Output: 10
print(double_lambda(5)) # Output: 10

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(multiply(3, 4))   # Output: 12


# Function Documentation (Docstrings)

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The area of the rectangle
    """
    return length * width


# Access the documentation
print(calculate_area.__doc__)
help(calculate_area)


# Scope and Global Variables
global_var = 10

def modify_global():
    global global_var  # Declare we want to modify the global variable
    global_var = 20

def local_scope():
    local_var = 30  # This variable is only accessible inside the function
    print(local_var)

modify_global()
print(global_var)    # Output: 20










































































