# WARNING: This is a common mistake
def add_to_list(item, my_list=[]):
    """
    This function demonstrates the tricky behavior of mutable default arguments.
    The empty list is created only once when the function is defined!
    """
    my_list.append(item)
    return my_list

print(add_to_list(1))  # Output: [1]
print(add_to_list(2))  # Output: [1, 2] - Surprise! The list persisted!

# The correct way to handle this
def add_to_list_fixed(item, my_list=None):
    """
    This is the proper way to handle mutable default arguments.
    Create the list inside the function if None is provided.
    """
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_to_list_fixed(1)) # Output: [1]
print(add_to_list_fixed(2))  # Output: [2] - Each call gets a fresh list