class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'F'

    def display(self):
        print(f"Roll No: {self.roll_no} | Name: {self.name:<10} | Marks: {self.marks:<3} | Grade: {self.grade}")


class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        print(f"\n--- {self.college_name} Student Records ---")
        for student in self.students:
            student.display()


# Execution
mit = College("MIT ADT")
mit.add_student(Student(101, "Alice", 92))
mit.add_student(Student(102, "Bob", 78))
mit.add_student(Student(103, "Charlie", 64))
mit.add_student(Student(104, "David", 45))

mit.display_all_students()
