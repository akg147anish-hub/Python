"""
Question:
Reverse the digits of a number.
"""

number = int(input("Enter a number: "))

original = number
number = abs(number)

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

if original < 0:
    reverse = -reverse

print("Reversed number:", reverse)