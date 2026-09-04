class Person:
    def __init__(self, name= str):
        self.name = name

    def introduce(self):
        return f"hi myself {self.name}"

class Student(Person):
    def __init__(self, name= str, roll_no= int):
        super().__init__(name)
        self.roll_no =roll_no

#method overriding
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro} and my rollno is {self.roll_no}"

me = Student("Sriraj",23)
print(me.introduce())
print(Student.mro())
