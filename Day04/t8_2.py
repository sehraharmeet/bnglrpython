import json
import os

FILE_NAME = "students.json"

class Student:
    def __init__(self, sid, name, course):
        self.sid = sid
        self.name = name
        self.course = course


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_students(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_students():
    existing_data = load_students()

    students = []

    n = int(input("How many students you want to add? "))

    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")

        student = Student(sid, name, course)
        students.append(student.__dict__)

    existing_data.extend(students)
    save_students(existing_data)

    print("\nStudents added successfully!")


def display_students():
    data = load_students()

    if not data:
        print("No students found.")
        return

    print("\nStudent Records:\n")

    for student in data:
        print(f"ID: {student['sid']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
        print("-" * 30)


def main():
    while True:
        print("""
========= Student Management =========
1. Add Students
2. Display Students
3. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_students()

        elif choice == "2":
            display_students()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


main()
