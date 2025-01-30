"""
Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:

{'a': 1, 'b': 5, 'c': 7, 'd': 5}

"""
def merge_dicts(dict1, dict2):

    merged_dict = {}

    # Get all unique keys from both dictionaries
    all_keys = set(dict1.keys()).union(set(dict2.keys()))

    # Iterate over each unique key
    for key in all_keys:
        # Get the value from dict1 if key exists, otherwise use 0
        value1 = dict1.get(key, 0)

        # Get the value from dict2 if key exists, otherwise use 0
        value2 = dict2.get(key, 0)

        # Store the sum of values in the merged dictionary
        merged_dict[key] = value1 + value2

    return merged_dict


# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

result = merge_dicts(dict1, dict2)
print(result)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}


"""
Key with the Highest Value
Define a function which takes a dictionary as a parameter 
and returns the key with the highest value in a dictionary.

Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output:

b

"""
my_dict = {'a': 5, 'b': 9, 'c': 2}
# sort the dict by values
all_values = dict(sorted(my_dict.items(), key=lambda x: x[1]))
#to get the last key in sorted dict
last_key = next(reversed(all_values.keys()))
print(last_key)

#using pred-deined  max func
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)





my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filterd_dict = {k:v for k,v in my_dict.items() if v%2 ==0}
print(filterd_dict)


