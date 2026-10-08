"""
Question:
Print all prime numbers within a given range.
"""

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for number in range(start, end + 1):

    if number < 2:
        continue

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")