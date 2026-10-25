"""
Question:
Create a menu-driven calculator.
Exit when the user chooses 5.
"""

while True:
    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator closed.")
        break

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice.")
        continue

    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", first + second)

    elif choice == "2":
        print("Result:", first - second)

    elif choice == "3":
        print("Result:", first * second)

    elif choice == "4":
        if second == 0:
            print("Cannot divide by zero.")
            continue

        print("Result:", first / second)