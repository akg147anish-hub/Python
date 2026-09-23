"""
Question:
Calculate grade based on marks.
"""

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 40:
    print("Grade: E")
else:
    print("Grade: F")