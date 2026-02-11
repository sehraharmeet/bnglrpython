class Student:
    def __init__(self, sid, name, course):
        self.sid = sid
        self.name = name
        self.course = course

    def __str__(self):
        return f"Student ID: {self.sid}, Name: {self.name}, Course: {self.course}"
    
    def __len__(self):
        return len(self.name)


s1 = Student(101, "Harmeet", "Python")

print(s1)
print(len(s1))

