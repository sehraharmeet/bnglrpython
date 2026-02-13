from ui.menu import main_menu
from controllers.auth_controller import AuthController
from controllers.dashboard_controller import DashboardController


def main():
    auth_controller = AuthController()
    dashboard_controller = DashboardController()

    while True:
        choice = main_menu()

        if choice == "1":
            auth_controller.register()

        elif choice == "2":
            if auth_controller.login():
                dashboard_controller.show_dashboard()

        elif choice == "3":
            print("Market View - Coming Soon")

        elif choice == "4":
            print("Help Section - Coming Soon")

        elif choice == "5":
            print("Smart Portfolio Manager v1.0")
            print("Built as Fintech Simulation Project")

        elif choice == "6":
            print("Exiting application...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
