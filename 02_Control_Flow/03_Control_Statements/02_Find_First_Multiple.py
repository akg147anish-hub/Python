"""
Question:
Find the first multiple of 7 between 1 and 100.
"""

for number in range(1, 101):
    if number % 7 == 0:
        print("First multiple of 7:", number)
        break