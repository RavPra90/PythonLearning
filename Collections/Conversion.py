"""
Python Collection Conversions: Different Ways to Convert Between Collections
In Python, we often need to convert one collection type (list, tuple, set, dictionary, etc.) into another.
Below are various methods to achieve these conversions, along with explanations and code snippets.
"""


# 1. Converting Between Lists, Tuples, and Sets

#  1.1 List to Tuple
# Use the `tuple()` function to convert a list into a tuple.
lst = [1, 2, 3, 4]
tpl = tuple(lst)
print(tpl)  # Output: (1, 2, 3, 4)
# - Use Case: When you need an immutable version of a list.
# - Time Complexity: \( O(n) \) (since all elements must be copied).



#  1.2 List to Set
# Use the `set()` function to remove duplicates from a list.
lst = [1, 2, 2, 3, 4, 4]
st = set(lst)
print(st)  # Output: {1, 2, 3, 4}
# - Use Case: Removing duplicates from a list.
# - Time Complexity: \( O(n) \).



#  1.3 Tuple to List
# Use the `list()` function.
tpl = (1, 2, 3, 4)
lst = list(tpl)
print(lst)  # Output: [1, 2, 3, 4]
# - Use Case: If you need a mutable version of a tuple.
# - Time Complexity: \( O(n) \).



#  1.4 Set to List
# Use `list()` to convert a set to a list.
st = {1, 2, 3, 4}
lst = list(st)
print(lst)  # Output: [1, 2, 3, 4] (order may vary)
# - Use Case: When you need an ordered structure.
# - Time Complexity: \( O(n) \).



#  1.5 Set to Tuple
# Use `tuple()` to convert a set to a tuple.
st = {1, 2, 3, 4}
tpl = tuple(st)
print(tpl)  # Output: (1, 2, 3, 4) (order may vary)
# - Use Case: Creating an immutable version of a set.
# - Time Complexity: \( O(n) \).



# 2. Converting Dictionaries to Other Collections

#  2.1 Dictionary Keys to List
# Use `list(dict.keys())` to extract keys as a list.
d = {'a': 1, 'b': 2, 'c': 3}
keys_list = list(d.keys())
print(keys_list)  # Output: ['a', 'b', 'c']
# - Time Complexity: \( O(n) \).



#  2.2 Dictionary Values to List
# Use `list(dict.values())`.
values_list = list(d.values())
print(values_list)  # Output: [1, 2, 3]
# - Time Complexity: \( O(n) \).



#  2.3 Dictionary Items to List of Tuples
# Use `list(dict.items())`.
items_list = list(d.items())
print(items_list)  # Output: [('a', 1), ('b', 2), ('c', 3)]
# - Use Case: When iterating over key-value pairs.
# - Time Complexity: \( O(n) \).



#  2.4 List of Tuples to Dictionary
# Convert a list of `(key, value)` pairs into a dictionary using `dict()`.
lst = [('a', 1), ('b', 2), ('c', 3)]
d = dict(lst)
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}
# - Time Complexity: \( O(n) \).



 # 3. String and Collection Conversions

#  3.1 String to List of Characters
# Use `list()` to break a string into individual characters.
s = "hello"
char_list = list(s)
print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']
# - Use Case: Useful in text processing.
# - Time Complexity: \( O(n) \).



#  3.2 String to List of Words
# Use `.split()` to break a string into words.
s = "hello world"
words = s.split()
print(words)  # Output: ['hello', 'world']
# - Use Case: Tokenizing text.
# - Time Complexity: \( O(n) \).



#  3.3 List of Characters to String
# Use `''.join(list)` to form a string.
char_list = ['h', 'e', 'l', 'l', 'o']
s = ''.join(char_list)
print(s)  # Output: "hello"
# - Time Complexity: \( O(n) \).



#  3.4 List of Words to String
# Use `' '.join(list)`.
words = ['hello', 'world']
s = ' '.join(words)
print(s)  # Output: "hello world"
# - Time Complexity: \( O(n) \).



 # 4. Advanced Conversions

#  4.1 Nested List to Flattened List
# Use `itertools.chain()` for efficient flattening.
from itertools import chain

nested = [[1, 2], [3, 4], [5, 6]]
flat = list(chain(*nested))
print(flat)  # Output: [1, 2, 3, 4, 5, 6]
# - Time Complexity: \( O(n) \).



#  4.2 List to Dictionary with Index as Key
# Use `enumerate()`.
lst = ['a', 'b', 'c']
d = dict(enumerate(lst))
print(d)  # Output: {0: 'a', 1: 'b', 2: 'c'}
# - Time Complexity: \( O(n) \).



#  4.3 Dictionary to JSON String
# Use `json.dumps()`.
import json

d = {'name': 'Alice', 'age': 25}
json_str = json.dumps(d)
print(json_str)  # Output: '{"name": "Alice", "age": 25}'
# - Use Case: Storing data in JSON format.
# - Time Complexity: \( O(n) \).
