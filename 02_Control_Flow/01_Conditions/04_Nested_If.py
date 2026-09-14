"""
Topic: Nested if
Description: Demonstrates an if statement inside another if statement.
"""

age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")

if age >= 18:
    if has_id == "yes":
        print("Entry allowed.")
    else:
        print("Please show your ID.")
else:
    print("Entry not allowed.")