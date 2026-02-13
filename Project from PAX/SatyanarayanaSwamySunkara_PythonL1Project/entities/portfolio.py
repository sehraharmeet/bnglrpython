

class Portfolio:

    def buy(self, user, market, stock, qty):
        price = market.get_price(stock)
        user.buy_stock(stock, qty, price)

    def sell(self, user, market, stock, qty):
        price = market.get_price(stock)
        user.sell_stock(stock, qty, price)

    def profit_loss(self, user, market):
        total = 0
        for s, d in user.stocks.items():
            current = market.get_price(s)
            total += (current - d["avg"]) * d["qty"]
        return total