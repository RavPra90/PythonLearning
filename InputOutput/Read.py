# Python provides simple yet powerful tools for reading files.
# Here’s a comprehensive guide to both basic and advanced file reading techniques with code examples.

# Basic Concepts

#Reading a File Using `open()`
# The `open()` function is used to open files. Always remember to close the file after reading.

#Reading the Entire File
# Open and read the entire file at once
file = open('example.txt', 'r')  # 'r' stands for read mode
content = file.read()   #Reads entire file into memory
print(content)  # Outputs the entire file content
file.close()  # Close the file to free resources


#Using `with` (Recommended)
# Using `with` automatically closes the file after usage.
# The with statement is crucial as it ensures proper file handling and automatically
# closes the file when we're done. This is called context management.
# File is automatically closed after the block
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)



# Reading Line by Line - more memory efficient for large files
with open('example.txt', 'r') as file:
    for line in file:  #File object is an iterator
        print(line.strip())  # Print each line without trailing newline characters


# Different ways to read file content
with open('example.txt', 'r') as file:

    content = file.read(10)  # Reads the first 10 characters

    first_line = file.readline()      # Read one line at a time

    all_lines = file.readlines() #The `readlines()` method reads all lines and stores them in a list.

    file.seek(0) # Reset file pointer to beginning. If we dont set it then the cursor will point to last element of the line



 # Advanced Concepts

#Reading Binary Files
# For non-text files (like images or PDFs), use `'rb'` mode
with open('image.png', 'rb') as file:
    binary_data = file.read()
    print(binary_data[:10])  # Output: First 10 bytes of the file


# Reading files with specific encoding
import codecs

# Reading UTF-8 file with error handling
with codecs.open('unicode_file.txt', 'r', encoding='utf-8', errors='replace') as file:
    content = file.read()  # 'replace' substitutes invalid characters with �

# Using different encodings
with open('file.txt', 'r', encoding='latin-1') as file:
    content = file.read()


#handling large files efficiently using generators:
def read_in_chunks(file_path, chunk_size=1024):
    """
    Generator function to read file in chunks
    Useful for large files to prevent memory overload
    """
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Usage example
for chunk in read_in_chunks('large_file.txt'):
   print(chunk)

#Reading File in Reverse Order
# Reverse the lines of a file.
with open('example.txt', 'r') as file:
    for line in reversed(file.readlines()):
        print(line.strip())



# Using File Seek and Tell
# Control the file pointer using `seek()` and find the current position using `tell()`.
with open('example.txt', 'r') as file:
    print(file.tell())  # Current position (0 at the start)
    file.seek(5)        # Move to the 5th byte
    print(file.read(10))  # Read 10 characters from the 5th byte
    print(file.tell())  # Current position after reading



# Using `Path` from `pathlib`
# The `pathlib` module simplifies file reading operations.
from pathlib import Path

# Read the entire file
content = Path('example.txt').read_text()
print(content)

# Read binary files
binary_content = Path('image.png').read_bytes()
print(binary_content[:10])  # First 10 bytes



#Reading CSV Files
# Python provides the `csv` module for handling CSV files.
import csv
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list


# Reading JSON Files
# Python’s `json` module is used to read and parse JSON files.
import json
with open('data.json', 'r') as file:
    data = json.load(file)  # Parse JSON into a Python dictionary
    print(data)



# Handling File Not Found Errors
# Gracefully handle errors while reading files.
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")


# Read File and Skip Blank Lines
# Ignore empty lines while reading a file
with open('example.txt', 'r') as file:
    for line in file:
        if line.strip():  # Skip blank lines
            print(line.strip())



# Reading File Based on Delimiter
# Use the `split()` method for custom delimiters.
with open('example.txt', 'r') as file:
    content = file.read()
    parts = content.split('---')  # Split based on '---'
    print(parts)


# Context Manager for Temporary Files
# Use `tempfile` for creating temporary files.
import tempfile

with tempfile.TemporaryFile('w+t') as temp_file:
    temp_file.write("Temporary file content")
    temp_file.seek(0)
    print(temp_file.read())  # Output: Temporary file content
