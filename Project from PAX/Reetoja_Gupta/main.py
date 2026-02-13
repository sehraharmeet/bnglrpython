from services import register, login, load_data, save_data

def main():
    print("*======================================*")
    print("Welcome to Smart Portfolio Manager")
    print("*======================================*")
    choice=input("1. Register\n2. Login\nChoose: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (admin/user): ")
        register(username, password, role)
        print("Registration successful!")

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        user = login(username, password)
        print("-----------------------------------")
        print(f"Welcome {user.username} - Role: {user.role}")

        data = load_data()
        stocks = data["stocks"]

        while True:
            print("\n1. Buy\n2. Sell\n3. View Portfolio\n4. Exit")
            action = input("Choose: ")

            if action == "1":
                symbol = input("Stock symbol - AAPL/TSLA/GOOGL/MSFT")
                quantity = int(input("Quantity: "))
                user.buy_stock(symbol, quantity, stocks[symbol])
                print(f"{quantity} Stock bought!")

            elif action == "2":
                symbol = input("Stock symbol - AAPL/TSLA/GOOGL/MSFT")
                quantity = int(input("Quantity: "))
                user.sell_stock(symbol, quantity, stocks[symbol])
                print(f"{quantity} Stock sold!")

            elif action == "3":
                value = user.calculate_portfolio_value(stocks)
                print("Portfolio:", user.portfolio)
                print("Balance:", user.balance)
                print("Portfolio Value:", value)

            elif action == "4":
                data["users"] = [
                    u if u["username"] != user.username else user.__dict__
                    for u in data["users"]
                ]
                save_data(data)
                break

if __name__ == "__main__":
    main()

