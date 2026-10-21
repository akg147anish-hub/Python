"""
Question:
Keep accepting numbers until the user enters 0.
Print their sum.
"""

total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total += number

print("Total sum:", total)