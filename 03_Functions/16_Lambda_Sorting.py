"""
Question:
Sort a list of tuples based on the second element.
"""

students = [
    ("Keshav", 85),
    ("Rahul", 70),
    ("Aman", 95),
    ("Rohit", 80)
]

students.sort(key=lambda student: student[1])

print(students)