# a. Reverse a String
string = "Python"
reversed_string = string[::-1]
print(reversed_string)  # Output: nohtyP


# b. Check if a String is a Palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Ignore case and spaces
    return s == s[::-1]

print(is_palindrome("Madam"))       # Output: True
print(is_palindrome("Hello"))       # Output: False


# #STRING INTERPOLATION - formatting string
print("I am learning {}".format("Python"))  #I am learning Python

print("The {2} {1} {0}  ".format('fox','brown', 'quick'))    #The quick brown fox

print("The {f} {g} {h}  ".format(f= 'fox',g= 'brown', h= 'quick')) #The fox brown quick


name = "John"
age = 30

# Old style
print("My name is %s and I am %d years old." % (name, age))

# str.format() method
print("My name is {} and I am {} years old.".format(name, age))

# f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")



# d. Removing Characters
string = "Hello, World!"

# Remove specific characters
cleaned = string.replace(",", "").replace("!", "")
print(cleaned)  # Output: Hello World

# Remove vowels
no_vowels = "".join([char for char in string if char.lower() not in "aeiou"])
print(no_vowels)  # Output: Hll, Wrld!




# e. Frequency of Characters
from collections import Counter

string = "abracadabra"
frequency = Counter(string)
print(frequency)  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})



# f. Generate Random Strings
import random
import string

# Generate a random string of length 10
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
print(random_string)



# g. Encode and Decode Strings
string = "Hello, Python!"

# Encoding to bytes
encoded = string.encode("utf-8")
print(encoded)  # Output: b'Hello, Python!'

# Decoding to string
decoded = encoded.decode("utf-8")
print(decoded)  # Output: Hello, Python!



# h. Removing Duplicates (Order-Preserving)
string = "abracadabra"
unique_chars = "".join(dict.fromkeys(string))
print(unique_chars)  # Output: abrcd




#String Iteration
string = "Python"
for char in string:
    print(char, end=" ")  # Output: P y t h o n




#Handling Multi-Line Strings
#We can use the method splitlines() in string class to split at newlines
multi_line =  """This is a
multi-line
string."""
lines = multi_line.splitlines()
print(lines)  # Output: ['This is a', 'multi-line', 'string.']


order = '1,2013-07-25 00:00:00.0,1,CLOSED'
print("month",int(order.split(',')[1][5:7])) # o/p month 7 as we typecast '07' to int so o/p here is 7


#STRING COMPARISON
x= "python"
y="python"
z= "Python"
print(x*2)   #pythonpython
print(x==y)  #true
print(x==z)  #false


#Case Folding (For Case-Insensitive Matching)
string1 = "Python"
string2 = "PYTHON"

# Case-insensitive comparison
print(string1.casefold() == string2.casefold())  # Output: True


#String Compression Using zlib
#Compressing strings can be useful when dealing with large text data.
import zlib

text = "This is a long string that we want to compress." * 10

# Compress
compressed = zlib.compress(text.encode())
print(f"Compressed size: {len(compressed)}")

# Decompress
decompressed = zlib.decompress(compressed).decode()
print(f"Decompressed text: {decompressed}")


#String Deduplication (Removing Duplicates)

text = "programming"

# Remove duplicates while preserving order
unique_chars = "".join(dict.fromkeys(text))
print(unique_chars)  # Output: progamin



#Efficient Substring Search with in and find()

text = "Python programming is fun."

# Check if a substring exists
if "programming" in text:
    print("Substring found!")

# Get the index of the substring
index = text.find("programming")
print(index)  # Output: 7

#String Parsing with ast.literal_eval
#Convert strings representing Python objects into actual Python objects.
import ast

# Convert string representation of a list to an actual list
list_string = "[1, 2, 3, 4]"
parsed_list = ast.literal_eval(list_string)
print(parsed_list)  # Output: [1, 2, 3, 4]
print(type(parsed_list))   #Output  : <class 'list'>

#using ast we can convert strings to collection. here it is converting it to dictionary
import ast
x = ast.literal_eval("{'foo' : 'bar', 'hello' : 'world'}")
print(type(x)) #Output :<type'dict'>


#we can also use json.loads to convert string to dictionary
import json
x = json.loads("{'foo' : 'bar', 'hello' : 'world'}")
print(type(x))    #Output : <type'dict'>



#check if the string is empty in Python?
string = ""
if not string:
    print("Empty String!")  #Output : Empty String!


#concatenate str and integer
str4 = "Python"
num = 3
print (str4 + str(num))  #Output : Python3