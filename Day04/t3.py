class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working as a general employee.")

class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code.")

class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing a product.")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing the team.")

def employee_work(employee):
    employee.work()

dev = Developer("Alisha", 90000)
designer = Designer("Reema", 80000)
manager = Manager("Jai", 100000)

employee_work(dev)       
employee_work(designer)  
employee_work(manager)   

