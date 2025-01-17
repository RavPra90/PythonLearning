# Nested Tuples
# Tuples can contain other tuples or data structures.
from collections import namedtuple

nested = (1, (2, 3), (4, (5, 6)))
print(nested[1])  # Output: (2, 3)
print(nested[2][1][1])  # Output: 6


#Using Tuples as Keys in Dictionaries
# Since tuples are immutable, they can be used as dictionary keys.
coordinates = {(1, 2): "A", (3, 4): "B"}
print(coordinates[(1, 2)])  # Output: A



#Tuple Comprehension with `zip()`
# Tuples cannot be directly created using comprehensions, but you can use `zip()` to create tuples.
# Using zip
keys = ("name", "age", "city")
values = ("Alice", 25, "New York")

zipped = tuple(zip(keys, values))
print(zipped)  # Output: (('name', 'Alice'), ('age', 25), ('city', 'New York'))



#  Counting and Indexing
# Tuples have two built-in methods: `count()` and `index()`
t = (1, 2, 2, 3, 3, 3)

# Count occurrences
print(t.count(3))  # Output: 3

# Find the index of the first occurrence
print(t.index(2))  # Output: 1


# Tuple Concatenation and Repetition
# Tuples can be concatenated or repeated.
t1 = (1, 2)
t2 = (3, 4)

# Concatenation
result = t1 + t2
print(result)  # Output: (1, 2, 3, 4)

# Repetition
print(t1 * 3)  # Output: (1, 2, 1, 2, 1, 2)



# Tuple Sorting
# Tuples themselves cannot be sorted, but you can sort the elements to create a new tuple.
t = (4, 1, 3, 2)

# Sort elements
sorted_t = tuple(sorted(t))
print(sorted_t)  # Output: (1, 2, 3, 4)



# Advanced Unpacking
# Unpacking with arbitrary-length components using `*`.
t = (1, 2, 3, 4, 5)

a, b, *c = t
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: [3, 4, 5]

# Nested unpacking
nested = (1, (2, 3))
x, (y, z) = nested
print(x, y, z)  # Output: 1 2 3





# Checking for Tuple Immutability with `id()`
# Tuples are immutable, but if they contain mutable elements, the content can change.
t = (1, [2, 3], 4)
print(id(t[1]))  # ID of the list

t[1].append(5)
print(t)         # Output: (1, [2, 3, 5], 4)
print(id(t[1]))  # Same ID, showing list mutation




# Tuple as Return Values
# Tuples are often used to return multiple values from functions.
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([4, 7, 1, 9])
print(result)  # Output: (1, 9)

# Tuple unpacking
min_val, max_val = result
print(min_val, max_val)  # Output: 1 9




# Tuple as Data Structure (Named Tuples):
# pythonCopy from collections import namedtuple

# Creating a named tuple class
Person = namedtuple('Person', ['name', 'age', 'city'])

# Creating instances
person1 = Person('Alice', 30, 'New York')
person2 = Person('Bob', 25, 'San Francisco')

# Accessing fields
print(person1.name)  # Using dot notation   Alice
print(person1[0])    # Using index     Alice

# Converting to dictionary
person_dict = person1._asdict()
print(person_dict)    #Output : {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Creating new instance with updated values
person1_updated = person1._replace(age=31)
print(person1_updated)        #Output : Person(name='Alice', age=31, city='New York')

