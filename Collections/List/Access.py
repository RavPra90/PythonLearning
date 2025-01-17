# Certainly! Here are the different ways to access elements from a list in Python,
# along with code snippets for better understanding:

#  1. Access by Index
# You can access elements in a list using their index. Indexing starts from `0` for the first element.
lst = [10, 20, 30, 40, 50]

# Accessing elements by index
print(lst[0])  # Output: 10 (first element)
print(lst[3])  # Output: 40 (fourth element)

# - Negative Indexing: Access elements from the end of the list.
print(lst[-1])  # Output: 50 (last element)
print(lst[-2])  # Output: 40 (second last element)


#  2. Access by Slicing
# Slicing allows you to extract a portion (sublist) of a list.
lst = [10, 20, 30, 40, 50]

# Slice syntax: lst[start:end:step]
print(lst[1:4])   # Output: [20, 30, 40] (from index 1 to 3)
print(lst[:3])    # Output: [10, 20, 30] (from start to index 2)
print(lst[2:])    # Output: [30, 40, 50] (from index 2 to end)
print(lst[::2])   # Output: [10, 30, 50] (every second element)
print(lst[::-3])  # Output: [10, 20, 30] (from start to index 1)
print(lst[::-1])  # Output: [50, 40, 30, 20, 10] (reverse the list)


#  3. Using a `for` Loop
# You can iterate through the list using a `for` loop.
lst = [10, 20, 30, 40, 50]

for element in lst:
    print(element)
# Output:
# 10
# 20
# 30
# 40
# 50

#  4. Using `enumerate()`
# `enumerate()` allows you to access both the index and the value of each element.
lst = [10, 20, 30, 40, 50]

for index, value in enumerate(lst):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: 10
# Index: 1, Value: 20
# Index: 2, Value: 30
# Index: 3, Value: 40
# Index: 4, Value: 50




#  5. Using List Comprehension
# You can access elements or even transform them in one line using list comprehension.
lst = [10, 20, 30, 40, 50]

# Accessing and creating a new list
squared = [x**2 for x in lst]
print(squared)  # Output: [100, 400, 900, 1600, 2500]


#  6. Access Using `zip()`
# You can pair multiple lists using `zip()` and access elements together.
lst1 = [10, 20, 30]
lst2 = ['A', 'B', 'C']

for num, char in zip(lst1, lst2):
    print(f"Number: {num}, Character: {char}")
# Output:
# Number: 10, Character: A
# Number: 20, Character: B
# Number: 30, Character: C


#  7. Access Using a Function (`map()`)
# You can apply a function to all elements using `map()`.
lst = [10, 20, 30, 40, 50]

# Doubling each element in the list
doubled = list(map(lambda x: x * 2, lst))
print(doubled)  # Output: [20, 40, 60, 80, 100]


# 8. Nested List Access
# For nested lists, use multiple indices to access inner elements.
nested_list = [[1, 2], [3, 4], [5, 6]]

# Access the first inner list
print(nested_list[0])  # Output: [1, 2]

# Access the first element of the first inner list
print(nested_list[0][0])  # Output: 1
