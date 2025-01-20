# Strings are sequences of characters, using the syntax of either single  quotes or double quotes:

a= 'hello'
print (a)
print(type(a))
a= "Hello"
print (a)
print(type(a))
a= " I don't do that "
print (a)
print(type(a))

a= "i'm learning python"
print(a)

# Because strings are ordered sequences
# it means we can using indexing and slicing to grab sub-sections of the string

b= 'pythonisamazing'
print(b[0])
print(b[-15]) # it will also result o/p as p
print(b[-1]) # negative indexing -1 means last letter in string

# Slicing allows you to grab a subsection of multiple characters, a “slice” of the string.
# This has the following syntax:
# [start:stop:step]
    # start is a numerical index for the slice start
    # stop is the index you will go up to (but not include)
    # step is the size of the “jump” you take.

# string index starts at 0.
c = 'LearningPython'
print(c[8:]) # it will slice to the end string include character at position 8
print(c[5:9]) #ingP the last index position will not display in the o/p

#we can specify the step size as well
print(c[::2])  # it will print the o/p skipping one value o/p -LannPto

#reverse a string shortcut
print(c[::-1]) #nohtyPgninraeL


# STRING PROPERTIES

#1. Immutable -Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)
name = 'Python'
#name[0]= 'L'  #it's not allowed in Python
#print(name) #TypeError: 'str' object does not support item assignment.

#We can do this by Concatenation
name = 'L' + name
print(name)  #LPython



#index vs find
# index(): Returns the lowest index of the substring if it is found. Raises a ValueError if the substring is not found.
# find(): Also returns the lowest index of the substring if it is found. Returns -1 if the substring is not found



#METHODS
sub= 'Learning Python'
print(sub.upper())  #LEARNING PYTHON
print(sub.lower())   #learning python
print(sub.capitalize())  #Learning python
print(sub[6])  # n index start from 0
print(sub[-1]) #  n it print the last element
print(sub.find("n")) #it will give me the first occurence of n  here o/p is 4
print(sub.find("z")) # it will show -1 when the string is not present.
print(sub.index("n"))  #4
#print(sub.index("z")) # it will throw an error ValueError: substring not found
print(sub.replace("r","x")) #o/p Leaxning python . it wont change thee original value
print(sub[2:5]) #to print the substring, here 2 in inclusive and 5 is exclusive. o/p arn
print(sub[2:]) #o/p arning python
print(sub[:9]) # Learning
print(sub[:]) #Learning python
print(sub.isalnum()) # o/p false
print(sub.isalpha()) # o/p false
print(sub.count("n")) # it shows the total occurences of string  o/p = 3
print(sub.split("n")) # it will split the string based on string provided o/p ['Lear', 'i', 'g pytho', '']
print(sub.split("ing"))# o/p ['Learn', ' python']
print(sub.split()) #o/p it will split based on space ['Learning', 'python']
print(len(sub)) # o/p  15

order = '1,2013-07-25 00:00:00.0,1,CLOSED'
print("month",int(order.split(',')[1][5:7])) # o/p month 7 as we typecast '07' to int so o/p here is 7

s = '    .hello.   '
print ("strip ",s.strip(' ').rstrip('.'))  #strip  .hello




#STRING INTERPOLATION - formatting string
print("I am learning {}".format("Python"))  #I am learning Python

print("The {2} {1} {0}  ".format('fox','brown', 'quick'))    #The quick brown fox

print("The {f} {g} {h}  ".format(f= 'fox',g= 'brown', h= 'quick')) #The fox brown quick

car= 'Nexon'
print(f"the car model is {car}")  #the car model is Nexon
print("the car model is {}".format(car))  #the car model is Nexon

language= 'Python'
level = 'basic'

print(f"This course explain {level} concepts of {language}")  #This course explain basic concepts of Python

brand = "TATA"
model = "NEXON"
year = 2024
price= 15.0
s= "the brand is %s, model is %s, the year  is %d, the price is %f" %(brand,model,year,price)
print (s) # the brand is TATA, model is NEXON, the year  is 2024, the price is 15.000000


#reverse String
s1 = "Learning Python"
print(s1[::-1]) #o/p nohtyP gninraeL

#palindrome
s2= "malayalam"
print("s2 ---> ", s2== s2[::-1])  #s2 --->  True it is case -sensitive .


#STRING COMPARISON
x= "python"
y="python"
z= "Python"
print(x*2)   #pythonpython
print(x==y)  #true
print(x==z)  #false