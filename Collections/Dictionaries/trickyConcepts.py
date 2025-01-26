# Here are some tricky and advanced concepts and methods of Python dictionaries that go beyond the basics:

# Using `defaultdict` from `collections
# Example: Grouping Data

from collections import defaultdict
"""
    defaultdict is a subclass of Python's built-in dict that provides a default value for non-existent keys.
    When you access a key that doesn't exist in the dictionary, defaultdict automatically initializes it with 
        the default value (defined when the defaultdict is created).
    Syntax:
    from collections import defaultdict

    defaultdict(default_factory)
    default_factory: A callable (e.g., list, int, set, etc.) that defines the default value for missing keys. For example:
    defaultdict(list) initializes a missing key with an empty list.
    defaultdict(int) initializes a missing key with 0.
"""
data = [("a", 1), ("b", 2), ("a", 3), ("b", 4), ("c", 5)]
grouped = defaultdict(list)
# This creates a dictionary where each key will have a default value of an empty list ([]) if it doesn’t already exist.

for key, value in data:
    grouped[key].append(value)

print(grouped)  # Output: {'a': [1, 3], 'b': [2, 4], 'c': [5]}


# Use Case: Word Frequency Count
from collections import defaultdict

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1
print(word_count)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}



#  2. `Counter` from `collections`
# A `Counter` is a dictionary subclass designed for counting hashable objects.
# Example: Counting Elements
from collections import Counter

data = ["a", "b", "a", "c", "b", "a"]
counter = Counter(data)
print(counter)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})

# Advanced Counter Operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)  # Addition: Counter({'a': 4, 'b': 3})
print(c1 - c2)  # Subtraction: Counter({'a': 2})



 # Dictionary Comprehensions with Conditions
# Example: Create Dictionary with Filters
data = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v for k, v in data.items() if v % 2 == 0}
print(filtered)  # Output: {'b': 2, 'd': 4}

# Example: Modify Values
squared = {k: v**2 for k, v in data.items()}
print(squared)  # Output: {'a': 1, 'b': 4, 'c': 9, 'd': 16}



#`ChainMap` from `collections`
# `ChainMap` groups multiple dictionaries into a single view.
# Example: Combine Dictionaries
from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

chain = ChainMap(dict1, dict2)
print(chain["a"])  # Output: 1 (from dict1)
print(chain["b"])  # Output: 2 (from dict1) (takes the first occurrence)
print(chain["c"])  # Output: 4 (from dict2)

# Use Case: Dynamic Scope Resolution
defaults = {"theme": "light", "version": 1.0}
user_settings = {"theme": "dark"}

config = ChainMap(user_settings, defaults)
print(config["theme"])  # Output: dark  (takes the first occurrence)
print(config["version"])  # Output: 1.0



# dict.fromkeys() for Uniform Initialization
# Easily create dictionaries with uniform values for all keys.
keys = ['a', 'b', 'c']
uniform_dict = dict.fromkeys(keys, 0)
print(uniform_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}


# Inverting a Dictionary
# Flip the keys and values of a dictionary.
data = {'a': 1, 'b': 2, 'c': 3}
inverted = {value: key for key, value in data.items()}
print(inverted)  # Output: {1: 'a', 2: 'b', 3: 'c'}



#Sorting a Dictionary
# By Keys
data = {"c": 3, "a": 10, "b": 2}
sorted_by_keys = dict(sorted(data.items()))
print(sorted_by_keys)  # Output: {'a': 10, 'b': 2, 'c': 3}

# By Values
sorted_by_values = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_by_values)  # Output: {'b': 2, 'c': 3,'a':10}

# Custom Sorting
# Sort by key length
data = {"apple": 3, "kiwi": 1, "banana": 2}
sorted_custom = dict(sorted(data.items(), key=lambda x: len(x[0])))
print(sorted_custom)  # Output: {'kiwi': 1, 'apple': 3, 'banana': 2}


dictlist=[{'name':'Rahul', 'age':23, 'marks':60}, {'name':'Anil', 'age':18, 'marks':55}, {'name':'Sunil', 'age':21, 'marks':90}]
newlist=sorted(dictlist, key = lambda k:k['name'])
print(newlist)
#output: [{'name': 'Anil', 'age': 18, 'marks': 55}, {'name': 'Rahul', 'age': 23, 'marks': 60}, {'name': 'Sunil', 'age': 21, 'marks': 90}]


"""
OrderedDict is a sub class of dictionary which remembers the order of entries added in dictionary object. 
When iterating over an ordered dictionary, the items are returned in the order their keys were first added.
"""
from collections import OrderedDict
D = {5:'fff', 3:'ttt', 1:'ooo',4:'bbb', 2:'ddd'}
OrderedDict(sorted(D.items(), key = lambda t: t[0]))
#Output: OrderedDict([(1, 'ooo'), (2, 'ddd'), (3, 'ttt'), (4, 'bbb'), (5, 'fff')])


# Nested Dictionary Operations
# Accessing and Updating Nested Keys
nested = {"person": {"name": "Alice", "details": {"age": 25, "city": "NY"}}}

# Access nested elements
print(nested["person"]["details"]["city"])  # Output: NY

# Update nested elements
nested["person"]["details"]["city"] = "San Francisco"
print(nested) #Output : {'person': {'name': 'Alice', 'details': {'age': 25, 'city': 'San Francisco'}}}


# Flatten a Nested Dictionary

def flatten_dict(d, parent_key="", sep="_"):
    flattened = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            flattened.update(flatten_dict(v, new_key, sep))
        else:
            flattened[new_key] = v
    return flattened

nested = {"a": {"b": {"c": 1}}, "d": 2}
print(flatten_dict(nested))  # Output: {'a_b_c': 1, 'd': 2}


# `setdefault()` Method
# `setdefault()` retrieves the value of a key, and if the key is missing, it assigns a default value.
# Example: Initialize Missing Keys
my_dict = {"a": 1, "b": 2}
my_dict.setdefault("c", 0)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 0}

# Use Case: Counting Frequency

data = ["a", "b", "a", "c", "b", "a"]
freq = {}

for item in data:
    freq[item] = freq.setdefault(item, 0) + 1

print(freq)  # Output: {'a': 3, 'b': 2, 'c': 1}



# Using `functools.lru_cache` with Dictionaries
# `lru_cache` memoizes function results for faster access.
# Example: Cache Expensive Function Results

from functools import lru_cache

@lru_cache(maxsize=None)
def expensive_function(x):
    print(f"Calculating for {x}")
    return x**2

print(expensive_function(5))  # Output: Calculating for 5, 25
print(expensive_function(5))  # Output: 25 (retrieved from cache)



# Dictionary Merging Precedence and Update Patterns:
 # The order of merging affects the final result
defaults = {'color': 'red', 'size': 'medium'}
user_settings = {'color': 'blue', 'theme': 'dark'}

# Different merging techniques produce different results
method1 = {**defaults, **user_settings}  # Later dict takes precedence
print(method1)  #Output : {'color': 'blue', 'size': 'medium', 'theme': 'dark'}
method2 = defaults | user_settings  # Python 3.9+ syntax
print(method2)      #Output : {'color': 'blue', 'size': 'medium', 'theme': 'dark'}
method3 = defaults.copy()
method3.update(user_settings)
print(method3)        #Output : {'color': 'blue', 'size': 'medium', 'theme': 'dark'}

# Chain updates with multiple dictionaries
settings = {}
settings.update(defaults)
settings.update(user_settings)
settings.update(temporary_override := {'color': 'green'})
print(settings)    #Output : {'color': 'green', 'size': 'medium', 'theme': 'dark'}


# Using Dictionary as a Switch-Case
# Dictionaries can be used as a substitute for switch-case statements.

def add(a, b): return a + b
def subtract(a, b): return a - b

switch = {
    'add': add,
    'subtract': subtract
}

result = switch['add'](10, 5)
print(result)  # Output: 15



# Check for Key or Value Existence
# Tricky Key/Value Search
data = {"a": 1, "b": 2, "c": 3}

# Check if key exists
if "a" in data:
    print("Key exists!")

# Check if value exists
if 2 in data.values():
    print("Value exists!")



# OrderedDict vs Regular Dict (Historical Context)
from collections import OrderedDict

# Prior to Python 3.7, regular dictionaries didn't maintain insertion order
# OrderedDict was used for this purpose
ordered = OrderedDict()
ordered['first'] = 1
ordered['second'] = 2
ordered['third'] = 3

# OrderedDict still has some unique features
# It considers order when comparing equality
dict1 = OrderedDict({'a': 1, 'b': 2})
dict2 = OrderedDict({'b': 2, 'a': 1})
print(dict1 == dict2)  # False - different order

# Regular dictionaries only compare contents
regular1 = {'a': 1, 'b': 2}
regular2 = {'b': 2, 'a': 1}
print(regular1 == regular2)  # True - order doesn't matter



# Dictionary Views and Their Dynamic Nature
# Dictionary views (keys(), values(), items()) are dynamic - they reflect dictionary changes
grades = {'Alice': 85, 'Bob': 92}
grade_views = grades.keys()
print(grade_views)  # dict_keys(['Alice', 'Bob'])

# The view automatically updates when the dictionary changes
grades['Charlie'] = 88
print(grade_views)  # dict_keys(['Alice', 'Bob', 'Charlie'])

# This can lead to unexpected behavior in loops if you modify while iterating
# Here's a common mistake:
for student in grades.keys():
    if grades[student] < 90:
        del grades[student]  # RuntimeError: dictionary changed size during iteration

# Correct approach using a list to create a static copy
for student in list(grades.keys()):
    if grades[student] < 90:
        del grades[student]  # Works correctly