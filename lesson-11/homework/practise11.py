 1. Create a Virtual Environment & Install Packages
1.python -m venv venv
2.venv\Scripts\activate
3.pip install requests numpy
4.pip list
2. Create Custom Modules
1.def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
  2.def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
3.import math_operations
import string_utils

print(math_operations.add(5, 3))
print(math_operations.divide(10, 2))

print(string_utils.reverse_string("Python"))
print(string_utils.count_vowels("Hello World"))

3. Create Custom Packages
1.import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

from geometry.circle import calculate_area, calculate_circumference

print(calculate_area(5))
print(calculate_circumference(5))

2.def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
from file_operations.file_writer import write_file
from file_operations.file_reader import read_file

write_file("test.txt", "Hello Python!")
print(read_file("test.txt"))

