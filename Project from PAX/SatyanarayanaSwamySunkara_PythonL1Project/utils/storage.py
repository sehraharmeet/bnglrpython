import json
from entities.user import User
from entities.market import Market
from entities.request import StockRequest

USERS_FILE = "data/users.json"
MARKET_FILE = "data/market.json"
# REQUEST_FILE = "data/requests.json"

# Loading and Saving Users


def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
    except:
        return {}

    users = {}
    for username, info in data.items():
        users[username] = User(
        username,
        info["password"],
        info.get("balance", 0),
        info.get("stocks", {})
    )
    return users

def save_users(users):
    data = {}
    for username, user in users.items():
        data[username] = {
            "password": user.password,
            "balance": user.balance,
            "stocks": user.stocks
        }

    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)


# Loading and saving market

def load_market():
    try:
        with open(MARKET_FILE, "r") as f:
            stocks = json.load(f)
    except:
        stocks = {}
        
    return Market(stocks)


def save_market(market):
    with open(MARKET_FILE, "w") as f:
        json.dump(market.stocks, f, indent=4)


    


