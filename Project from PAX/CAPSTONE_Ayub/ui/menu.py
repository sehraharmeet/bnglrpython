def main_menu():
    print("\n===== SMART PORTFOLIO MANAGER =====")
    print("1. Register")
    print("2. Login")
    print("3. View Market (Guest)")
    print("4. Help")
    print("5. About")
    print("6. Exit")
    return input("Choose option: ")


def dashboard_menu():
    print("\n===== DASHBOARD =====")
    print("1. Funds Management")
    print("2. Market")
    print("3. Portfolio")
    print("4. Trading")
    print("5. Logout")
    return input("Choose option: ")


def funds_menu():
    print("\n--- Funds Management ---")
    print("1. Add Funds")
    print("2. Withdraw Funds")
    print("3. View Balance")
    print("4. Back")
    return input("Choose option: ")


def market_menu():
    print("\n--- Market ---")
    print("1. View All Stocks")
    print("2. Search Stock")
    print("3. Back")
    return input("Choose option: ")


def portfolio_menu():
    print("\n--- Portfolio ---")
    print("1. View Portfolio")
    print("2. View Profit/Loss")
    print("3. Back")
    return input("Choose option: ")


def trading_menu():
    print("\n--- Trading ---")
    print("1. Buy Stock")
    print("2. Sell Stock")
    print("3. View Transaction History")
    print("4. Back")
    return input("Choose option: ")
