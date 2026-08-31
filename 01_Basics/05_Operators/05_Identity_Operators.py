"""
Topic      : Identity Operators
Module     : Python Basics - Operators
Description: Demonstrates 'is' and 'is not' operators.
Author     : Anish Kumar Gupta
"""

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print("list_a is list_b:", list_a is list_b)
print("list_a is list_c:", list_a is list_c)

print("list_a is not list_c:", list_a is not list_c)