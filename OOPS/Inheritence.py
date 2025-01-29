"""
Inheritance is a core feature of object-oriented programming (OOP) in Python.
It allows one class (child or derived class) to inherit attributes and methods from another class (parent or base class).
This promotes reusability and reduces redundancy.

"""

# Single Inheritance
#A single child class inherits from a single parent class.

# Parent class
class Animal:
    def speak(self):
        print("I am an animal.")

# Child class
class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Woof! Woof!")

# Create an instance of Dog
dog = Dog()
dog.speak()  # Output: I am an animal. (inherited from Animal)
dog.bark()   # Output: Woof! Woof!



#Multilevel Inheritance
#In multilevel inheritance, a child class inherits from a parent class, and then another child class inherits from that child class.

class Animal:
    def speak(self):
        print("I am an animal.")

class Mammal(Animal):  # Mammal inherits from Animal
    def has_hair(self):
        print("I have hair.")

class Dog(Mammal):  # Dog inherits from Mammal
    def bark(self):
        print("Woof! Woof!")

# Create an instance of Dog
dog = Dog()
dog.speak()    # Output: I am an animal. (inherited from Animal)
dog.has_hair() # Output: I have hair. (inherited from Mammal)
dog.bark()     # Output: Woof! Woof!



#Multiple Inheritance
#In multiple inheritance, a child class can inherit from more than one parent class.

class Flyer:
    def fly(self):
        print("I can fly.")

class Swimmer:
    def swim(self):
        print("I can swim.")

class Duck(Flyer, Swimmer):  # Duck inherits from Flyer and Swimmer
    def quack(self):
        print("Quack! Quack!")

# Create an instance of Duck
duck = Duck()
duck.fly()   # Output: I can fly.
duck.swim()  # Output: I can swim.
duck.quack() # Output: Quack! Quack!



#Overriding Methods
#A child class can override methods defined in the parent class to provide a specific implementation.

class Animal:
    def speak(self):
        print("I make generic sounds.")

class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")  # Overriding the parent class method

# Create instances
animal = Animal()
cat = Cat()

animal.speak()  # Output: I make generic sounds.
cat.speak()     # Output: Meow! Meow!



# Using `super()`
#The `super()` function is used to call a method from the parent class.

class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)  # Call the parent class's constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Call the parent class's method
        print(f"I am a {self.breed} dog.")

# Create an instance of Dog
dog = Dog("Mammal", "Golden Retriever")
dog.speak()
# Output:
# I am an animal.
# I am a Golden Retriever dog.




#Diamond Problem and Method Resolution Order (MRO)
#The diamond problem arises in multiple inheritance. Python resolves it using the C3 linearization algorithm (MRO).

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):  # D inherits from both B and C
    pass

d = D()
d.greet()  # Output: Hello from B (MRO prioritizes B over C)
print(D.mro())  # Output: [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]



#Private and Protected Attributes in Inheritance
"""
- Protected Attributes: Can be accessed in child classes but not outside.
- Private Attributes: Cannot be directly accessed by child classes.
"""
class Animal:
    def __init__(self):
        self._protected_attr = "I am protected"
        self.__private_attr = "I am private"

class Dog(Animal):
    def show_attributes(self):
        print(self._protected_attr)  # Accessible
        # print(self.__private_attr) # AttributeError: 'Animal' object has no attribute '__private_attr'

dog = Dog()
dog.show_attributes()       # Output: I am protected
print(dog._protected_attr)  # Output: I am protected
# print(dog.__private_attr) # AttributeError
