
import ast
import os

USER_FILE = "user.txt"
STOCK_MASTER = "stockmaster.txt"
LOG_IN = "False"
USER = ""
EXIT = "False"
modified_list = []

class User:   
    def create_user(self):
        name = input("Enter Username: ")
        password = input("Enter Password: ")

        user_list = [name, password]
       
        if not os.path.exists(USER_FILE):
            open(USER_FILE, "w").close()
        
        with open(USER_FILE, "r") as file:
            for line in file:
                stored_user = ast.literal_eval(line.strip())
                if stored_user[0] == name:
                    print("Username already exists!")
                    return

        
        with open(USER_FILE, "a") as file:
            file.write(str(user_list) + "\n")

        print(f"User '{name}' created successfully!")

    def login_user(self):
        global LOG_IN,USER 
        if not os.path.exists(USER_FILE):
            print("No users found. Please create an account first.")
            return

        name = input("Enter Username: ")
        password = input("Enter Password: ")

        with open(USER_FILE, "r") as file:
            for line in file:
                stored_user = ast.literal_eval(line.strip())
                if stored_user[0] == name and stored_user[1] == password:
                    print(f"\n LogIn Succesfull - {name}!")
                    LOG_IN = "True"
                    USER = name
                    
            if LOG_IN != "True":
                    print("Invalid Username or Password.")
        #return

    def admin(self):
            global USER,EXIT
            admin_choice = input("Enter your choice: ")

            if admin_choice == "1": #for adding new stock
                stock_name = input("Enter stock name: ")
                stock_code = input("Enter stock code : ")
                stock_QTY = int(input("Enter stock shares quantity: "))
                stock_price = float(input("Enter stock share price : "))
                
                stock_list = [stock_name,stock_code,stock_QTY,stock_price]

                if not os.path.exists(STOCK_MASTER):
                    open(STOCK_MASTER, "w").close()
                    
                with open(STOCK_MASTER, "r") as file:
                    for line in file:
                        stored_stock = ast.literal_eval(line.strip())
                        if stored_stock[1] == stock_code:
                            print(f"stock name/code '{stock_code}' already exists!")
                            return
                
                with open(STOCK_MASTER, "a") as file:
                    file.write(str(stock_list) + "\n")

                print(f"stock '{stock_name}' created successfully!")
            elif admin_choice == "2": #To modify existing stock name, quantity and price
                stock_code = input("Enter stock code to be modified : ")
                stock_name = input("Enter stock new name: ")
                stock_QTY = int(input("Enter quantity to be added: "))
                stock_price = float(input("Enter new price : "))
                stored_stock=[]
                # stock_list = [stock_name,stock_code,stock_QTY,stock_price]

                if not os.path.exists(STOCK_MASTER):
                    open(STOCK_MASTER, "w").close()
                    
                with open(STOCK_MASTER, "r") as file:
                    modified_list = []
                    for line in file:
                        stored_stock = ast.literal_eval(line.strip())
                        print(f"==>{stored_stock[1]}{stock_code}")
                        if stored_stock[1] != stock_code:
                            print(f"stock code '{stock_code}' not valid!")
                            
                        elif stored_stock[1] == stock_code:
                            stored_stock[0] = stock_name
                            stored_stock[2] = stored_stock[2]+stock_QTY
                            stored_stock[3] = stock_price
                            stock_list = [stored_stock[0],stored_stock[1],stored_stock[2],stored_stock[3]]
                        modified_list.append(stored_stock)
                open(STOCK_MASTER, "w").close()
                for modified_line in modified_list:
                    with open(STOCK_MASTER, "a") as file:
                        file.write(str(modified_line) + "\n")

                print(f"stock '{stock_name}' updated successfully!")
                
            elif admin_choice == "3":
                print(f"User' {USER}' loggedoff succesfully")
                EXIT = "True"

            else:
                print(f"Hello {USER}' Invalid choice. Try again.")

    def trade_user(self):
            global USER,EXIT
            user_choice = input("Enter your choice: ")
            if user_choice == "1": #to display dashboard
                print(f"Hello '{USER}' Dashboard application desig in progress")
            elif user_choice == "2": #to buy stock
                print(f"Hello '{USER}' Stock buy application desig in progress")
            elif user_choice == "3": #to sell stock
                print(f"Hello '{USER}' Sell stock application desig in progress")
            elif user_choice == "4": # logoff
                print(f"User' '{USER}' loggedoff succesfully")
                EXIT = "True"
            else:
                print(f"Hello '{USER}' Invalid choice. Try again.")

        #print(f"Wecome trade user - {USER}")
    
def main():
    global LOG_IN,USER,EXIT
    obj=User()
    while True:

        print("""
========= Welcome to Trading App =========
1. New User (Sign Up)
2. Existing User (Login)
3. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            obj.create_user()

        elif choice == "2":
            obj.login_user()
            if LOG_IN == "True":
                if USER == "Admin":
                    while True:
                        print("""
                            ========= Welcome ADMIN =========
                            1. Add New Stock to StockMaster
                            2. Edit StockMaster
                            3. Logoff
                            """)
                        obj.admin()
                        if EXIT == "True":
                            break
                else:
                    while True:
                        print("""
                            ========= Welcome to Trading App =========
                            1. Dashboard
                            2. Buy Stock
                            3. Sell stock
                            4. Logoff
                            """)
                        obj.trade_user()
                        if EXIT == "True":
                            break

          
        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
