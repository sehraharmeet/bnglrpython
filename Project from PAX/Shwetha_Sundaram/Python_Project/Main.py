from User import User
from admin import Admin
from stock_market import StockMarket
import datahandler
from exceptions import InsufficientFundsError, StockNotFoundError

def login_menu():
    print("\n--- Login Menu ---")
    print("1. Admin Login")
    print("2. Investor Login")
    print("3. Register Investor")
    print("4. Exit")

def admin_menu(admin, market):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View All Stocks")
        print("4. Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            price = float(input("Enter price: "))
            admin.add_stock(market, symbol, price)
        elif choice == "2":
            symbol = input("Enter stock symbol: ")
            admin.remove_stock(market, symbol)
        elif choice == "3":
            admin.view_all_stocks(market)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def user_menu(user, market):
    while True:
        print("\n--- Investor Menu ---")
        print("1. View Portfolio")
        print("2. View All Stocks")
        print("3. Buy Stock")
        print("4. Sell Stock")
        print("5. Analyze Profit/Loss")
        print("6. Logout")
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                user.portfolio.view_portfolio()
            elif choice == "2":
                admin = Admin()
                admin.view_all_stocks(market)
            elif choice == "3":
                stock = input("Enter stock symbol: ")
                qty = int(input("Enter quantity: "))
                user.portfolio.buy_stock(stock, qty, market)
            elif choice == "4":
                stock = input("Enter stock symbol: ")
                qty = int(input("Enter quantity: "))
                user.portfolio.sell_stock(stock, qty, market)
            elif choice == "5":
                user.portfolio.analyze(market)
            elif choice == "6":
                break
            else:
                print("Invalid choice!")
        except InsufficientFundsError as e:
            print(f"Error: {e}")
        except StockNotFoundError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input! Please enter numbers where required.")

def run():
    market = StockMarket()
    users = datahandler.load_users()
    admin = Admin()

    while True:
        login_menu()
        choice = input("Enter choice: ")

        if choice == "1": 
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if username == admin.username and password == admin.password:
                admin_menu(admin, market)
            else:
                print("Invalid admin credentials!")

        elif choice == "2":  
            username = input("Enter username: ")
            if username in users:
                user_menu(users[username], market)
            else:
                print("Please register as new user!")

        elif choice == "3":  
            username = input("Enter new username: ")
            if username in users:
                print("Username already exists. Try logging in.")
            else:
                users[username] = User(username)
                datahandler.save_users(users)
                print("Account created successfully! You can now log in.")

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    run()
