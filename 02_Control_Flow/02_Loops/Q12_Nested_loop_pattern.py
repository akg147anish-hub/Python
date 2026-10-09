"""
Question:
Print a right angled star pattern using nested loops.
"""

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):

    for j in range(i):
        print("*", end="")

    print()