

class Course:
    """A course that stores students and their marks."""

    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_student(self, student, marks):
        """Add a student and their marks."""
        if not isinstance(marks, (int, float)):
            raise ValueError("Marks must be a number.")

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")

        self.marks[student] = marks

    def average(self):
        """Return the average of all marks."""
        if len(self.marks) == 0:
            return 0

        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        """Return the name of the student with the highest marks."""
        if len(self.marks) == 0:
            return None

        return max(self.marks, key=self.marks.get)

    def __len__(self):
        """Return the number of students."""
        return len(self.marks)
    
    def remove_student(self, name: str) -> None:
        """Remove a student, or raise KeyError if missing."""
        if name not in self.marks:
            raise KeyError(f"No student named {name}")
        del self.marks[name]
        
    

def load_course(filename):
    """Load students and marks from a file."""
    course = Course("Loaded Course")

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.rsplit(",", 1)

                if len(parts) == 2:
                    student = parts[0].strip()
                    marks = float(parts[1].strip())

                    if marks.is_integer():
                        marks = int(marks)

                    course.add_student(student, marks)

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")

    return course
