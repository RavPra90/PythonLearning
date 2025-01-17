# Python lists are one of the most versatile data structures,
# and they come with several built-in methods that allow us to manipulate and process
# the list effectively.
# Below are the common methods used in Python lists, along with explanations and code snippets:

# 1. `append()`
# Adds a single element to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]


# 2. `extend()`
# Extends the list by appending elements from another iterable (e.g., list, tuple).
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]


# 3. `insert()`
# Inserts an element at a specified position.
my_list = [1, 2, 4]
my_list.insert(2, 3)  # Insert 3 at index 2
print(my_list)  # Output: [1, 2, 3, 4]


# 4. `remove()`
# Removes the first occurrence of a specified value.
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)  # Removes the first occurrence of 2
print(my_list)  # Output: [1, 3, 2, 4]


# 5. `pop()`
# Removes and returns the element at the specified index. Defaults to the last element if no index is specified.
my_list = [1, 2, 3, 4]
popped = my_list.pop(2)  # Removes and returns the element at index 2
print(popped)  # Output: 3
print(my_list)  # Output: [1, 2, 4]


# 6. `clear()`
# Removes all elements from the list.
my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)  # Output: []



# 7. `index()`
# Returns the index of the first occurrence of a specified value.
my_list = [1, 2, 3, 4, 3]
index = my_list.index(3)
print(index)  # Output: 2


# 8. `count()`
# Returns the number of occurrences of a specified value.
my_list = [1, 2, 2, 3, 4, 2]
count = my_list.count(2)
print(count)  # Output: 3


# 9. `sort()`
# Sorts the list in ascending order (in-place).
my_list = [4, 2, 1, 3]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]


#To sort in descending order:
my_list.sort(reverse=True)
print(my_list)  # Output: [4, 3, 2, 1]

#we can also use sorted to sort the list
lst1 = sorted(my_list)
print(lst1)

lst2 = sorted(my_list , reverse=True)
print(lst2)

#The main difference between sort and sorted in Python is that sort function returns nothing and
#makes changes to the original sequence,
#while the sorted () function creates a new sequence type containing a sorted version of the given sequence

# 10. `reverse()`
# Reverses the elements of the list (in-place).
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]

# 11. `copy()`
# Returns a shallow copy of the list.
my_list = [1, 2, 3]
copied_list = my_list.copy()
print(copied_list)  # Output: [1, 2, 3]


# 12. `len()`
# Returns the number of elements in the list (not a method but a built-in function).
my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4


# 13. `list()`
# Used to create a new list from an iterable.
new_list = list(range(5))  # Creates a list from range
print(new_list)  # Output: [0, 1, 2, 3, 4]



# 14. List Comprehension (not a method but widely used with lists)
# Creates a new list by processing each element in an iterable.
squared_list = [x**2 for x in range(5)]
print(squared_list)  # Output: [0, 1, 4, 9, 16]



#Example: Combining Methods
my_list = [3, 1, 4]
my_list.append(2)
my_list.sort()
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]

import random as r
x= [1,2,3,4,5,6,7,8]
print(r.sample(x,4)) # it will print random 4 values from a list in a form of list
#note : o/p of sample is always a list
print(r.sample(range(1,100),3))  # Output : [35, 20, 66]


#1. “in” operator :- This operator is used to check if an element is present in the list or not.
# Returns true if element is present in list else returns false.
num = [1,2,3,4,5]
if(2 in num):
    print("elemnet is in the lsit")

#2. “not in” operator :- This operator is used to check if an element is not present in the list or not.
# Returns true if element is not present in list else returns false.

if(8 not in num):
    print("elemnet not in the list ")
else :
    print("elemnet in the list ")
