import os
print(os.getcwd())
print(os.listdir())
os.mkdir("new_folder_feb09_2026")
print(os.listdir())
os.rmdir("new_folder_feb09_2026")
print(os.listdir())

# os.rename("old.txt", "new.txt")
# os.remove("file.txt")
print(os.path.isdir("new_folder"))
print(os.path.isfile("d31.py"))

# path = os.path.join("special", "file.txt")
# os.path.exists("file.txt")

