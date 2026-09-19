"""
Question:
Find the largest of two numbers.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("Largest:", num1)
elif num2 > num1:
    print("Largest:", num2)
else:
    print("Both numbers are equal.")