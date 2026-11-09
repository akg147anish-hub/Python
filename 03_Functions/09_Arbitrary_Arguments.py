"""
Question:
Calculate the sum of any number of arguments using *args.
"""

def calculate_sum(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total


print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30, 40))