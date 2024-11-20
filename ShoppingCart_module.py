from prettytable import PrettyTable

# Global database
ItemsInCart = []

# Calculate the total cost of the cart
def totalCost():
    addTotal = sum(item[4] for item in ItemsInCart)
    print(f'''
     +--------------+----------------------------+
     | Total Amount | {addTotal} rs.       |
     +--------------+----------------------------+
''')

# Print all items in the cart along with the total cost
def printCartItems():
    cartTable = PrettyTable(["Selected ID", "Item Name", "Price/1qt", "Quantity", "Total"])
    for item in ItemsInCart:
        cartTable.add_row(item)
    print(cartTable)
    totalCost()

# Add items to the cart, or update quantity if the item already exists
def addItemInCart(itemName, itemPrice, selector_id):
    print("\nIf you don't want to add more items, then Enter '-1' \n")
    while True:
        selected_id = getValidSelectedItem(selector_id)
        if selected_id == -1:
            printCartItems()
            return
        item_name = itemName[selected_id]
        price = itemPrice[selected_id]
        quantity = getQuantity()
        updateCart(selected_id=selected_id, item_name=item_name, price=price, quantity=quantity)

# Validate the item selected by the user
def getValidSelectedItem(selector_id):
    while True:
        try:
            selectedItem = int(input("Select Item by ID: "))
            if selectedItem in selector_id or selectedItem == -1:
                return selectedItem
            else:
                print("Invalid ID! Try again.")
        except ValueError:
            print("Invalid input! Enter a valid ID.")

# Get the quantity of an item
def getQuantity():
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity > 0:
                return quantity
            else:
                print("Please enter a +ve number.")
        except ValueError:
            print("Invalid quantity!")

# Update cart if the item already exists, else add a new entry
def updateCart(selected_id, item_name, price, quantity):
    # Check if item already exists in the cart
    for item in ItemsInCart:
        if item[0] == selected_id:
            # If the item exists, update its quantity and total price
            item[3] += quantity
            item[4] = item[3] * item[2]  # Update total price
            print(f"Updated {item_name}'s quantity to {item[3]}")
            return
    
    # If item doesn't exist, add it to the cart
    addToDatabase(selected_id, item_name, price, quantity)

# Add the selected item to the cart
def addToDatabase(selected_id, item_name, price, quantity):

    allData = [selected_id, item_name, price, quantity, price * quantity]
    ItemsInCart.append(allData)

# Remove an item from the cart by its ID
def removeItemFromCart():
    if not ItemsInCart:
        print("The cart is empty. No items to remove.")
        return
    
    printCartItems()
    while True:
        try:
            item_id = int(input("Enter the Selected ID of the item to remove: "))
            for item in ItemsInCart:
                if item[0] == item_id:
                    ItemsInCart.remove(item)
                    print(f"Item {item[1]} removed from the cart.")
                    return
            print("Item ID not found. Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid Selected ID.")

# Check if the user wants to remove an item from the cart
def checkForRemove():
    while True:
        choice = input("Do you want to remove items from the cart? Enter 'yes' or 'no': ").strip().lower()
        if choice == 'yes':
            removeItemFromCart()
            return True
        elif choice == 'no':
            return False
        else:
            print("Invalid input! Enter 'yes' or 'no'.")

# Print the list of available shop items
def printShopItems(items):
    itemName = list(items.keys())
    itemPrice = list(items.values())
    selector_id = []
    itemTable = PrettyTable(["S.No", "Item Name", "Price", "Selector ID"])
    for i in range(len(itemName)):
        itemTable.add_row([i + 1, itemName[i], itemPrice[i], i])
        selector_id.append(i)
    print(itemTable)
    return selector_id

# Main function
def main():
     
    print("Welcome you ! In the shopping store")


    print("Available items")
    shopItems = {
        "Apple": 120, "Banana": 60, "Grapes": 80,
        "Orange": 50, "Phone Charger": 150, "Phone Cover": 120,"Sim Card":300,"Ear Phone":400,"Laptop charger":1000,"Laptop Bag":2000
    }
    itemName = list(shopItems.keys())
    itemPrice = list(shopItems.values())
    
    selector_id = printShopItems(shopItems)
    
    addItemInCart(itemName, itemPrice, selector_id)
    
    while True:
        if checkForRemove():
            printCartItems()
        else:
            return 

main()
