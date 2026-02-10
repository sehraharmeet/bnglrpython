class Employee:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} -> Employee constructor function")

    def display_info(self):
        print(f"{self.name} handles basic operations")


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} -> Manager constructor function")

    def display_info(self):
        print(f"{self.name} manages team and projects")


class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)

    def display_info(self):
        print(f"{self.name} writes and maintains code")



employees = [
    Employee("Amit"),
    Manager("Rahul"),
    Developer("Neha")
]

print("\n--- Employee Responsibilities ---\n")

for emp in employees:
    emp.display_info()
