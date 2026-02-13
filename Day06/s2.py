import sys

if len(sys.argv) < 2:
    print("Please provide marks as command-line arguments.")
    sys.exit()

marks = [float(m) for m in sys.argv[1:]]

average = sum(marks) / len(marks)

print("Average Marks:", average)

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

