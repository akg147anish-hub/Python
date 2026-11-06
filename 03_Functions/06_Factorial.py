"""
Question:
Calculate the factorial of a number using a function.
"""

def factorial(number):

    if number < 0:
        return "Factorial is not defined for negative numbers"

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


number = int(input("Enter a number: "))

print("Factorial:", factorial(number))