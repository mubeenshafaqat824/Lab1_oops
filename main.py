"""Main program for CSC350 Lab 1: Course Manager with Python OOP."""

from course import Course, InvalidMarksError, load_course


# ----- Task 1: warm-up Student class -----
class Student:
    """A student with a name and marks."""

    def __init__(self, name: str, marks: int):
        """Store name and marks as attributes."""
        self.name = name
        self.marks = marks

    def passed(self) -> bool:
        """Return True if marks are 50 or more."""
        return self.marks >= 50

    def __str__(self) -> str:
        return f"{self.name} ({self.marks}): {'Pass' if self.passed() else 'Fail'}"


students = [Student("Ali", 72), Student("Sara", 45), Student("Omar", 50)]
for s in students:
    print(s)

# ----- Task 2: test the Course class -----
c = Course("Programming for AI")
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)
print(len(c))
print(c.average())
print(c.top_student())

# ----- Task 3: custom exception and __str__ -----
try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:", e)
print(c)

# ----- Task 4: load students from a file -----
course = load_course("Programming for AI", "marks.txt")
print(course)
print("Top student:", course.top_student())

# wrong file name
load_course("Programming for AI", "mark.txt")
