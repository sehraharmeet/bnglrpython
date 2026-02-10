import json

class Student:
    def __init__(self, sid, name, course):
        self.sid = sid
        self.name = name
        self.course = course

    def to_dict(self):
        return {
            "id": self.sid,
            "name": self.name,
            "course": self.course
        }

students = []

for i in range(2):
    print(f"Enter details for student {i+1}:")
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    students.append(Student(sid, name, course))

def jsonconv(student_list):
    data = [stud.to_dict() for stud in student_list]
    with open("students.json", "a") as file:
        json.dump(data, file, indent=4)
    print("students.json file created successfully.")


jsonconv(students)

