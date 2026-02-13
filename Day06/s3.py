import sys
import os

if len(sys.argv) < 3:
    print("Please enter StudentName Marks1 Marks 2 and so on..")
    sys.exit()

student_name = sys.argv[1]

try:
    marks = [float(m) for m in sys.argv[2:]]
except ValueError:
    print("Please enter valid numeric marks.")
    sys.exit()

average = sum(marks) / len(marks)
result = "Pass" if average >= 40 else "Fail"

directory = "assessment"
os.makedirs(directory, exist_ok=True)

file_path = os.path.join(directory, f"{student_name}.txt")

with open(file_path, "w") as file:
    file.write(f"Name: {student_name}, Marks: {marks}, Average: {average:.2f}, Result: {result}\n")

print(f"Assessment saved successfully for {student_name}")
