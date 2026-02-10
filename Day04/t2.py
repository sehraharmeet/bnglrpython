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


class Employee:

    def __init__(self, name, salary, hours):
        self.name = name
        
        self.salary_obj = Salary(salary)
        self.work_obj = Work(hours)

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary_obj.get_salary())
        print("Work Hours:", self.work_obj.get_work_hours())


emp = Employee("Rahul", 50000, 8)
emp.display()
