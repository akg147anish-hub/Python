"""
Question:
Demonstrate remove(), pop() and clear().
"""

numbers = [10, 20, 30, 40, 50]

numbers.remove(20)
print("After remove:", numbers)

removed = numbers.pop()
print("Removed element:", removed)
print("After pop:", numbers)

numbers.clear()
print("After clear:", numbers)