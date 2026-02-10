# import os
# print(os.getcwd())
# print(os.listdir())

# import os

# cur = os.getcwd()
# print(os.listdir(cur + r"\support"))


import os

cur = os.getcwd()
sup = os.path.join(cur, "bnglr","support")

print(os.listdir(sup))