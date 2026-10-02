"""
Question:
Count the number of digits in a number.
"""

number = int(input("Enter a number: "))

number = abs(number)

count = 0

if number == 0:
    count = 1
else:
    while number > 0:
        number //= 10
        count += 1

print("Number of digits:", count)
