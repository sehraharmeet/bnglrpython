class Employee:
    def __init__(self, empcode, empname):
        self.empcode = empcode
        self.empname = empname

    def method_name(self):
        print(f"EmpCode {self.empcode} - {self.empname}")

employees = [
    [1001, "Aman"],
    [10001, "Harmeet"]
]

emp_objects = []

for code, name in employees:    
    emp_objects.append(Employee(code, name))

for e in emp_objects:
    print(e.empcode)
    #e.method_nmae()
