"""
Question:
Find the largest among three numbers using a function.
"""

def find_largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


result = find_largest(10, 25, 15)

print("Largest number:", result)