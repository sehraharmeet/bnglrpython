class stock:
    def __init__(self, symbol: str, name: str, price: float):
        self.symbol = symbol.upper()
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.symbol:<10} {self.name:<30} ₹{self.price:>10,.2f}"