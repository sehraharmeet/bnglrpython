from typing import Dict
from models.stock import stock

class portfolioitem:
    def __init__(self, stock: stock, quantity: int, buy_price: float):
        self.stock = stock
        self.quantity = quantity
        self.buy_price = buy_price

    @property
    def current_value(self) -> float:
        return self.quantity * self.stock.price

    @property
    def profit_loss(self) -> float:
        return self.current_value - (self.quantity * self.buy_price)

    def __str__(self):
        return (f"{self.quantity:>5} × {self.stock.symbol:<8} "
                f"(buy @ ₹{self.buy_price:>8,.2f}) → "
                f"₹{self.current_value:>10,.2f}  (P/L: ₹{self.profit_loss:+10,.2f})")


class portfolio:
    def __init__(self, initial_cash: float = 100000.0):
        self.cash = initial_cash
        self.holdings: Dict[str, portfolioitem] = {}

    def buy(self, stock: stock, quantity: int) -> bool:
        if quantity <= 0:
            return False
        cost = stock.price * quantity
        if cost > self.cash:
            return False
        self.cash -= cost

        if stock.symbol in self.holdings:
            item = self.holdings[stock.symbol]
            total_qty = item.quantity + quantity
            avg_price = (item.buy_price * item.quantity + stock.price * quantity) / total_qty
            item.quantity = total_qty
            item.buy_price = avg_price
        else:
            self.holdings[stock.symbol] = portfolioitem(stock, quantity, stock.price)
        return True

    def sell(self, symbol: str, quantity: int) -> bool:
        if quantity <= 0 or symbol not in self.holdings:
            return False
        item = self.holdings[symbol]
        if quantity > item.quantity:
            return False

        proceeds = item.stock.price * quantity
        self.cash += proceeds
        item.quantity -= quantity

        if item.quantity == 0:
            del self.holdings[symbol]
        return True

    def total_value(self) -> float:
        holdings_value = sum(item.current_value for item in self.holdings.values())
        return self.cash + holdings_value

    def __str__(self):
        lines = [f"Cash balance:      ₹{self.cash:>12,.2f}",
                 f"Total portfolio:   ₹{self.total_value():>12,.2f}"]
        if self.holdings:
            lines.append("\nHoldings:")
            for item in self.holdings.values():
                lines.append(str(item))
        else:
            lines.append("\nNo holdings yet.")
        return "\n".join(lines)