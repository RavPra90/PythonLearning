# Tuples in Python are immutable, ordered collections of items.
# They are commonly used for grouping related data. Below, we cover both basic and advanced concepts with code examples.

#   Creating a Tuple
# Tuples are defined using parentheses `()`.
# Empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# Single element tuple (comma is mandatory)
single_element = (42,)
print(single_element)  # Output: (42,)

# Multiple elements
multi_element = (1, 2, 3)
print(multi_element)  # Output: (1, 2, 3)

# Without parentheses (tuple packing)
packed_tuple = 1, 2, 3
print(packed_tuple)  # Output: (1, 2, 3)



# Accessing Elements
# You can use indexing and slicing, similar to lists.
t = (10, 20, 30, 40, 50)

# Access by index
print(t[0])  # Output: 10
print(t[-1])  # Output: 50

# Slicing
print(t[1:4])  # Output: (20, 30, 40)



# Tuple Unpacking
# You can assign tuple elements to variables directly.
t = (1, 2, 3)

# Unpacking
a, b, c = t
print(a, b, c)  # Output: 1 2 3

# Partial unpacking
t = (10, 20, 30, 40)
a, *b = t
print(a)  # Output: 10
print(b)  # Output: [20, 30, 40]



# Immutable Nature
# Tuples cannot be modified after creation.
t = (1, 2, 3)
# t[0] = 10  # Error: 'tuple' object does not support item assignment



# Membership and Iteration
t = (1, 2, 3, 4)

# Check membership
print(2 in t)  # Output: True
print(5 in t)  # Output: False

# Iteration
for item in t:
    print(item, end=" ")  # Output: 1 2 3 4


# Basic operations
mixed_tuple = (1, "hello", 3.14, True)
print(len(mixed_tuple))       #Output :4
print("hello" in mixed_tuple)     #Output :True
print(mixed_tuple.index("hello"))     #Output :1
print(mixed_tuple.count(1))    #Output :2