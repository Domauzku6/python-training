from math import sqrt
# This imports the sqrt function from the math module, which is used to calculate the square root of a number.

import math as m
# This imports the entire math module and gives it an alias 'm'. You can use 'm' to access any function or constant in the math module, such as m.pi or m.sin().

import sys
# This imports the sys module, which provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter. For example, sys.argv can be used to access command-line arguments.

print("Hello, World!") # print statement
"""
This script contains two print statements that output messages to the console.
Functions:
    print("Hello, World!"): Prints the string "Hello, World!" to the console.
    print("Welcome to programming world!"): Prints the string "Welcome to programming world!" to the console.
"""
# False: A boolean value representing false.
print(False)

# class: Used to define a new user-defined class.
class MyClass:
    pass

# finally: Used in try...except blocks to define a block of code that will be executed no matter if there is an exception or not.
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Division by zero!")
finally:
    print("This is the finally block.")

# is: Used to test object identity.
print(1 is 1)

# return: Used to exit a function and return a value.
def my_function():
    return "Returned value"
print(my_function())

# None: A special constant representing the absence of a value or a null value.
print(None)

# continue: Used to skip the rest of the code inside a loop for the current iteration only.
for i in range(5):
    if i == 2:
        continue
    print(i)

# for: Used to create a for loop.
for i in range(3):
    print(i)

# lambda: Used to create an anonymous function.
add = lambda x, y: x + y
print(add(2, 3))

# try: Used to catch exceptions.
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Caught division by zero!")

# True: A boolean value representing true.
print(True)

# def: Used to define a function.
def greet():
    print("Hello!")
greet()

# from: Used to import specific parts of a module.
print(sqrt(4))

# nonlocal: Used to declare that a variable inside a nested function is not local to it.
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
    inner()
    print(x)
outer()

# while: Used to create a while loop.
i = 0
while i < 3:
    print(i)
    i += 1

# and: A logical operator.
print(True and False)

# del: Used to delete objects.
x = [1, 2, 3]
del x[1]
print(x)

# global: Used to declare a global variable.
global_var = "global"
def global_test():
    global global_var
    global_var = "modified global"
global_test()
print(global_var)

# not: A logical operator.
print(not False)

# with: Used to wrap the execution of a block of code.
with open("test.txt", "w") as file:
    file.write("Hello, World!")

# as: Used to create an alias.
print(m.pi)

# elif: Used in conditional statements, same as else if.
x = 10
if x < 5:
    print("x is less than 5")
elif x == 10:
    print("x is 10")
else:
    print("x is greater than 5")

# if: Used to make a conditional statement.
if True:
    print("This is true")

# or: A logical operator.
print(True or False)

# yield: Used to return a generator.
def generator():
    yield 1
    yield 2
    yield 3
for value in generator():
    print(value)

# assert: Used for debugging purposes.
assert 2 + 2 == 4

# else: Used in conditional statements.
if False:
    print("This won't be printed")
else:
    print("This will be printed")

# import: Used to import modules.
print(sys.version)

# pass: A null statement, a statement that will do nothing.
def empty_function():
    pass

# break: Used to break out of a loop.
for i in range(5):
    if i == 3:
        break
    print(i)

# except: Used to catch exceptions.
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Caught an exception")

# int: A data type representing integers.
print(int(3.5))

# raise: Used to raise an exception.
try:
    raise ValueError("An error occurred")
except ValueError as e:
    print(e)



print("Welcome to programming world!") # print statement
###
#output:
#Hello, World
###



