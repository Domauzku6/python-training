# int.py

# Basic integer operations
a = 10
b = 3

print("Integer operations:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)  # Integer division
print("a % b =", a % b)    # Modulus
print("a ** b =", a ** b)  # Exponentiation

# Basic float operations
x = 10.5
y = 3.2

print("\nFloat operations:")
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)  # Floor division
print("x % y =", x % y)    # Modulus
print("x ** y =", x ** y)  # Exponentiation

# Working with large integers
large_int = 123456789012345678901234567890
print("\nLarge integer:", large_int)

# Converting strings to integers and floats
str_num = "12345"
int_num = int(str_num)
float_num = float(str_num)
print("\nConverted string to integer:", int_num)
print("Converted string to float:", float_num)

# Binary, octal, and hexadecimal representations
binary_num = 0b1010
octal_num = 0o12
hex_num = 0xA

print("\nBinary 0b1010 as integer:", binary_num)
print("Octal 0o12 as integer:", octal_num)
print("Hexadecimal 0xA as integer:", hex_num)

# Complex numbers
complex_num1 = 2 + 3j
complex_num2 = 1 + 2j

print("\nComplex number operations:")
print("complex_num1 + complex_num2 =", complex_num1 + complex_num2)
print("complex_num1 - complex_num2 =", complex_num1 - complex_num2)
print("complex_num1 * complex_num2 =", complex_num1 * complex_num2)
print("complex_num1 / complex_num2 =", complex_num1 / complex_num2)