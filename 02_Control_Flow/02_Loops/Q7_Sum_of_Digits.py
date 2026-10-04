"""
Question:
Calculate the sum of digits of a number.
"""

number = int(input("Enter a number: "))

number = abs(number)

digit_sum = 0

while number > 0:
    digit_sum += number % 10
    number //= 10

print("Sum of digits:", digit_sum)