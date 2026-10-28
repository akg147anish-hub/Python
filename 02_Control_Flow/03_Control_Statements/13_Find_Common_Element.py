"""
Question:
Find common elements in two lists without duplicate results.
"""

first_list = [10, 20, 30, 40, 20]
second_list = [20, 30, 50, 30]

common = []

for number in first_list:
    if number not in second_list:
        continue

    if number in common:
        continue

    common.append(number)

print("Common elements:", common)