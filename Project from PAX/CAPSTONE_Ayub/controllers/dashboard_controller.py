from ui.menu import dashboard_menu, funds_menu, market_menu, portfolio_menu, trading_menu

class DashboardController:

    def show_dashboard(self):
        while True:
            choice = dashboard_menu()

            if choice == "1":
                self.handle_funds()

            elif choice == "2":
                self.handle_market()

            elif choice == "3":
                self.handle_portfolio()

            elif choice == "4":
                self.handle_trading()

            elif choice == "5":
                print("Logging out...")
                break

            else:
                print("Invalid choice")

    def handle_funds(self):
        while True:
            choice = funds_menu()

            if choice == "1":
                print("Add Funds - Coming Soon")
            elif choice == "2":
                print("Withdraw Funds - Coming Soon")
            elif choice == "3":
                print("View Balance - Coming Soon")
            elif choice == "4":
                break
            else:
                print("Invalid choice")

    def handle_market(self):
        while True:
            choice = market_menu()

            if choice == "1":
                print("View All Stocks - Coming Soon")
            elif choice == "2":
                print("Search Stock - Coming Soon")
            elif choice == "3":
                break
            else:
                print("Invalid choice")

    def handle_portfolio(self):
        while True:
            choice = portfolio_menu()

            if choice == "1":
                print("View Portfolio - Coming Soon")
            elif choice == "2":
                print("View Profit/Loss - Coming Soon")
            elif choice == "3":
                break
            else:
                print("Invalid choice")

    def handle_trading(self):
        while True:
            choice = trading_menu()

            if choice == "1":
                print("Buy Stock - Coming Soon")
            elif choice == "2":
                print("Sell Stock - Coming Soon")
            elif choice == "3":
                print("Transaction History - Coming Soon")
            elif choice == "4":
                break
            else:
                print("Invalid choice")
