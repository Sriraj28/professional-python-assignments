class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.__salary}")

    def calculate_bonus(self):
        return self.__salary * 0.10


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def calculate_bonus(self):
        return self.team_size * 5000


class Developer(Employee):
    def calculate_bonus(self):
        return 15000


# Objects
manager = Manager("Rahul", 60000, 5)
developer = Developer("Anita", 50000)

manager.display()
print("Manager Bonus:", manager.calculate_bonus())

print()

developer.display()
print("Developer Bonus:", developer.calculate_bonus())
