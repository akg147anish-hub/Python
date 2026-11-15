"""
Question:
Generate Fibonacci numbers using recursion.
"""

def fibonacci(number):

    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


terms = int(input("Enter number of terms: "))

if terms < 0:
    print("Enter a non-negative number")
else:
    for i in range(terms):
        print(fibonacci(i), end=" ")

    print()