# In Python, dictionaries are key-value pair collections.
# Here's a comprehensive explanation with different ways to define and access elements from a dictionary


# 1. Defining a Dictionary
# Basic Definition

# Using curly braces
# empty dictionary
my_dict = {}
print(my_dict)
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)      # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Using `dict()` Constructor
# Using the dict() function
my_dict = dict(name="Alice", age=25, city="New York")
print(my_dict)     # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# With Mixed Data Types
# Keys can be strings, numbers, or even tuples (immutable)
my_dict = {1: "one", "two": 2, (3, 4): "tuple key"}
print(my_dict)     # Output : {1: 'one', 'two': 2, (3, 4): 'tuple key'}

# Using `zip()` to Combine Keys and Values
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
my_dict = dict(zip(keys, values))
print(my_dict)   # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)           # Output : {1: 'apple', 2: 'ball'}



#  Accessing Dictionary Elements
"""
    While indexing is used with other container types to access values, dictionary uses keys.
    Key can be used either inside square brackets or with the get() method.
    The difference while using get() is that it returns None instead of KeyError, 
        if the key is not found.

"""

# Using Square Brackets
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
 # Access by key
print(my_dict["name"])   #Output: Alice

# KeyError if the key does not exist
#print(my_dict["country"])   #Raises KeyError


# Using `get()` Method
# - Safer than square brackets as it allows a default value.
print(my_dict.get("age"))       #   Output: 25
print(my_dict.get("country", "N/A"))  # Output: N/A


# Accessing Keys, Values, and Items
#Keys
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# Values
print(my_dict.values())   #Output: dict_values(['Alice', 25, 'New York'])

#Key-Value pairs
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])



# 3. Adding or Updating Elements
# Add New Key-Value Pair
my_dict["country"] = "USA"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}

#Update Existing Key
my_dict["age"] = 30
print(my_dict)   #Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

#Using `update()` Method
my_dict.update({"profession": "Engineer", "city": "San Francisco"})
print(my_dict)
#Output: {'name': 'Alice', 'age': 30, 'city': 'San Francisco', 'country': 'USA', 'profession': 'Engineer'}



# Deleting Elements
"""
    We can remove a particular item in a dictionary by using the method pop().
    This method removes as item with the provided key and returns the value.
    The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary.
    All the items can be removed at once using the clear() method.
    We can also use the del keyword to remove individual items or the entire dictionary itself.

"""

#Using `del`
del my_dict["city"]
print(my_dict)   #Output: {'name': 'Alice', 'age': 30, 'country': 'USA', 'profession': 'Engineer'}

#Using `pop()`
removed = my_dict.pop("age")
print(removed)   #Output: 30
print(my_dict)   #Output: {'name': 'Alice', 'country': 'USA', 'profession': 'Engineer'}

# Using `popitem()`
# - Removes and returns the last inserted key-value pair.
last_item = my_dict.popitem()
print(last_item)   #Output: ('profession', 'Engineer')


# 5. Dictionary Comprehension

#Dictionary comprehension is an elegant and concise way to create new dictionary from an iterable in Python.
#Dictionary comprehension consists of an expression pair (key: value) followed by for statement inside curly braces {}.

# Creating a Dictionary
 #Squaring numbers
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#Filter Keys/Values
original = {"a": 10, "b": 15, "c": 20}
#The items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.
print("items in dictionary ",original.items())  #Output : items in dictionary  dict_items([('a', 10), ('b', 15), ('c', 20)])

filtered = {k: v for k, v in original.items() if v > 10}
print(filtered)   #Output: {'b': 15, 'c': 20}


# 6. Iterating Through a Dictionary
# Looping Through Keys
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for x in my_dict:
    print(x)   # Bydefault it prints the key - Outputs: name, age, country

# Looping Through Values
for value in my_dict.values():
    print(value)   #Outputs: Alice, 25, USA

#Looping Through Key-Value Pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")   #Output : name: Alice
                                #         age: 25
                                #         city: New York

#9. Accessing Nested Dictionaries
nested_dict = {"person": {"name": "Alice", "age": 25, "address": {"city": "NY", "zip": "10001"}}}
 #Access nested elements
print(nested_dict["person"]["address"]["city"])  # Output: NY

#Using `get()` for Nested Access
city = nested_dict.get("person", {}).get("address", {}).get("city", "Unknown")
print(city)  # Output: NY






