"""
Question:
Print an increasing number pattern.
"""

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(j, end="")

    print()