from utils.storage import load_users, save_users
from utils.exceptions import InvalidLogin, UserAlreadyExists
from entities.user import User



def register(username, password):
    users = load_users()

    if username in users:
     raise UserAlreadyExists("User already exists")

    users[username] = User(username, password)
    save_users(users)

def login(username, password):
    users = load_users()

    if username not in users or users[username].password != password:
     raise InvalidLogin("Invalid username or password")

    return users[username]


def update_user(user):
    users = load_users()
    users[user.username] = user
    save_users(users)

def admin_login(username, password):
    if username == "Satya" and password == "Satya@185":
        return True
    raise InvalidLogin("Invalid admin credentials")