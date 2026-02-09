import sys

# for s in sys.argv:
#     print(s)
if(len(sys.argv)>3):
    if(sys.argv[3]=="json"):
        print("welcome to json way")
    elif(sys.argv[3]=="xml"):
        print("welcome to xml way")
    else:
        print("sorry")
else:
        print("Invalid no of arg, please provide 3 more para")