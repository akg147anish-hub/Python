"""
Question:
Remove duplicates from a list while preserving order.
Use continue to skip elements already seen.
"""

numbers = [10, 20, 10, 30, 20, 40, 30]
unique_numbers = []

for number in numbers:
    if number in unique_numbers:
        continue

    unique_numbers.append(number)

print(unique_numbers)