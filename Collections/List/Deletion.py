# In Python, there are several ways to remove elements from a list, depending on the use case. Here's a detailed explanation of the different methods:

# 1. `list.remove(element)
# Removes the first occurrence of a specific element from the list.
# - Use Case: When you know the element you want to remove (by value).
# - Raises Error: If the element does not exist in the list.
lst = [1, 2, 3, 2, 4]
lst.remove(2)  # Removes the first occurrence of 2
print(lst)  # Output: [1, 3, 2, 4]


# 2. `list.pop(index)
# Removes the element at the specified index and returns it.
# If no index is specified, it removes and returns the last element.
# - Use Case: When you want to remove an element by its position.
# - Raises Error: If the index is out of range.
lst = [1, 2, 3, 4]
print(lst.pop())  #returns the last element 4
removed = lst.pop(1)  # Removes element at index 1
print(lst)  # Output: [1, 3, 4]
print(removed)  # Output: 2


# 3. `del list[index]
# Deletes an element at the specified index or slices of elements.
# - Use Case: When you don't need to capture the removed element.
lst = [1, 2, 3, 4]
del lst[2]  # Deletes element at index 2
print(lst)  # Output: [1, 2, 4]

# Deleting a slice of elements
lst = [1, 2, 3, 4, 5]
del lst[1:3]  # Deletes elements at index 1 and 2
print(lst)  # Output: [1, 4, 5]


# 4. `list.clear()
# Removes all elements from the list, making it empty.
# - Use Case: When you want to completely empty the list.
lst = [1, 2, 3, 4]
lst.clear()
print(lst)  # Output: []


# 5. List Comprehension
# Removes elements based on a condition (creates a new list).
# - Use Case: When you want to filter out specific elements.
lst = [1, 2, 3, 4, 5]
lst = [x for x in lst if x != 3]  # Removes all occurrences of 3
print(lst)  # Output: [1, 2, 4, 5]


# 6. `filter()` Function
# Uses a filtering condition to remove elements and returns an iterator.
# - Use Case: Similar to list comprehension, but more functional.
lst = [1, 2, 3, 4, 5]
lst = list(filter(lambda x: x != 3, lst))  # Removes all occurrences of 3
print(lst)  # Output: [1, 2, 4, 5]


# 7. Remove Duplicates Using `set
# Converts the list to a `set` (which removes duplicates) and back to a list.
# - Use Case: When you want to remove all duplicate elements.
lst = [1, 2, 2, 3, 4, 4]
lst = list(set(lst))  # Removes duplicates
print(lst)  # Output: [1, 2, 3, 4] (order may vary)


# 8. Slicing
# Creates a new list with desired elements, effectively "removing" the others.
# - Use Case: To remove elements by slicing and keeping others.
lst = [1, 2, 3, 4]
lst = lst[:2] + lst[3:]  # Removes the element at index 2
print(lst)  # Output: [1, 2, 4]

