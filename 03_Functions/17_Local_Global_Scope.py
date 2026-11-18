"""
Question:
Demonstrate local and global variable scope.
"""

message = "Global variable"


def display():
    message = "Local variable"
    print(message)


display()

print(message)