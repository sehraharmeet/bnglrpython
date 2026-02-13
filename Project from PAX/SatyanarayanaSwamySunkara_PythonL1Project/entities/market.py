from utils.exceptions import StockNotFound

class Market:
    def __init__(self, stocks=None):
        self.stocks = stocks if stocks else {}

    def get_price(self, name):
        if name not in self.stocks:
            raise StockNotFound("Stock not available")
        return self.stocks[name]

    def view_market(self):
        for s, p in self.stocks.items():
            print(s, ":", p)

    def add_stock(self, name, price):
        self.stocks[name] = price

    def remove_stock(self, name):
        if name not in self.stocks:
            raise StockNotFound("Stock not found")
        del self.stocks[name]