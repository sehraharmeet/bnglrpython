import json

class User:
    def __init__(self,username,password,role="user",balance=10000,portfolio=None):
        self.username=username
        self.password=password
        self.role=role
        self.balance=balance
        self.portfolio=portfolio if portfolio is not None else {}
    
    def buy_stock(self,symbol,quantity,price):
        total_cost=quantity*price
        if total_cost>self.balance:
            raise Exception("Insufficient Funds")
        
        self.balance-=total_cost
        self.portfolio[symbol]=self.portfolio.get(symbol,0)+quantity
    
    def sell_stock(self, symbol, quantity, price):
        if symbol not in self.portfolio or self.portfolio[symbol] < quantity:
            raise Exception("Not enough stocks to sell")
        
        self.balance += quantity * price
        self.portfolio[symbol] -= quantity

    def calculate_portfolio_value(self, stock_data):
        total=0
        for symbol, quantity in self.portfolio.items():
            total += quantity * stock_data[symbol]
        return total
    