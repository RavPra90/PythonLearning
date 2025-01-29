#  Basic Concepts on Python Classes (with Code Snippets)
"""
Python classes are a fundamental part of object-oriented programming (OOP),
allowing you to create custom data structures with attributes and methods.
Here's a comprehensive overview of Python classes with examples:
1. What is a Class?
A class is a blueprint for creating objects. It defines attributes (variables) and methods (functions)
that the objects instantiated from the class will have.

"""

#We can create an empty class using pass statement in Python.
# An empty class
class Test:
    pass

# Basic syntax of a class
class MyClass:
    # Class attribute
    class_attribute = "I am a class attribute"

    """
    The word 'self' is used to represent the instance of a class.
    By using the "self" keyword we access the attributes and methods of the class in python.
    
    The __init__ method
    The __init__ method is similar to constructors in C++ and Java. It is run as soon as an object of a class is instantiated. 
    The method is useful to do any initialization you want to do with your object.
    """

    # Constructor method (initializer)
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute  # Instance attribute



# Create an object of MyClass
obj = MyClass("I am an instance attribute")
print(obj.instance_attribute)  # Output: I am an instance attribute
print(MyClass.class_attribute)  # Output: I am a class attribute




#Constructor Method (`__init__`)
# The `__init__` method is used to initialize an object’s attributes when the object is created.
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.introduce()  # Output: Hi, I am Alice and I am 25 years old.
person2.introduce()  # Output: Hi, I am Bob and I am 30 years old.




# 3. Class and Instance Attributes
# - Class attributes are shared among all instances of a class.
# - Instance attributes are unique to each object.
class Car:
    wheels = 4  # Class attribute (shared by all instances)

    def __init__(self, brand, color):
        self.brand = brand  # Instance attribute
        self.color = color  # Instance attribute

# Create two objects
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.wheels)  # Output: 4 (class attribute)
print(car2.brand)   # Output: Honda (instance attribute)

# Modifying instance attribute
car1.color = "Green"
print(car1.color)  # Output: Green

# Modifying class attribute
Car.wheels = 6
print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6




# Methods

"""
- Instance methods: Operate on an instance of the class.
- Class methods: Operate on the class itself (use `@classmethod`).
- Static methods: Don’t operate on an instance or the class (use `@staticmethod`).
- A class method takes cls as first parameter while a static method needs no specific parameters.
"""

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        print("This is a calculator class.")

    def subtract(self, a, b):
        return a - b

# Using the methods
print(Calculator.add(5, 3))  # Output: 8 (static method)
Calculator.info()            # Output: This is a calculator class. (class method)

calc = Calculator()
print(calc.subtract(10, 4))  # Output: 6 (instance method)



# Magic (Dunder) Methods
# Magic methods start and end with double underscores (`__`). Examples include `__init__`, `__str__`, and `__len__'

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

book = Book("Python Programming", 350)
print(book)       # Output: Book: Python Programming, Pages: 350
print(len(book))  # Output: 350