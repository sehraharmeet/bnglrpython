from models.stock import stock
from models.user import user, customer, admin
from utils.file_handler import load_stocks, load_users, save_users, save_stocks

def clear_screen():
    print("\033c", end="")

def show_header():
    print("=" * 60)
    print("      SMART PORTFOLIO MANAGER - Simulator      ")
    print("=" * 60)

def display_available_stocks(stocks):
    """Show list of available stocks in a nice table"""
    if not stocks:
        print("No stocks available in the market.")
        return

    print("\nAvailable Stocks:")
    print("-" * 70)
    print(f"{'Symbol':<10} {'Company Name':<35} {'Current Price (₹)':>15}")
    print("-" * 70)
    
    for s in sorted(stocks.values(), key=lambda x: x.symbol):
        print(f"{s.symbol:<10} {s.name:<35} {s.price:>15,.2f}")
    
    print("-" * 70)

def main():
    stocks = load_stocks()
    users = load_users(stocks)
    current_user: user | None = None

    while True:
        clear_screen()
        show_header()

        if current_user is None:
            print("1. Register")
            print("2. Login")
            print("0. Exit")
        else:
            print(f"Logged in as: {current_user.username}  ({current_user.get_role()})")
            print("-" * 60)
            options = current_user.get_menu_options()
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")
            print("0. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "0":
            if current_user:
                save_users(users)
            print("\nGoodbye! See you again.")
            break

        if current_user is None:
            if choice == "1":  
                username = input("Username: ").strip()
                if username in users:
                    print("Username already taken.")
                    input("Press Enter...")
                    continue

                role = input("Role (customer / admin): ").strip().lower()
                password = input("Password: ")

                if role == "admin":
                    u = admin(username, password)
                else:
                    u = customer(username, password)

                users[username] = u
                save_users(users)
                print(f"Registered successfully as {u.get_role()}!")
                input("Press Enter...")

            elif choice == "2":  
                username = input("Username: ").strip()
                password = input("Password: ")
                if username in users and users[username].check_password(password):
                    current_user = users[username]
                    print(f"Welcome, {username}!")
                else:
                    print("Invalid credentials.")
                input("Press Enter...")

        else:  
            try:
                idx = int(choice) - 1
                selected = current_user.get_menu_options()[idx]
            except:
                print("Invalid choice.")
                input("Press Enter...")
                continue

            handled = current_user.handle_special_action(selected, stocks, users)

            if not handled:
                if selected == "View Portfolio":
                    print("\n" + str(current_user.portfolio))

                elif selected == "Buy Stock":
                    
                    display_available_stocks(stocks)

                    symbol = input("\nEnter stock symbol to buy: ").strip().upper()

                    if symbol not in stocks:
                        print("Stock not found in the market.")
                    else:
                        try:
                            qty = int(input(f"Enter quantity for {symbol}: "))
                            if qty <= 0:
                                print("Quantity must be positive.")
                            elif current_user.portfolio.buy(stocks[symbol], qty):
                                print(f"Success! Bought {qty} shares of {symbol}")
                                save_users(users)
                            else:
                                print("Buy failed: insufficient cash or invalid quantity")
                        except ValueError:
                            print("Please enter a valid number for quantity.")

                elif selected == "Sell Stock":
                    if not current_user.portfolio.holdings:
                        print("You don't own any stocks yet.")
                    else:
                        print("\nYour Current Holdings:")
                        print("-" * 60)
                        print(f"{'Symbol':<10} {'Qty':>8} {'Current Value (₹)':>18}")
                        print("-" * 60)
                        for item in current_user.portfolio.holdings.values():
                            print(f"{item.stock.symbol:<10} {item.quantity:>8} {item.current_value:>18,.2f}")
                        print("-" * 60)

                        symbol = input("\nEnter stock symbol to sell: ").strip().upper()
                        if symbol not in current_user.portfolio.holdings:
                            print("You don't own this stock.")
                        else:
                            try:
                                qty = int(input(f"Enter quantity to sell: "))
                                if current_user.portfolio.sell(symbol, qty):
                                    print(f"Success! Sold {qty} shares of {symbol}")
                                    save_users(users)
                                else:
                                    print("Sell failed: invalid quantity or not owned")
                            except ValueError:
                                print("Please enter a valid number.")

                elif selected == "View Market Prices":
                    display_available_stocks(stocks)

            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()