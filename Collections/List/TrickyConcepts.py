# Here are some tricky concepts and advanced methods
# related to Python lists that showcase their flexibility and powerful functionalities:


# 1. Negative Indexing
# - Access elements from the end of the list using negative indices.
lst = [1, 2, 3, 4, 5]
print(lst[-1])  # Output: 5 (last element)
print(lst[-2])  # Output: 4 (second last element)


# 2. Nested Lists (Multidimensional Lists)
# - Python lists can contain other lists, enabling multidimensional data structures.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(matrix[0][1])  # Output: 2 (row 1, column 2)

# Flattening a nested list
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 3. List Comprehension with Conditions
# - A compact way to create or modify lists using if conditions.
# Create a list of squares of even numbers
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]

# Filter and modify elements
words = ["apple", "banana", "cherry"]
filtered = [word.upper() for word in words if "a" in word]
print(filtered)  # Output: ['APPLE', 'BANANA']


# 4. List Slicing
# - Extract sublists or manipulate lists using slicing.
lst = [0, 1, 2, 3, 4, 5]
print(lst[1:4])  # Output: [1, 2, 3] (elements at indices 1 to 3)

# Reverse the list
print(lst[::-1])  # Output: [5, 4, 3, 2, 1, 0]

"""
    lst[start:end] = ... replaces the elements in the range [start:end] with the new elements.
    If start == end, the slice is empty, so the assignment inserts the new elements 
        instead of replacing anything.
    lst[2:2] is a slice that starts and ends at the same index (2), 
        meaning it selects an empty slice at that position.
    Assigning a list to an empty slice effectively inserts the new elements at 
        that position without replacing any existing elements.

"""
# Replace a slice
lst[2:4] = [9, 8]
print(lst)   # Output: [0, 1, 9, 8, 4, 5]
lst[2:2] = [2, 7]    #It will insert the list at given pos Output [0, 1, 2, 7, 9, 8, 4, 5]
print(lst)


# 5. Unpacking a List
# - Python allows you to unpack list elements into variables.
# Simple unpacking
lst = [1, 2, 3]
a, b, c = lst
print(a, b, c)  # Output: 1 2 3

# Using * for remaining elements
lst = [1, 2, 3, 4, 5]
a, *b, c = lst
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5



# 6. Using `zip()` for Pairing
# - Combine elements from two or more lists.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = list(zip(list1, list2))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzipping
unzipped = list(zip(*zipped))
print(unzipped)  # Output: [(1, 2, 3), ('a', 'b', 'c')]


# 7. Removing Duplicates While Preserving Order
# - Use `dict.fromkeys()` to remove duplicates and retain order.

"""
    dict.fromkeys(iterable) creates a dictionary where the keys are taken from the given iterable, 
            and the values are set to None by default.
    In Python dictionaries, keys are unique. If duplicate keys are encountered in the input, 
            they are automatically ignored, keeping only the first occurrence of each key.
    Starting from Python 3.7, dictionaries maintain the insertion order of their keys. 
        This means that the order in which keys are added to the dictionary is the same order 
        in which they will appear when iterating over the dictionary.
    By using dict.fromkeys(lst), the duplicates are removed (because keys are unique),
        and the original order of the elements in lst is preserved.

"""

lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(dict.fromkeys(lst))
print(unique)  # Output: [1, 2, 3, 4, 5]



# 8. Rotating a List
# - Rotate a list by slicing and concatenating.
lst = [1, 2, 3, 4, 5]

# Rotate left by 2
rotated_left = lst[2:] + lst[:2]
print(rotated_left)  # Output: [3, 4, 5, 1, 2]

# Rotate right by 2
rotated_right = lst[-2:] + lst[:-2]
print(rotated_right)  # Output: [4, 5, 1, 2, 3]



# 9. Using `any()` and `all()`
# - Check conditions for elements in a list.
lst = [1, 2, 3, 4]

# Check if any element is greater than 3
print(any(x > 3 for x in lst))  # Output: True

# Check if all elements are positive
print(all(x > 0 for x in lst))  # Output: True



# 10. Using `bisect` for Sorted List Insertion
# - Insert elements into a sorted list while maintaining order.
import bisect

lst = [1, 3, 4, 7]
bisect.insort(lst, 5)  # Insert 5 in sorted order
print(lst)  # Output: [1, 3, 4, 5, 7]



# 12. Using `collections.Counter` for Frequency
# - Count occurrences of elements in a list.
from collections import Counter
lst = [1, 2, 2, 3, 3, 3]
freq = Counter(lst)
print(freq)  # Output: Counter({3: 3, 2: 2, 1: 1})


# 13. Multiply Lists Using `*` Operator
# - Duplicate elements in a list.
lst = [1, 2, 3]
multiplied = lst * 3
print(multiplied)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]



# 14. Finding the Second Largest Element
# - A tricky way to find the second largest in a list.
lst = [3, 1, 4, 4, 5, 2, 5]
second_largest = sorted(set(lst))[-2]
print(second_largest)  # Output: 4



# 15. Finding Common Elements Between Two Lists
# - Use `set` intersection to find common elements.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common)  # Output: [3, 4]



# 16. Generate List of Indices for Specific Values
# - Get indices of all occurrences of a specific value.
lst = [1, 2, 3, 2, 4, 2]
indices = [i for i, x in enumerate(lst) if x == 2]
print(indices)  # Output: [1, 3, 5]


# 17. Zipping and Summing Lists
# - Combine elements of two lists and sum their corresponding elements.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

summed = [x + y for x, y in zip(list1, list2)]
print(summed)  # Output: [5, 7, 9]