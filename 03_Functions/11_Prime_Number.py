"""
Question:
Check whether a number is prime using a function.
"""

def is_prime(number):

    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime number")
else:
    print("Not a prime number")