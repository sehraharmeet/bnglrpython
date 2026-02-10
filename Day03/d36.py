class Employee:
    def __init__(self,param1,param2):
        self.empcode = param1
        self.empname = param2

    def method_name(self):
        print(f"EmpCode {self.empcode}-{self.empname}")

emp1=Employee(10001,"Harmeet")
emp2=Employee(10002,"Reema")

emp1.method_name()
emp2.method_name()