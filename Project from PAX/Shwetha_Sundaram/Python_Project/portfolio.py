from exceptions import InsufficientFundsError, StockNotFoundError

class Portfolio:
    def __init__(self, user):
        self.user = user
        self.holdings = {}  # {symbol: {"qty": int, "avg_price": float}}

    def buy_stock(self, symbol, qty, market):
        price = market.get_price(symbol)
        cost = price * qty
        if self.user.balance < cost:
            raise InsufficientFundsError("Not enough balance to buy stock!")

        self.user.balance -= cost
        if symbol in self.holdings:
            old_qty = self.holdings[symbol]["qty"]
            old_avg = self.holdings[symbol]["avg_price"]
            new_avg = ((old_qty * old_avg) + cost) / (old_qty + qty)
            self.holdings[symbol]["qty"] += qty
            self.holdings[symbol]["avg_price"] = new_avg
        else:
            self.holdings[symbol] = {"qty": qty, "avg_price": price}

        print(f"Bought {qty} shares of {symbol} at {price}")

    def sell_stock(self, symbol, qty, market):
        if symbol not in self.holdings or self.holdings[symbol]["qty"] < qty:
            raise StockNotFoundError(f"Not enough shares of {symbol} to sell!")

        price = market.get_price(symbol)
        revenue = price * qty
        self.user.balance += revenue
        self.holdings[symbol]["qty"] -= qty
        if self.holdings[symbol]["qty"] == 0:
            del self.holdings[symbol]

        print(f"Sold {qty} shares of {symbol} at {price}")

    def view_portfolio(self):
        print("\n--- Portfolio ---")
        for stock, data in self.holdings.items():
            print(f"{stock}: {data['qty']} shares (Avg Price: {data['avg_price']})")
        print(f"Balance: {self.user.balance}")

    def analyze(self, market):
        print("\n--- Profit/Loss Analysis ---")
        total_pl = 0
        for stock, data in self.holdings.items():
            current_price = market.get_price(stock)
            invested = data["qty"] * data["avg_price"]
            current_value = data["qty"] * current_price
            pl = current_value - invested
            total_pl += pl
            print(f"{stock}: Qty={data['qty']}, Avg={data['avg_price']}, "
                  f"Current={current_price}, P/L={pl}")
        print(f"\nTotal Profit/Loss: {total_pl}")
