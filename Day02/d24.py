# def accept_names():
#     names = []
#     for i in range(1,6):
#         name = input("Enter name {i}: ")
#         names.append(name)
#     return names

# def display_names(names):
#     for name in names:
#         print(name)

# names_list = accept_names()
# display_names(names_list)

names = [input(f"Enter name {i}: ") for i in range(1,6)]
display_name = lambda name: name.upper()
for inf in (list(map(display_name, names))):
    print(inf)
#upper_names = list(map(lambda n: n.upper(), names))
#print(upper_names)
