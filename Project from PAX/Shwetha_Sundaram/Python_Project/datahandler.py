import json
import os
from User import User

def load_users(filename="users.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return {u: User(u, d["balance"]) for u, d in data.items()}
    except FileNotFoundError:
        return {}

def save_users(users, filename="users.json"):
    data = {u: {"balance": user.balance} for u, user in users.items()}
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except OSError as e:
        print(f"Error saving users: {e}")


def load_stocks(filename="stocks.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)  
    except FileNotFoundError:
        return {}

def save_stocks(stocks, filename="stocks.json"):
    try:
        with open(filename, "w") as f:
            json.dump(stocks, f, indent=4)
    except OSError as e:
        print(f"Error saving stocks: {e}")
