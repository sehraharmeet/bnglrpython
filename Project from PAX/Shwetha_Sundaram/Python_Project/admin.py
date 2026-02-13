class Admin:
    def __init__(self, username="admin", password="admin123"):
        self.username = username
        self.password = password

    def add_stock(self, market, symbol, price):
        market.add_stock(symbol, price)
        print(f"Stock {symbol} added with price {price}")
            

    def remove_stock(self, market, symbol):
        if symbol in market.prices:
            del market.prices[symbol]
            print(f"Stock {symbol} removed")
        else:
            print("Stock not found!")

    def view_all_stocks(self, market):
        print("\n--- Available Stocks ---")
        for symbol, price in market.prices.items():
            print(f"{symbol}: {price}")
