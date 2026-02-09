class Employee:
    def method_name(self):
        self.empcode=1001
        self.empname="harmeet"
        print(f"EmpCode {self.empcode}-{self.empname}")

    def method_name2(self):
        print(f"EmpCode {self.empcode}-{self.empname}")
emp1=Employee()
emp1.method_name()
emp1.method_name2()
