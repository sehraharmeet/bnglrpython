import json
from pathlib import Path
from models.stock import stock
from models.user import user, customer, admin
from models.portfolio import portfolioitem, portfolio

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

STOCKS_FILE = DATA_DIR / "stocks.json"
USERS_FILE = DATA_DIR / "users.json"


def load_stocks() -> dict[str, stock]:
    if not STOCKS_FILE.exists():
        default = {
            "RELIANCE": {"name": "Reliance Industries", "price": 2950.75},
            "TCS": {"name": "Tata Consultancy Services", "price": 4200.0},
            "HDFCBANK": {"name": "HDFC Bank", "price": 1650.25},
            "INFY": {"name": "Infosys", "price": 1850.10},
            "ITC": {"name": "ITC Ltd", "price": 480.50},
        }
        save_stocks({k: stock(k, v["name"], v["price"]) for k, v in default.items()})

    with open(STOCKS_FILE, encoding="utf-8") as f:
        data = json.load(f)
    return {k: stock(k, v["name"], v["price"]) for k, v in data.items()}


def save_stocks(stocks: dict[str, stock]):
    data = {s.symbol: {"name": s.name, "price": s.price} for s in stocks.values()}
    with open(STOCKS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_users(stocks: dict[str, stock]) -> dict[str, user]:
    if not USERS_FILE.exists():
        return {}

    with open(USERS_FILE, encoding="utf-8") as f:
        data = json.load(f)

    users = {}
    for uname, udata in data.items():
        user_type = udata.get("type", "customer")
        password = udata.get("password", "")

        if user_type == "admin":
            user_obj = admin(uname, password)
        else:
            user_obj = customer(uname, password)

        port = portfolio(udata.get("cash", 100000.0))
        for sym, holding in udata.get("holdings", {}).items():
            if sym in stocks:
                port.holdings[sym] = portfolioitem(
                    stocks[sym],
                    holding["quantity"],
                    holding["buy_price"]
                )
        user_obj.portfolio = port
        users[uname] = user_obj

    return users


def save_users(users: dict[str, user]):
    data = {}
    for uname, u in users.items():
        holdings = {}
        for sym, item in u.portfolio.holdings.items():
            holdings[sym] = {
                "quantity": item.quantity,
                "buy_price": item.buy_price
            }
        data[uname] = {
            "type": type(u).__name__,
            "password": u.password,
            "cash": u.portfolio.cash,
            "holdings": holdings
        }
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)