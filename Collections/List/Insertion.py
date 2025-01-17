# Certainly! Python provides several ways toinsert elements into a list, depending on the position and the number of elements you want to insert. Here's a detailed explanation with examples:
#
#
# 1. `list.append(element)`
# Adds a single element to the end of the list.
# -Use Case: When you want to add an element at the end of the list.
lst = [1, 2, 3]
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]



# 2. `list.insert(index, element)`
# Inserts an element at a specific position in the list.

# -Use Case: When you need to insert an element at a particular index.
# - If the index is out of range, the element is added at the start (for negative indices) or end.
lst = [1, 2, 3]
lst.insert(1, 100)  # Inserts 100 at index 1
print(lst)  # Output: [1, 100, 2, 3]

lst.insert(0, 0)  # Inserts 0 at the start
print(lst)  # Output: [0, 1, 100, 2, 3]

lst.insert(9, 60)  # Inserts 60 at the end
print(lst)  #Output : [0, 1, 100, 2, 3, 60]

# 3. `list.extend(iterable)`
# Extends the list by appending all elements from another iterable (e.g., list, tuple, set, string).

# -Use Case: When you want to add multiple elements to the end of a list.
lst = [1, 2, 3]
lst.extend([4, 5, 6])
print(lst)  # Output: [1, 2, 3, 4, 5, 6]

# Extending with a string
lst.extend("AB")
print(lst)  # Output: [1, 2, 3, 4, 5, 6, 'A', 'B']


# 4. Slice Assignment
# You can use slicing to insert multiple elements at a specific position.

# -Use Case: When you need to insert multiple elements at a specific index.

lst = [1, 2, 5]
lst[2:2] = [3, 4]  # Inserts 3, 4 at index 2
print(lst)  # Output: [1, 2, 3, 4, 5]


# 5. Concatenation (`+`)
# Creates a new list by concatenating the original list with another list.
#
# -Use Case: When you want to create a new list by adding elements.
lst = [1, 2, 3]
new_lst = lst + [4, 5]
print(new_lst)  # Output: [1, 2, 3, 4, 5]


# 6. Using `list comprehensions`
# Insert elements into a new list dynamically.

# -Use Case: When creating a modified version of the list with additional elements.

lst = [1, 2, 3]
new_lst = [x for pair in zip(lst, [10, 20, 30]) for x in pair] + [40]
print(new_lst)  # Output: [1, 10, 2, 20, 3, 30, 40]



# 8. Using `deque` (from `collections` module)
# Forefficient inserts at both ends of a list, consider using a `deque`.
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)  # Insert at the end
dq.appendleft(0)  # Insert at the beginning
print(list(dq))  # Output: [0, 1, 2, 3, 4]



# 9. Inserting Elements in a Sorted List
# For inserting elements in a sorted manner, use `bisect.insort()`.
#
# -Use Case: When working with sorted lists.

import bisect

lst = [1, 3, 4, 7]
bisect.insort(lst, 5)  # Inserts 5 in the correct sorted position
print(lst)  # Output: [1, 3, 4, 5, 7]



# 10. Using `itertools.chain()`
# Chain multiple lists or elements into a single list.

# -Use Case: Combine multiple iterables into a list.

from itertools import chain

lst1 = [1, 2]
lst2 = [3, 4]
new_lst = list(chain(lst1, [100], lst2))
print(new_lst)  # Output: [1, 2, 100, 3, 4]
