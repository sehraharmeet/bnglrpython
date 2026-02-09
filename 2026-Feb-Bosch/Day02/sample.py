customers = []   # list for storage


# Function to add customer
def add_customer():
    print("\n--- Add Customer ---")
    
    cust_id = input("Enter Customer ID: ")
    name = input("Enter Name: ")
    city = input("Enter City: ")
    phone = input("Enter Phone: ")

    customer = {
        "ID": cust_id,
        "Name": name,
        "City": city,
        "Phone": phone
    }

    customers.append(customer)
    print("Customer added successfully!\n")


# Function to display customers
def display_customers():
    print("\n--- Customer List ---")

    if not customers:
        print("No customers found.\n")
        return

    for cust in customers:
        print(f"""
ID    : {cust['ID']}
Name  : {cust['Name']}
City  : {cust['City']}
Phone : {cust['Phone']}
---------------------------""")

# Menu function
def menu():
    while True:
        print("""
========= CUSTOMER MENU =========
1. Add Customer
2. Display Customers
3. Exit
================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            display_customers()

        elif choice == "3":
            print("Exiting application... Goodbye 👋")
            break

        else:
            print("Invalid choice. Try again.\n")


# Start the application
menu()
