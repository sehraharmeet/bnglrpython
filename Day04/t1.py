class Salary:
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

class Work:
    def __init__(self, hours):
        self.hours = hours

    def get_work_hours(self):
        return self.hours


class Employee(Salary, Work):

    def __init__(self, name, salary, hours):
        self.name = name
        
        Salary.__init__(self, salary)
        Work.__init__(self, hours)

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.get_salary())
        print("Work Hours:", self.get_work_hours())

emp = Employee("Rahul", 50000, 8)
emp.display()
