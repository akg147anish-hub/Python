"""
Question:
Print numbers from 1 to 15.
Skip multiples of 3.
"""

for number in range(1, 16):
    if number % 3 == 0:
        continue

    print(number)