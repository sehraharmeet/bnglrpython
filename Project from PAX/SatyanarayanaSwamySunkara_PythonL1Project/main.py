from utils.auth import register, login, update_user, admin_login
from utils.storage import load_market, save_market
from entities.portfolio import Portfolio
from utils.exceptions import InvalidLogin, InsufficientBalance, StockNotFound

portfolio = Portfolio()

def admin_panel():
    market = load_market()

    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. View Market")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            market.view_market()

        elif choice == "2":
            name = input("Stock name: ").upper()
            price = int(input("Price: "))
            market.add_stock(name, price)
            save_market(market)
            print("Stock added!")

        elif choice == "3":
            name = input("Stock name: ").upper()
            try:
                market.remove_stock(name)
                save_market(market)
                print("Stock removed!")
            except StockNotFound:
                print("Stock not found")

        elif choice == "4":
            print("Logging out...")
            break

        else:
            print("Please enter a valid choice")

def user_dashboard(user):
    market = load_market()

    while True:
        print(f"\n--- USER DASHBOARD ({user.username}) ---")
        print("1. Add Money")
        print("2. Buy Stock")
        print("3. Sell Stock")
        print("4. View Portfolio")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            amt = int(input("Amount: "))
            user.add_money(amt)
            update_user(user)

        elif choice == "2":
            market.view_market()
            stock = input("Stock: ").upper()
            qty = int(input("Qty: "))
            try:
                portfolio.buy(user, market, stock, qty)
                update_user(user)
                print("Purchased!")
            except InsufficientBalance:
                print("Not enough balance")
            except StockNotFound:
                print("Invalid stock")

        elif choice == "3":
            stock = input("Stock: ").upper()
            qty = int(input("Qty: "))
            try:
                portfolio.sell(user, market, stock, qty)
                update_user(user)
                print("Sold!")
            except StockNotFound:
                print("You don't own enough shares")

        elif choice == "4":
            user.show_portfolio()
            print("Profit/Loss:", portfolio.profit_loss(user, market))

        elif choice == "5":
            print("Logging out...")
            break

        else:
            print("Please enter a valid choice")


while True:
    print("\n====== SMART PORTFOLIO MANAGER ======")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    role = input("Select role: ")

    if role == "1":
        u = input("Admin username: ")
        p = input("Password: ")
        try:
            admin_login(u, p)
            admin_panel()
        except InvalidLogin:
            print("Wrong admin credentials")

    elif role == "2":
        print("\n1. Register")
        print("2. Login")
        choice = input("Choose: ")

        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            try:
                register(u, p)
                print("Account created!")
            except:
                print("User already exists")

        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            try:
                user = login(u, p)
                user_dashboard(user)
            except InvalidLogin:
                print("Invalid login")

        else:
            print("Please enter a valid choice")

    elif role == "3":
        print("Goodbye ")
        break

    else:
        print("Please enter a valid choice")
