"""Lab 1 starter: complete every TODO."""


class Course:
    """A course that stores students and their marks."""

    def __init__(self, name):
        self.name = name
        self.marks = {}            # student name -> marks

    def add_student(self, student, marks):
        # TODO: raise ValueError if marks are not between 0 and 100
        # TODO: store marks in self.marks using the student name as key
        pass

    def average(self):
        # TODO: return the average of all marks
        pass

    def top_student(self):
        # TODO: return the name of the student with the highest marks
        pass

    def __len__(self):
        # TODO: return the number of students
        pass
