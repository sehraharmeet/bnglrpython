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

obj = MathOperations()
print(obj.add(10, 20))
obj.greet()
