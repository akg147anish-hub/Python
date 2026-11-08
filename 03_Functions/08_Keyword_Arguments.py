"""
Question:
Display student details using keyword arguments.
"""

def student_details(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_details(
    course="BTech CSE",
    name="Anish",
    age=20
)