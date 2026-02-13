import json
import os


# ---------------- FILE MANAGER ----------------

class FileManager:

    @staticmethod
    def load_data(filename):
        try:
            if not os.path.exists(filename):
                return []
            with open(filename, "r") as file:
                return json.load(file)
        except:
            return []

    @staticmethod
    def save_data(filename, data):
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
        except:
            print("Error saving data.")


# ---------------- ADMIN CLASS ----------------

class Admin:

    def __init__(self):
        self.admin_file = "admin.json"
        self.stock_file = "stocks.json"
        self.user_file = "users.json"

    def create_admin(self):
        admins = FileManager.load_data(self.admin_file)

        if admins:
            print("Admin already exists.")
            return

        try:
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
        except:
            print("Invalid input.")
            return

        admins.append({
            "username": username,
            "password": password
        })

        FileManager.save_data(self.admin_file, admins)
        print("Admin created successfully.")

    def login(self):
        admins = FileManager.load_data(self.admin_file)

        if not admins:
            print("No admin found. Create admin first.")
            return False

        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
        except:
            print("Invalid input.")
            return False

        if username == admins[0]["username"] and password == admins[0]["password"]:
            print("Admin login successful.")
            return True
        else:
            print("Invalid credentials.")
            return False

    def create_stock(self):
        stocks = FileManager.load_data(self.stock_file)

        try:
            name = input("Enter stock name: ")
            if not name.strip():
                print("Name cannot be empty.")
                return
            price = float(input("Enter stock price: "))
            if price <= 0:
                print("Price must be positive.")
                return
            quantity = int(input("Enter stock quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                return
        except:
            print("Invalid input.")
            return

        stocks.append({
            "symbol": name,
            "price": price,
            "quantity": quantity
        })

        FileManager.save_data(self.stock_file, stocks)
        print("Stock created successfully.")

    def view_stocks(self):
        stocks = FileManager.load_data(self.stock_file)

        if not stocks:
            print("No stocks available.")
            return

        for i, stock in enumerate(stocks):
            print(i + 1, stock["symbol"], "Price:", stock["price"], "Qty:", stock["quantity"])

    def modify_price(self):
        stocks = FileManager.load_data(self.stock_file)
        self.view_stocks()

        try:
            choice = int(input("Select stock number to modify price: "))
            new_price = float(input("Enter new price: "))
        except:
            print("Invalid input.")
            return

        if 1 <= choice <= len(stocks):
            stocks[choice - 1]["price"] = new_price
            FileManager.save_data(self.stock_file, stocks)
            print("Price updated successfully.")
        else:
            print("Invalid selection.")

    def modify_quantity(self):
        stocks = FileManager.load_data(self.stock_file)
        self.view_stocks()

        try:
            choice = int(input("Select stock number to modify quantity: "))
            new_qty = int(input("Enter new quantity: "))
        except:
            print("Invalid input.")
            return

        if 1 <= choice <= len(stocks):
            stocks[choice - 1]["quantity"] = new_qty
            FileManager.save_data(self.stock_file, stocks)
            print("Quantity updated successfully.")
        else:
            print("Invalid selection.")

    def create_user(self):
        users = FileManager.load_data(self.user_file)

        try:
            name = input("Enter user name: ")
            if not name.strip():
                print("Name cannot be empty.")
                return
        except:
            print("Invalid input.")
            return

        users.append({
            "name": name,
            "cash": 0,
            "portfolio": {}
        })

        FileManager.save_data(self.user_file, users)
        print("User created successfully.")


# ---------------- USER CLASS ----------------

class User:

    def __init__(self):
        self.user_file = "users.json"
        self.stock_file = "stocks.json"

    def select_user(self):
        users = FileManager.load_data(self.user_file)

        if not users:
            print("No users available.")
            return None, None, None

        for i, user in enumerate(users):
            print(i + 1, user["name"])

        try:
            choice = int(input("Select user: "))
        except:
            print("Invalid input.")
            return None, None, None

        if 1 <= choice <= len(users):
            return users[choice - 1], users, choice - 1
        else:
            print("Invalid selection.")
            return None, None, None

    def add_funds(self):
        user, users, index = self.select_user()
        if not user:
            return

        try:
            amount = float(input("Enter amount to add: "))
            if amount <= 0:
                print("Amount must be positive.")
            return
        except:
            print("Invalid input.")
            return

        user["cash"] += amount
        users[index] = user
        FileManager.save_data(self.user_file, users)
        print("Funds added successfully.")

    def buy_stock(self):
        user, users, index = self.select_user()
        if not user:
            return

        stocks = FileManager.load_data(self.stock_file)

        if not stocks:
            print("No stocks available.")
            return

        for i, stock in enumerate(stocks):
            print(i + 1, stock["symbol"], "Price:", stock["price"], "Qty:", stock["quantity"])

        try:
            choice = int(input("Select stock number: "))
            quantity = int(input("Enter quantity to buy: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                return
        except:
            print("Invalid input.")
            return

        if 1 <= choice <= len(stocks):
            stock = stocks[choice - 1]

            if quantity > stock["quantity"]:
                print("Not enough stock available.")
                return

            total_cost = stock["price"] * quantity

            if user["cash"] < total_cost:
                print("Insufficient funds. Please add funds.")
                return

            user["cash"] -= total_cost
            stock["quantity"] -= quantity

            if stock["symbol"] in user["portfolio"]:
                user["portfolio"][stock["symbol"]]["quantity"] += quantity
            else:
                user["portfolio"][stock["symbol"]] = {
                    "quantity": quantity,
                    "avg_price": stock["price"]
                }

            users[index] = user
            stocks[choice - 1] = stock

            FileManager.save_data(self.user_file, users)
            FileManager.save_data(self.stock_file, stocks)

            print("Stock purchased successfully.")
        else:
            print("Invalid selection.")

    def sell_stock(self):
        user, users, index = self.select_user()
        if not user:
            return

        if not user["portfolio"]:
            print("No stocks to sell.")
            return

        stocks = FileManager.load_data(self.stock_file)

        symbols = list(user["portfolio"].keys())

        for i, sym in enumerate(symbols):
            print(i + 1, sym, "Qty:", user["portfolio"][sym]["quantity"])

        try:
            choice = int(input("Select stock to sell: "))
            quantity = int(input("Enter quantity to sell: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                return
        except:
            print("Invalid input.")
            return

        if 1 <= choice <= len(symbols):
            symbol = symbols[choice - 1]
            owned_qty = user["portfolio"][symbol]["quantity"]

            if quantity > owned_qty:
                print("Not enough shares to sell.")
                return

            for stock in stocks:
                if stock["symbol"] == name:
                    print("Stock already exists.")
                    return
                elif stock["symbol"] == symbol:
                    sell_price = stock["price"]
                    stock["quantity"] += quantity
                    break

            user["cash"] += sell_price * quantity
            user["portfolio"][symbol]["quantity"] -= quantity

            if user["portfolio"][symbol]["quantity"] == 0:
                del user["portfolio"][symbol]

            users[index] = user

            FileManager.save_data(self.user_file, users)
            FileManager.save_data(self.stock_file, stocks)

            print("Stock sold successfully.")
        else:
            print("Invalid selection.")

    def dashboard(self):
        user, users, index = self.select_user()
        if not user:
            return

        stocks = FileManager.load_data(self.stock_file)

        print("Name:", user["name"])
        print("Cash:", user["cash"])
        print("----------------------")

        for symbol, data in user["portfolio"].items():

            quantity = data["quantity"]
            buy_price = data["avg_price"]
            current_price = 0

            for stock in stocks:
                if stock["symbol"] == symbol:
                    current_price = stock["price"]
                    break

            difference = current_price - buy_price
            amount = difference * quantity

            print("Stock:", symbol)
            print("Quantity:", quantity)
            print("Buy Price:", buy_price)
            print("Current Price:", current_price)

            if amount > 0:
                print("Profit:", amount)
                print("Loss: 0")
            elif amount < 0:
                print("Profit: 0")
                print("Loss:", abs(amount))
            else:
                print("Profit: 0")
                print("Loss: 0")

            print("----------------------")


# ---------------- MAIN MENU ----------------

def main():
    admin = Admin()
    user = User()

    while True:
        print("\n1. Create Admin")
        print("2. Admin Login")
        print("3. User Menu")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Invalid input.")
            continue

        if choice == 1:
            admin.create_admin()

        elif choice == 2:
            if admin.login():
                while True:
                    print("\n1. Create Stock")
                    print("2. View Stocks")
                    print("3. Modify Price")
                    print("4. Modify Quantity")
                    print("5. Create User")
                    print("6. Back")

                    try:
                        admin_choice = int(input("Enter choice: "))
                    except:
                        print("Invalid input.")
                        continue

                    if admin_choice == 1:
                        admin.create_stock()
                    elif admin_choice == 2:
                        admin.view_stocks()
                    elif admin_choice == 3:
                        admin.modify_price()
                    elif admin_choice == 4:
                        admin.modify_quantity()
                    elif admin_choice == 5:
                        admin.create_user()
                    elif admin_choice == 6:
                        break
                    else:
                        print("Invalid choice.")

        elif choice == 3:
            while True:
                print("\n1. Add Funds")
                print("2. Buy Stock")
                print("3. Sell Stock")
                print("4. Dashboard")
                print("5. Back")

                try:
                    user_choice = int(input("Enter choice: "))
                except:
                    print("Invalid input.")
                    continue

                if user_choice == 1:
                    user.add_funds()
                elif user_choice == 2:
                    user.buy_stock()
                elif user_choice == 3:
                    user.sell_stock()
                elif user_choice == 4:
                    user.dashboard()
                elif user_choice == 5:
                    break
                else:
                    print("Invalid choice.")

        elif choice == 4:
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
