from portfolio import Portfolio

class User:
    def __init__(self, username, balance=10000):
        self.username = username
        self.balance = balance
        self.portfolio = Portfolio(self)

    def __repr__(self):
        return f"User({self.username}, Balance={self.balance})"
