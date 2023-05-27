# Example 1: Creating a Class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example 2: Inheriting from a Parent Class
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# Example 3: Encapsulation and Abstraction
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self._balance

# Example 4: Opening and Closing Files
file = open("data.txt", "r")
content = file.read()
file.close()

# Example 5: Reading and Writing Files
file = open("data.txt", "w")
file.write("Hello, World!")
file.close()

# Example 6: File Positions and Seek
file = open("data.txt", "r")
file.seek(5)
content = file.read()
file.close()

# Example 7: Importing Modules
import math

# Example 8: Creating Modules
# File: math_operations.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Example 9: Packages
# File: mypackage/__init__.py
# Empty file to mark the directory as a Python package

# File: mypackage/mymodule.py
def say_hello():
    print("Hello, World!")

# Example 10: Regular Expressions
import re

# Example 11: Pattern Matching
pattern = r"\d{3}-\d{3}-\d{4}"
text = "Phone numbers: 123-456-7890, 987-654-3210"
matches = re.findall(pattern, text)

# Example 12: Modifying Strings with Regular Expressions
pattern = r"world"
text = "Hello, world! Welcome to the world."
modified_text = re.sub(pattern, "Python", text)

# Example 13: Handling Exceptions with try-except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Example 14: The finally Block and Clean-up Actions
try:
    # Code that may raise an exception
finally:
    # Cleanup code that always executes
