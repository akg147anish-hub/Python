"""
Question:
Display multiple student details using **kwargs.
"""

def student_details(**details):

    for key, value in details.items():
        print(key, ":", value)


student_details(
    name="Rishabh",
    age=20,
    course="BTech CSE",
    college="IIT Bombay"
)