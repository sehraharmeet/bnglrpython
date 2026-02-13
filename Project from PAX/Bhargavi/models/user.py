from .portfolio import portfolio
from models.stock import stock

class user:
    def __init__(self, username: str, password: str, initial_cash: float = 100000.0):
        self.username = username
        self.password = password 
        self.portfolio = portfolio(initial_cash)

    def check_password(self, entered_password: str) -> bool:
        return self.password == entered_password

    def get_role(self) -> str:
        return type(self).__name__

    def get_menu_options(self) -> list[str]:
        return [
            "View Portfolio",
            "Buy Stock",
            "Sell Stock",
            "View Market Prices",
            "Logout"
        ]

    def handle_special_action(self, option: str, stocks: dict, users: dict) -> bool:
        return False


class customer(user):
    pass


class admin(user):
    def __init__(self, username: str, password: str):
        super().__init__(username, password, initial_cash=0.0)

    def get_menu_options(self) -> list[str]:
        return super().get_menu_options() + [
            "Add New Stock",
            "Update Stock Price",
            "View All Users",
            "Delete User"
        ]

    def handle_special_action(self, option: str, stocks: dict, users: dict) -> bool:
        if option == "Add New Stock":
            symbol = input("Enter stock symbol: ").strip().upper()
            if symbol in stocks:
                print("Symbol already exists.")
                return True

            name = input("Enter company name: ").strip()
            
            try:
                price = float(input("Enter initial price: "))
                if price <= 0:
                    print("Price must be positive.")
                    return True
            except ValueError:
                print("Invalid price. Please enter a number.")
                return True

            stocks[symbol] = stock(symbol, name, price)
            print(f"Added {symbol} successfully!")
            return True

        elif option == "Update Stock Price":
            symbol = input("Enter stock symbol: ").strip().upper()
            if symbol not in stocks:
                print("Stock not found.")
                return True

            try:
                new_price = float(input("Enter new price: "))
                if new_price <= 0:
                    print("Price must be positive.")
                    return True
                stocks[symbol].price = new_price
                print(f"Price of {symbol} updated to ₹{new_price:,.2f}")
            except ValueError:
                print("Invalid price. Please enter a number.")
            return True

        elif option == "View All Users":
            print("\nRegistered users:")
            for uname, u in users.items():
                print(f"• {uname:12} ({u.get_role():10})  Value: ₹{u.portfolio.total_value():>12,.2f}")
            return True

        elif option == "Delete User":
            target = input("Enter username to delete: ").strip()
            if target == self.username:
                print("Cannot delete yourself.")
            elif target in users:
                del users[target]
                print(f"User {target} deleted.")
            else:
                print("User not found.")
            return True

        return False