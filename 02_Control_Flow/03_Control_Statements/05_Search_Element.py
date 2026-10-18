"""
Question:
Search for 30 in a list.
Print its index and stop searching when found.
"""

numbers = [10, 20, 30, 40, 50]
target = 30

for index, number in enumerate(numbers):
    if number == target:
        print("Element found at index:", index)
        break
else:
    print("Element not found")