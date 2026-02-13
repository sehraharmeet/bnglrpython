books = []
inventory = {}
transactions = [] 


def add_book():
    title = input("Enter book title: ")

    if title in books:
        print("Book already exists! Updating stock instead.")
        restock_book()
        return

    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))

    books.append(title)
    inventory[title] = {"price": price, "stock": stock}

    print("Book added successfully!")


def restock_book():
    title = input("Enter book title to restock: ")

    if title not in books:
        print("Book not found!")
        return

    qty = int(input("Enter quantity to add: "))
    inventory[title]["stock"] += qty

    print("Stock updated!")


def update_price():
    title = input("Enter book title to update price: ")

    if title not in books:
        print("Book not found!")
        return

    new_price = float(input("Enter new price: "))
    inventory[title]["price"] = new_price

    print("Price updated!")


def remove_book():
    title = input("Enter book title to remove: ")

    if title in books:
        books.remove(title)
        del inventory[title]
        print("Book removed successfully!")
    else:
        print("Book not found!")


def purchase_book():
    title = input("Enter book title to purchase: ")

    if title not in books:
        print("Book not available!")
        return

    qty = int(input("Enter quantity: "))

    if inventory[title]["stock"] < qty:
        print("Insufficient stock!")
        return

    total_cost = qty * inventory[title]["price"]
    inventory[title]["stock"] -= qty

    transactions.append((title, qty, total_cost))

    print(f"Purchase successful! Total cost: {total_cost}")


def display_summary():
    print("\n------ Inventory ------")
    for title in books:
        print(f"{title} -> Price: {inventory[title]['price']}, Stock: {inventory[title]['stock']}")

    total_sales = sum(t[2] for t in transactions)

    print("\n------ Transactions ------")
    for t in transactions:
        print(t)

    print(f"\nTotal Sales: {total_sales}")


while True:
    print("\n===== Bookstore Menu =====")
    print("1. Add Book")
    print("2. Restock Book")
    print("3. Update Price")
    print("4. Remove Book")
    print("5. Purchase Book")
    print("6. Display Summary")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        restock_book()
    elif choice == "3":
        update_price()
    elif choice == "4":
        remove_book()
    elif choice == "5":
        purchase_book()
    elif choice == "6":
        display_summary()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")

