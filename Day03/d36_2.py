class Employee:
    # def __init__(self):
    #     self.empcode = 1001
    #     self.empname = "Aman"
    def __init__(self,param1=1001,param2="Aman"):
        self.empcode = param1
        self.empname = param2

    def method_name(self):
        print(f"EmpCode {self.empcode}-{self.empname}")

emp0=Employee()
emp0.method_name()

emp1=Employee(10001,"Harmeet")
emp1.method_name()

emp2=Employee(10002,"Reema")
emp2.method_name()