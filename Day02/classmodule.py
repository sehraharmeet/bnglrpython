class Employee:
    def __init__(self ,co):
        self.company=co 
        print("Employee constructor function")
    
    def disp(self):
        print("disp  function of Employee",self.co)
     
class Manager(Employee):
    def __init__(self,cd,nm,lc,co ): 
        super().__init__(co)
        self.code=cd
        self.name=nm
        self.location=lc        
        print("Manager constructor function")

    def disp(self):        
        print("disp  function of Manager",self.code )
         
manager_1 = Manager("101","harmeet","delhi","Bosch")
manager_1.disp()

 

