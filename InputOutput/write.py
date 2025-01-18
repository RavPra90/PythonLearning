# Python provides robust functionality for writing data to files.
# Here's a comprehensive explanation with code snippets to demonstrate both basic and advanced concepts.

# Basic Concepts

# Writing to a File
# The `open()` function is used to open a file in write mode (`'w'`).
# This will overwrite the file if it already exists.

# Writing to a file (overwrites existing content)
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Python file writing is simple.")


# Writing Lines to a File
# The `writelines()` method writes a list of strings to a file.
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open('example.txt', 'w') as file:
    file.writelines(lines)

#different write modes and their implications:
def demonstrate_write_modes():
    # 'w' - Write mode (overwrites file)
    with open('modes.txt', 'w') as file:
        file.write("This overwrites everything\n")

    # 'a' - Append mode (adds to end of file)
    with open('modes.txt', 'a') as file:
        file.write("This gets added to the end\n")

    # 'x' - Use `'x'` mode to create a new file. An error is raised if the file already exists.
    try:
        with open('new_file.txt', 'x') as file:
            file.write("This only works for new files\n")
    except FileExistsError:
        print("File already exists!")


#  Writing Binary Data
# For binary files (e.g., images or byte streams), use `'wb'`.
data = b"Binary data example"

with open('binary_file.bin', 'wb') as file:
    file.write(data)


#  Advanced Concepts

# Writing Data Using `print()`
# You can redirect the output of the `print()` function to a file.
with open('example.txt', 'w') as file:
    print("Using print to write to a file.", file=file)


#Writing JSON Data
# Python’s `json` module is used to write dictionaries or lists as JSON to a file.
import json

data = {"name": "John", "age": 30, "city": "New York"}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)



# Writing CSV Files
# The `csv` module is useful for working with structured data.
import csv

data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Jane", 25, "Los Angeles"],
]

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)



# Writing Large Files Efficiently
# For large data sets, write in chunks to avoid memory issues.
large_data = ["Line {}\n".format(i) for i in range(1, 1000001)]  # 1 million lines

with open('large_file.txt', 'w') as file:
    for line in large_data:
        file.write(line)


# Writing with `Path` from `pathlib`
# The `pathlib` module simplifies file operations.
from pathlib import Path

data = "Writing data using pathlib.\n"

path = Path('example_pathlib.txt')
path.write_text(data)



# Writing Temporary Files
# The `tempfile` module allows for creating temporary files that are automatically deleted
import tempfile

with tempfile.TemporaryFile('w+t') as temp_file:
    temp_file.write("Temporary file content.\n")
    temp_file.seek(0)  # Move cursor to the beginning
    print(temp_file.read())  # Output: Temporary file content.



# Writing Structured Data with `pickle`
# The `pickle` module serializes Python objects.
import pickle

data = {"name": "Alice", "scores": [90, 85, 88]}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)



# Handling Exceptions While Writing
# Gracefully handle errors during file operations.
try:
    with open('example.txt', 'w') as file:
        file.write("This might fail!")
except OSError as e:
    print(f"An error occurred: {e}")



# Writing File Line by Line Using a Generator
# Use generators to write data efficiently.
def generate_lines():
    for i in range(1, 101):
        yield f"Line {i}\n"

with open('generator_file.txt', 'w') as file:
    for line in generate_lines():
        file.write(line)


# Writing Data to Multiple Files
# Write to multiple files simultaneously.
file_names = ['file1.txt', 'file2.txt', 'file3.txt']

for i, name in enumerate(file_names, 1):
    with open(name, 'w') as file:
        file.write(f"This is File {i}")