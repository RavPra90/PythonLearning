# Set Operations

# a. Union
# Combines elements from two sets.
a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(a | b)        # Output: {1, 2, 3, 4, 5}
print(a.union(b))   # Output: {1, 2, 3, 4, 5}

# b. Intersection
# Finds common elements.
print(a & b)         # Output: {3}
print(a.intersection(b))  # Output: {3}

# c. Difference
# Finds elements in one set but not the other.
print(a - b)         # Output: {1, 2}
print(a.difference(b))  # Output: {1, 2}


# d. Symmetric Difference
# Finds elements in either set, but not both.
print(a ^ b)         # Output: {1, 2, 4, 5}
print(a.symmetric_difference(b))  # Output: {1, 2, 4, 5}




# Subsets and Supersets
a = {1, 2, 3}
b = {1, 2}

# Check if `b` is a subset of `a`
print(b.issubset(a))  # Output: True

# Check if `a` is a superset of `b`
print(a.issuperset(b))  # Output: True




# Frozen Sets (Immutable Sets)
# A `frozenset` is an immutable version of a set.
fs = frozenset([1, 2, 3])
print(fs)  # Output: frozenset({1, 2, 3})

# Immutable nature
# fs.add(4)  # Error: 'frozenset' object has no attribute 'add'




# Removing Duplicates from a List
# Sets can be used to remove duplicates from a list.
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)  # Output: [1, 2, 3, 4, 5] (order may vary)




# Set Comprehension
# You can create sets using comprehensions.
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)  # Output: {1, 4, 9, 16, 25}




# Finding Common Items Between Two Lists
# Use set intersection for efficient common element retrieval.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)
print(common)  # Output: {3, 4}



#  Efficient Membership Testing
# Sets are optimized for membership testing due to their hash-based implementation.
large_set = set(range(1, 1000000))
print(999999 in large_set)  # Output: True (fast lookup)




# Using Sets with `zip()`
# Create unique pairs using sets.
names = ["Alice", "Bob", "Alice"]
scores = [90, 85, 90]

unique_pairs = set(zip(names, scores))
print(unique_pairs)  # Output: {('Alice', 90), ('Bob', 85)}




# Advanced Filtering
# Remove elements from a set based on conditions.
s = {1, 2, 3, 4, 5, 6}

# Remove even numbers
filtered = {x for x in s if x % 2 != 0}
print(filtered)  # Output: {1, 3, 5}




#  Using `reduce()` for Set Operations
# Combine multiple sets using `reduce` from `functools`.
from functools import reduce

sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
common = reduce(lambda x, y: x & y, sets)
print(common)  # Output: {3}




#  Comparing Two Sets
# Check if two sets are disjoint or identical.
a = {1, 2, 3}
b = {4, 5, 6}

# Check if sets are disjoint
print(a.isdisjoint(b))  # Output: True

# Check equality
print(a == b)  # Output: False




#  Set Operations with Multiple Sets
# Python supports chaining of set operations.
a = {1, 2, 3}
b = {3, 4}
c = {4, 5}

result = a | b | c  # Union
print(result)  # Output: {1, 2, 3, 4, 5}



# Set Mutation Methods
# Modify sets in-place with methods like `update()` or `intersection_update()`.
a = {1, 2, 3}
b = {2, 3, 4}

# Update with union
a.update(b)
print(a)  # Output: {1, 2, 3, 4}

# In-place intersection
a.intersection_update(b)
print(a)  # Output: {2, 3, 4}

