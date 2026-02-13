from services.auth_service import AuthService


class AuthController:

    def __init__(self):
        self.auth_service = AuthService()

    def register(self):
        print("\n--- Register ---")
        username = input("Username: ")
        password = input("Password: ")
        self.auth_service.register_user(username, password)

    def login(self):
        print("\n--- Login ---")
        username = input("Username: ")
        password = input("Password: ")
        return self.auth_service.login_user(username, password)
