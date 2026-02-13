import random
from exceptions import StockNotFoundError
import datahandler

class StockMarket:
    def __init__(self, filename="stocks.json"):
        self.filename = filename
        self.prices = datahandler.load_stocks(filename)

    def get_price(self, symbol):
        if symbol not in self.prices:
            raise StockNotFoundError(f"Stock {symbol} not available in market!")
        self.prices[symbol] += random.randint(-10, 10)
        return self.prices[symbol]

    def add_stock(self, symbol, price):
        self.prices[symbol] = price
        datahandler.save_stocks(self.prices, self.filename)  
       # print(f"Stock {symbol} added with price {price}")

    def remove_stock(self, symbol):
        if symbol in self.prices:
            del self.prices[symbol]
            datahandler.save_stocks(self.prices, self.filename)  
            print(f"Stock {symbol} removed")
        else:
            raise StockNotFoundError(f"Stock {symbol} not available in market!")
