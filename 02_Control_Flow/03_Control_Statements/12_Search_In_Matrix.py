"""
Question:
Search for a target in a matrix.
Stop searching when the target is found.
"""

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50
found = False

for row_index, row in enumerate(matrix):
    for column_index, value in enumerate(row):
        if value == target:
            print(
                f"Found at row {row_index}, column {column_index}"
            )
            found = True
            break

    if found:
        break

if not found:
    print("Element not found")