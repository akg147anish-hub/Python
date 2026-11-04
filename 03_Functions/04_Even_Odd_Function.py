"""
Question:
Check whether a number is even or odd using a function.
"""

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))

result = check_even_odd(number)

print(result)