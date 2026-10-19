"""
Question:
Find the first even number in a list.
"""

numbers = [7, 9, 11, 14, 18, 21]

for number in numbers:
    if number % 2 == 0:
        print("First even number:", number)
        break
else:
    print("No even number found")