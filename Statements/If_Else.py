# Basic if statement
age = 18

# Simple if condition
if age >= 18:
    print("You are an adult")  # This line is indented and part of the if block

# If-else statement
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If-elif-else chain for multiple conditions
if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")

# IF with logical operators:

# Using logical operators (and, or, not)
username = "admin"
password = "secure123"

if username == "admin" and password == "secure123":
    print("Access granted")
else:
    print("Access denied")

# Using 'or' operator
if age < 13 or age >= 65:
    print("You get a discount")

# Using 'not' operator
is_holiday = True
if not is_holiday:
    print("Time to work!")


# Nested if statements
def check_eligibility(age, has_license, has_insurance):
    if age >= 18:
        if has_license:
            if has_insurance:
                print("You can rent a car")
            else:
                print("Please get insurance first")
        else:
            print("Please get a license first")
    else:
        print("You must be 18 or older")


# The same logic written more elegantly using compound conditions
def check_eligibility_improved(age, has_license, has_insurance):
    if age >= 18 and has_license and has_insurance:
        print("You can rent a car")
    else:
        if age < 18:
            print("You must be 18 or older")
        elif not has_license:
            print("Please get a license first")
        else:
            print("Please get insurance first")


# Ternary operator (conditional expressions)
# Traditional if-else
status = ""
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator equivalent
status = "adult" if age >= 18 else "minor"

# Chaining ternary operators (though this can reduce readability)
message = "child" if age < 13 else "teen" if age < 18 else "adult"


# Using if conditions with data structures
def get_discount_percentage(age, is_student, is_veteran):
    discounts = {
        'age': 20 if age >= 65 else (15 if age <= 12 else 0),
        'student': 10 if is_student else 0,
        'veteran': 15 if is_veteran else 0
    }
    return max(discounts.values())  # Returns the highest applicable discount


# Checking Membership
# Use in and not in to test for membership in sequences like lists or strings.
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Apple is available")  # Output: Apple is available

# Advanced Membership Check
# Use sets for faster membership testing in large datasets.
large_list = range(1, 1000000)
search_set = set(large_list)  # Convert to set for faster lookup

if 999999 in search_set:
    print("Found it!")  # Output: Found it!


# Using is for Identity Comparison
# Checks if two objects are the same.
x = None
if x is None:
    print("x is None")  # Output: x is None

# Using Functions in Conditions
# Call functions to evaluate conditions.
def is_even(n):
    return n % 2 == 0

if is_even(10):
    print("Number is even")  # Output: Number is even

# Conditional Assignment in a Loop
# Use if-else inside a loop for dynamic conditions.
    nums = [1, 2, 3, 4, 5]
results = ["Even" if n % 2 == 0 else "Odd" for n in nums]
print(results)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Using any() and all() in Conditions
# Evaluate multiple conditions at once.
nums = [10, 20, 30]
if all(n > 5 for n in nums):
    print("All numbers are greater than 5")  # Output: All numbers are greater than 5
if any(n < 15 for n in nums):
    print("At least one number is less than 15")  # Output: At least one number is less than 15