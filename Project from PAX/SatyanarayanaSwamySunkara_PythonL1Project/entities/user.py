from utils.exceptions import InsufficientBalance, StockNotFound

class User:
    def __init__(self, username, password, balance=0, stocks=None):
        self.username = username
        self.password = password
        self.balance = balance
        self.stocks = stocks if stocks else {}

    def add_money(self, amt):
        self.balance += amt

    def deduct_money(self, amt):
        if self.balance < amt:
            raise InsufficientBalance("Not enough balance")
        self.balance -= amt

    def buy_stock(self, name, qty, price):
        total = price * qty
        self.deduct_money(total)

        if name in self.stocks:
            self.stocks[name]["qty"] += qty
        else:
            self.stocks[name] = {"qty": qty, "avg": price}

 
    def sell_stock(self, name, qty, price):
        if name not in self.stocks:
            raise StockNotFound("Stock not owned")

        if self.stocks[name]["qty"] < qty:
            raise StockNotFound("Not enough shares")

        self.stocks[name]["qty"] -= qty
        self.balance += price * qty

        if self.stocks[name]["qty"] == 0:
            del self.stocks[name]



    def show_portfolio(self):
        print("Balance:", self.balance)

        if not self.stocks:
            print("No stocks owned")
            return

        for name, data in self.stocks.items():
            print(name, "| Qty:", data["qty"], "| Buy Price:", data["avg"])
