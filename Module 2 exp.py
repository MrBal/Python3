# Example 1: Variable assignment
x = 10
name = "John"

# Example 2: Strings
message = "Hello, World!"

# Example 3: Numbers
count = 10
price = 19.99

# Example 4: Lists
numbers = [1, 2, 3, 4, 5]

# Example 5: Tuples
point = (3, 4)

# Example 6: Dictionaries
student = {"name": "John", "age": 20, "grade": "A"}

# Example 7: Sets
fruits = {"apple", "banana", "orange"}

# Example 8: Arithmetic operators
x = 10 + 5

# Example 9: Comparison operators
x = 10 > 5

# Example 10: Logical operators
x = True and False

# Example 11: Assignment operators
x = 10

# Example 12: Conditional statements
if x > 10:
    print("x is greater than 10")

# Example 13: For loop
for i in range(5):
    print(i)

# Example 14: Break and continue statements
for i in range(10):
    if i == 5:
        break
    print(i)

# Example 15: Range function
for i in range(1, 6):
    print(i)

# Example 16: Defining functions
def greet(name):
    print("Hello, " + name + "!")

# Example 17: Parameters and arguments
greet("John")

# Example 18: Returning values from functions
def add(x, y):
    return x + y

result = add(3, 5)

# Example 19: Scope and variable visibility
def my_function():
    x = 10
    print(x)

my_function()

# Example 20: Handling exceptions with try-except blocks
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Example 21: Catching specific types of exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")

# Example 22: Raising exceptions with raise statement
def validate_age(age):
    if age < 0:
        raise ValueError("Invalid age!")

validate_age(-5)

# Example 23: Finally block for cleanup operations
try:
    # Code that may raise an exception
finally:
    # Cleanup code that always executes
