# file = open("example.txt", "w")
# file.write("Hello, this is a test.\nSecond line.")
# #file.close()  

# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()


# with open("example.txt", "w") as file:
#     file.write("Hello, this is a test.\nSecond line.")
try:
    with open("example2.txt", "r") as file:
        content = file.read()
        print(content)
finally:
    print("done")