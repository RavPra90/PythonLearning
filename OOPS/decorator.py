"""
Decorators

A decorator is a function that takes another function as input, adds some functionality, and returns a new function.
They are commonly used in Python for reusable code logic like logging, authentication, and access control.

"""
# A simple decorator
def decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@decorator  # Equivalent to: hello = decorator(hello)
def hello():
    print("Hello, World!")

hello()
# Output:
# Before the function is called.
# Hello, World!
# After the function is called.


#Decorator with Arguments
#A decorator can accept arguments by nesting another layer of functions.


def repeat(n):
    def decorator(func):
        def wrapper(*args, kwargs):
            for _ in range(n):
                func(*args, kwargs)
        return wrapper
    return decorator

@repeat(3)  # Call the function 3 times
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!



# Decorating Methods in Classes
#Decorators can also be used with methods inside classes.


def log_method_call(func):
    def wrapper(self, *args, kwargs):
        print(f"Method '{func.__name__}' called on {self}")
        return func(self, *args, kwargs)
    return wrapper

class Person:
    def __init__(self, name):
        self.name = name

    @log_method_call
    def greet(self):
        print(f"Hello, my name is {self.name}.")

p = Person("Alice")
p.greet()
# Output:
# Method 'greet' called on <__main__.Person object at 0x...>
# Hello, my name is Alice.


"""
Python decorators are widely used in real-world projects to add functionality to functions or methods without modifying their core logic. 

Decorators simplify repetitive tasks and enable code reusability in real-world scenarios like:

- Logging and debugging
- Authentication and security
- Performance monitoring
- Input validation
- Caching
- API management

Below are some real-world scenarios where decorators are commonly used:
"""


#Logging
#Decorators are used to log function calls, parameters, and results. This is especially useful in debugging or monitoring production systems.

#Example: Function Logging

import logging

logging.basicConfig(level=logging.INFO)

def log_function(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

add(3, 5)
# Output:
# Executing 'add' called with arguments (3, 5) and {}
# Function 'add' returned 8


#Use Case: Monitoring API endpoints, function performance, and debugging issues in real-world applications.



#Authentication and Authorization
#Decorators are often used in web frameworks (e.g., Flask, Django) to enforce user authentication and role-based access control.

#Example: Authorization Decorator

def requires_permission(role):
    def decorator(func):
        def wrapper(user, *args, kwargs):
            if user.get("role") == role:
                return func(user, *args, kwargs)
            else:
                raise PermissionError("You do not have the required permission!")
        return wrapper
    return decorator

@requires_permission("admin")
def delete_user(user, username):
    print(f"User {username} deleted by {user['username']}.")

# Simulate users
admin = {"username": "Alice", "role": "admin"}
regular_user = {"username": "Bob", "role": "user"}

delete_user(admin, "Charlie")  # Success
delete_user(regular_user, "Charlie")  # Raises PermissionError


#Use Case: Role-based access control in web applications.



# Caching
#Decorators are used to cache results of expensive function calls to avoid redundant computations and improve performance.

#Example: Simple Caching

import functools

def cache(func):
    stored_results = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in stored_results:
            print("Cache hit!")
            return stored_results[args]
        print("Cache miss!")
        result = func(*args)
        stored_results[args] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
# Output:
# Cache miss!
# ...
# Cache hit!


#Example: Use the functools.lru_cache decorator for memoization.
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(n):
    print(f"Computing {n}...")
    return n * n

print(expensive_computation(10))
print(expensive_computation(10))  # Cached result




#Performance Measurement
#A decorator can measure the execution time of a function to identify bottlenecks in performance.

#Example: Execution Timer

import time

def timer(func):
    def wrapper(*args, kwargs):
        start_time = time.time()
        result = func(*args, kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished!")

slow_function()
# Output:
# Finished!
# Function 'slow_function' executed in 2.0001 seconds.


#Use Case: Performance profiling in applications, particularly in data processing and computation-heavy tasks.



#Input Validation
#Decorators can validate the input arguments of functions, ensuring that they meet certain requirements before execution.

#Example: Input Validation

def validate_positive(func):
    def wrapper(*args):
        for arg in args:
            if arg < 0:
                raise ValueError("All arguments must be positive!")
        return func(*args)
    return wrapper

@validate_positive
def add_positive_numbers(a, b):
    return a + b

print(add_positive_numbers(3, 5))  # Output: 8
# add_positive_numbers(-3, 5)  # Raises ValueError


def validate_input(func):
    def wrapper(x, y):
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError("Inputs must be integers")
        return func(x, y)
    return wrapper

@validate_input
def multiply(x, y):
    return x * y

print(multiply(3, 5))  # Works
# print(multiply(3, '5'))  # Raises ValueError
#Use Case: Enforcing data integrity in APIs or other user-facing functions.



#Data Transformation
#Decorators can modify data returned by functions for consistent formatting or transformations.

 #Example: JSON Response Formatter

import json

def to_json(func):
    def wrapper(*args, kwargs):
        result = func(*args, kwargs)
        return json.dumps(result)
    return wrapper

@to_json
def get_data():
    return {"name": "Alice", "age": 25}

print(get_data())  # Output: '{"name": "Alice", "age": 25}'



# Retry Mechanism
#A decorator can retry a function automatically in case of failure, useful for handling network or transient errors.

#Example: Retry Decorator

import time
import random

def retry(max_retries):
    def decorator(func):
        def wrapper(*args, kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(1)
            raise Exception("All retries failed!")
        return wrapper
    return decorator

@retry(3)
def unstable_function():
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"

print(unstable_function())

