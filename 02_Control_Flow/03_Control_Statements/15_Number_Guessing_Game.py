"""
Question:
Create a number guessing game with a maximum of 5 attempts.
Stop when the correct number is guessed.
"""

secret_number = 27
max_attempts = 5

for attempt in range(1, max_attempts + 1):
    guess = int(input("Guess the number (1-50): "))

    if guess == secret_number:
        print("Correct guess!")
        break

    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    if attempt == max_attempts:
        print("Game over! The number was", secret_number)