class MathOperations:
    name="Bosch"
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def greet():
        print("Welcome to Static Methods!")

print(MathOperations.add(5, 3))
MathOperations.greet()
MathOperations.name="Bosch1"
print(MathOperations.name)
#MathOperations().name="Bosch2" 
#print(MathOperations.name)

obj = MathOperations()
print(obj.add(10, 20))
print(obj.name)
obj.name="Bosch2" 
print(obj.name)
print(MathOperations.name)

