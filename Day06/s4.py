class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name, 0)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


e1 = FullTimeEmployee("Aman", 50000, 10000)
e2 = PartTimeEmployee("Riya", 80, 500)

print(e1.name, "Salary:", e1.calculate_salary())
print(e2.name, "Salary:", e2.calculate_salary())

