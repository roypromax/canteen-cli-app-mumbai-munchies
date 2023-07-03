import json

file = open("inventory.json","r")
inventory = json.load(file)
file.close()

file = open("sales.json","r")
sales = json.load(file)
file.close()

def main_menu():
    print("-----------------------------------------------------------------")
    print("Welcome to the Mumbai Munchies Snack Inventory Management System!")
    print("-----------------------------------------------------------------")
    print("1. Add a snack")
    print("2. View inventory")
    print("3. Remove a snack")
    print("4. Update availability of a snack")
    print("5. Sell a snack")
    print("6. View sales")
    print("7. Exit")
    print("-----------------------------------------------------------------")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_snack()
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        remove_snack()
    elif choice == "4":
        update_availability()
    elif choice == "5":
        sell_snack()
    elif choice == "6":
        view_sales()
    elif choice == "7":
        exit_app()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def add_snack():
    ID = int(input("Enter snack ID: "))
    for item in inventory:
        if item["ID"] == ID:
            print("-----------------------------------------------------------------")
            print("Snack ID already exists. Try again with a different ID.")
            print("-----------------------------------------------------------------")
            return add_snack()

    name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    availability = input("Enter availability (yes or no): ")

    if availability.lower() not in ["yes", "no"]:
        print("-----------------------------------------------------------------")
        print("Invalid input: Please enter 'yes' or 'no'. Try again.")
        print("-----------------------------------------------------------------")
        return add_snack()

    newSnack = {"ID": ID, "name": name, "price": price, "availability": availability}
    inventory.append(newSnack)

    print("-----------------------------------------------------------------")
    print("New snack has been added to the inventory")
    print("-----------------------------------------------------------------")

    input()
    main_menu()


def view_inventory():
    print("-----------------------------------------------------------------")
    print("Inventory:")
    print("-----------------------------------------------------------------")

    if not inventory:
        print("Inventory is currently empty.")
    else:
        print("ID     Name           Price       Availability")
        print("----------------------------------------------")
        for item in inventory:
            print("{:<5}  {:<12}  ₹{:<10.2f}  {}".format(item['ID'], item['name'], item['price'], item['availability']))


    print("-----------------------------------------------------------------")
    input()
    main_menu()


def remove_snack():
    ID = int(input("Enter snack ID to be deleted: "))
    for item in inventory:
        if item["ID"] == ID:
            inventory.remove(item)
            print("-----------------------------------------------------------------")
            print(f"{item['name']} has been deleted from the inventory")
            print("-----------------------------------------------------------------")
            input()
            return main_menu()
    
    print("-----------------------------------------------------------------")
    print("Snack ID not found in the inventory.")
    print("-----------------------------------------------------------------")
    input()
    main_menu()


def update_availability():
    ID = int(input("Enter ID of snack to update availablity : "))
    for item in inventory : 
        if item["ID"]==ID:
            print("-----------------------------------------------------------------")
            print(f"The availability of {item['name']} is {item['availability']}")
            print("-----------------------------------------------------------------")
            task = int(input("Enter 1 to change availability or enter 2 for main menu : "))
            if task==1:
                if item["availability"]=="yes":
                    item["availability"]="no"
                elif item["availability"]=="no":
                    item["availability"]="yes"
                print("-----------------------------------------------------------------")
                print(f"Availability of {item['name']} has been updated to {item['availability']}")
                print("-----------------------------------------------------------------")
                input()
                return main_menu()
            elif task==2:
                return main_menu()
            else :
                print("-----------------------------------------------------------------")
                print("Invalid input: Please enter '1' or '2'. Try again.")
                print("-----------------------------------------------------------------")
                input()
                return main_menu()

    print("-----------------------------------------------------------------")
    print("Snack ID not found in the inventory.")
    print("-----------------------------------------------------------------")
    input()
    main_menu()
    
def sell_snack():
    ID = int(input("Enter ID of snack to sell : "))
    for item in inventory:
        if item["ID"]==ID:
            if item["availability"]=="no":
                print("-----------------------------------------------------------------")
                print(f"{item['name']} is not available")
                print("-----------------------------------------------------------------")
                input()
                return main_menu()
            elif item["availability"]=="yes":
                quantity = int(input("Enter quantity : "))
                newSale = {}
                newSale["ID"] = item["ID"]
                newSale["name"] = item["name"]
                newSale["price"] = item["price"]
                newSale["quantity"] = quantity
                newSale["saleValue"] = quantity*item["price"]
                sales.append(newSale)
                print("-----------------------------------------------------------------")
                print("Sale has been registered")
                print("-----------------------------------------------------------------")
                input()
                return main_menu()
    
    print("-----------------------------------------------------------------")
    print("Snack ID not found in the inventory.")
    print("-----------------------------------------------------------------")
    input()
    main_menu()

def view_sales():
    print("-----------------------------------------------------------------")
    print("Sales:")
    print("-----------------------------------------------------------------")
    print("{:<5}  {:<15}  {:<10}  {:<15}  {:<15}".format("ID", "Name", "Price", "Quantity Sold", "Sale Value"))
    print("--------------------------------------------------------------")

    for item in sales:
        print("{:<5}  {:<15}  {:<10}  {:<15}  {:<15}".format(
            item["ID"], item["name"], "₹" + str(item["price"]), item["quantity"], "₹" + str(item["saleValue"])))

    print("-----------------------------------------------------------------")
    input()
    main_menu()


def exit_app():
    file = open("inventory.json","w")
    json.dump(inventory,file)
    file.close()

    file = open("sales.json","w")
    json.dump(sales,file)
    file.close()

    print("-----------------------------------------------------------------")
    print("Data saved. Exiting the application.")
    print("-----------------------------------------------------------------")

    exit()
        
main_menu()