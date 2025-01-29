"""
Generators

Generators are special functions in Python that return an iterator and allow you to iterate over data lazily (one item at a time).
This is useful for working with large datasets or streams of data without loading everything into memory at once.
"""

#Creating Generators with `yield`
#A generator function uses the `yield` keyword instead of `return`.
#Each time `yield` is called, the function pauses its state and resumes from there on the next call.

"""
The difference is that while a return statement terminates a function entirely,
yield statement pauses the function saving all its states and later continues from there on successive calls.
Return sends a specified value back to its caller whereas Yield can produce a sequence of values.

"""

# Example: A generator to produce numbers from 1 to n
def number_generator(n):
    for i in range(1, n + 1):
        yield i  # Yield pauses the function and sends the current value

# Using the generator
gen = number_generator(5)
for num in gen:
    print(num, end=" ")  # Output: 1 2 3 4 5


#Lazy Evaluation
#Generators allow processing of large data lazily, saving memory.

# Generating squares of numbers lazily
def square_numbers(n):
    for i in range(n):
        yield i * i

squares = square_numbers(1000000)  # Large range
print(next(squares))  # Output: 0
print(next(squares))  # Output: 1
print(next(squares))  # Output: 4


"""
Python generators are incredibly useful in real-world projects when working with large datasets, 
asynchronous tasks, or situations where computation needs to be efficient in terms of memory and processing. 
Here are some practical scenarios where generators are widely used:

Use Generators in Real-World Projects?
Memory Efficiency: Process large datasets without loading them fully into memory.
Lazy Evaluation: Generate values only when needed, saving resources.
Pipelines: Create clean, readable, and efficient data processing workflows.
Performance Optimization: Minimize the overhead of repeated computations.
Scalability: Handle large-scale data or infinite sequences seamlessly.

"""

# Processing Large Files or Streams
"""
   - Scenario: When handling files too large to fit into memory, such as logs, CSVs, or JSON files.
   - Why: Generators allow processing the file line by line without loading the entire file into memory.
   - Example: Reading a large log file line by line.
"""


def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


for line in read_large_file("large_log.txt"):
    print(line)

# Infinite and  Streaming Data (Real-Time Data Processing)
"""
   - Scenario: When generating or processing infinite sequences, such as sensor data, random numbers, or live feeds.
   - Why: Generators are ideal for producing data on demand without exhausting memory.
   - Example: Generating an infinite stream of Fibonacci numbers.
"""
# Infine Data Example 1
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))


# Stream data Exampple 2
import random
import time
def sensor_data_stream():
    while True:
        yield {"temperature": random.uniform(20.0, 30.0), "humidity": random.uniform(30.0, 50.0)}
        time.sleep(1)
# Usage
for data in sensor_data_stream():
    print(data)

# Lazy Evaluation of Large Computations
"""
   - Scenario: When dealing with computationally expensive operations that you don't want to perform upfront.
   - Why: Generators compute values only when needed, optimizing resource usage.
   - Example: Generating prime numbers lazily.
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


prime_gen = generate_primes()
for _ in range(5):
    print(next(prime_gen))

# Data Streaming in APIs
"""
   - Scenario: Streaming responses in APIs to handle large amounts of data (e.g., paginated or continuous data).
   - Why: Generators allow you to stream data in chunks rather than sending it all at once.
   - Example: Streaming database query results in Flask.
"""

# Pipeline Processing
"""
   - Scenario: Building data processing pipelines where data flows through multiple transformations.
   - Why: Generators can process data lazily and efficiently, step by step.
   - Example: ETL pipeline for processing large datasets.
"""
def read_data():
    for i in range(1, 101):
        yield i

def filter_data(data):
    for item in data:
        if item % 2 == 0:
            yield item

def transform_data(data):
    for item in data:
        yield item
        2

pipeline = transform_data(filter_data(read_data()))
for item in pipeline:
    print(item)



# Memory-Efficient Data Generation
"""
   - Scenario: When you need to generate large datasets dynamically (e.g., mock data for testing).
   - Why: Generators avoid keeping the entire dataset in memory.
   - Example: Generating mock data for a database.
"""
import random

def generate_mock_data(n):
    for _ in range(n):
        yield {"id": random.randint(1, 1000), "value": random.random()}

for record in generate_mock_data(5):
    print(record)

# Pagination in Large Datasets
"""
   - Scenario: Fetching data in chunks from a database or API to avoid memory overload.
   - Why: Generators allow efficient pagination, fetching only the required subset of data.
   - Example: Paginating database query results.
"""
def paginate(query, page_size):
    total = len(query)
    for start in range(0, total, page_size):
        yield query[start:start + page_size]

data = list(range(1, 101))
for page in paginate(data, 10):
    print(page)
