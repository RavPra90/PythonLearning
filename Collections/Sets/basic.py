# Sets in Python are unordered collections of unique elements. They are mutable and are widely used when membership testing, uniqueness, or set operations are needed. Below is a detailed explanation of both basic and advanced set concepts with code examples.


# Creating a Set
# A set is created using `{}` or the `set()` function. Duplicate elements are automatically removed.
# Creating sets
set1 = {1, 2, 3, 4, 5}
print(set1)  # Output: {1, 2, 3, 4, 5}

# Using the set() function
set2 = set([1, 2, 2, 3])
print(set2)  # Output: {1, 2, 3}

# Empty set (use set(), not {})
empty_set = set()
print(empty_set)  # Output: set()


# Adding and Removing Elements
s = {1, 2, 3}

# Adding elements
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

# Removing elements
s.remove(3)  # Raises KeyError if element doesn't exist
print(s)  # Output: {1, 2, 4}

# Discarding elements (no error if element doesn't exist)
s.discard(5)
print(s)  # Output: {1, 2, 4}

# Removing and returning an arbitrary element
removed = s.pop()
print(removed)  # Output: 1 (or another element, as sets are unordered)
print(s)        # Remaining set



 # Membership Testing
s = {1, 2, 3, 4}
print(2 in s)   # Output: True
print(5 in s)   # Output: False



 # Iterating Over a Set
s = {1, 2, 3}
for elem in s:
    print(elem, end=" ")  # Output: 1 2 3 (order may vary)

