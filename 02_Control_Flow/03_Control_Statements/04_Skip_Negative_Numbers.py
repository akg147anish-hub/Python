"""
Question:
Print only non-negative numbers from a list.
"""

numbers = [10, -5, 20, -8, 0, 15, -2]

for number in numbers:
    if number < 0:
        continue

    print(number)