import json
from models import User

DATA_FILE="data.json"

def load_data():
    with open(DATA_FILE,"r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE,"w") as file:
        json.dump(data,file,indent=4)

def register(username, password, role="user"):
    data=load_data()
    for user in data["users"]:
        if user["username"]==username:
            raise Exception("User already exists")
    
    new_user=User(username,password,role)
    data["users"].append(new_user.__dict__)
    save_data(data)

def login(username, password):
    data=load_data()
    for user in data["users"]:
        if user["username"]==username and user["password"]==password:
            return User(**user)
    raise Exception("Invalid Credentials")