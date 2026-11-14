"""
Question:
Calculate factorial using recursion.
"""

def factorial(number):

    if number < 0:
        return None

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


number = int(input("Enter a number: "))

result = factorial(number)

if result is None:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial:", result)