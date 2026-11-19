"""
Question:
Modify a global variable inside a function.
"""

count = 10


def update_count():
    global count
    count = 20


print("Before:", count)

update_count()

print("After:", count)