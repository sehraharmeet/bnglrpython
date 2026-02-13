class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
   
    @staticmethod
    def deduct_tax(amount):
        return amount * 0.90   # 10% deduction

    def calculate_salary(self):
        return Employee.deduct_tax(self.base_salary)


class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        gross = self.base_salary + self.bonus
        return Employee.deduct_tax(gross)


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name, 0)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        gross = self.hours * self.rate
        return Employee.deduct_tax(gross)


e1 = FullTimeEmployee("Aman", 50000, 10000)
e2 = PartTimeEmployee("Riya", 80, 500)

print(e1.name, "Final Salary:", e1.calculate_salary())
print(e2.name, "Final Salary:", e2.calculate_salary())
