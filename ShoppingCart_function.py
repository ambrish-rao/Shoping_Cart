# Global database
ItemsInCart = []

# Display the available items in the shop
def displayShopItems(shopItems):
    print("Available items:")
    print("+----+-----------------+--------+-------------+")
    print("| S.No | Item Name       | Price  | Selector ID |")
    print("+----+-----------------+--------+-------------+")
    for i, (name, price) in enumerate(shopItems.items()):
        print(f"| {i+1:<4} | {name:<15} | {price:<6} | {i:<11} |")
    print("+----+-----------------+--------+-------------+\n")

# Add items to the cart
def addItemsToCart(shopItems):
    itemName = list(shopItems.keys())
    itemPrice = list(shopItems.values())
    selector_id = list(range(len(itemName)))

    print("If you don't want to add more items, then Enter '-1'\n")
    while True:
        try:
            selected_id = int(input("Select Item by ID: "))
            if selected_id == -1:
                break
            elif selected_id not in selector_id:
                print("Invalid ID! Try again.")
                continue

            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Please enter a positive number.")
                continue

            item_name = itemName[selected_id]
            price = itemPrice[selected_id]
            found = False

            # Check if item already exists in the cart
            for item in ItemsInCart:
                if item[0] == selected_id:
                    item[3] += quantity
                    item[4] = item[3] * item[2]  # Update total price
                    print(f"Updated {item_name}'s quantity to {item[3]}")
                    found = True
                    break

            # Add new item to cart if not found
            if not found:
                ItemsInCart.append([selected_id, item_name, price, quantity, price * quantity])
        except ValueError:
            print("Invalid input! Please try again.")

# Display all items in the cart
def displayCartItems():
    print("\nCart Items:")
    print("+-------------+-----------------+------------+----------+--------+")
    print("| Selected ID | Item Name       | Price/1qt  | Quantity | Total  |")
    print("+-------------+-----------------+------------+----------+--------+")
    for item in ItemsInCart:
        print(f"| {item[0]:<11} | {item[1]:<15} | {item[2]:<10} | {item[3]:<8} | {item[4]:<6} |")
    print("+-------------+-----------------+------------+----------+--------+")

# Calculate and display the total cost of the cart
def displayTotalCost():
    total_cost = sum(item[4] for item in ItemsInCart)
    print(f"\n+--------------+----------------------------+")
    print(f"| Total Amount | {total_cost} rs.          |")
    print(f"+--------------+----------------------------+")

# Remove items from the cart
def removeItemsFromCart():
    if not ItemsInCart:
        print("The cart is empty. No items to remove.")
        return

    displayCartItems()
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

# Main program logic
def main():
    print("Welcome! In the shopping store\n")

    # Shop items
    shopItems = {
        "Apple": 120, "Banana": 60, "Grapes": 80,
        "Orange": 50, "Phone Charger": 150, "Phone Cover": 120,
        "Sim Card": 300, "Ear Phone": 400, "Laptop charger": 1000, "Laptop Bag": 2000
    }

    # Display shop items
    displayShopItems(shopItems)

    # Add items to cart
    addItemsToCart(shopItems)

    # Display cart items and total cost
    displayCartItems()
    displayTotalCost()

    # Ask user if they want to remove items
    while True:
        remove_choice = input("\nDo you want to remove items from the cart? Enter 'yes' or 'no': ").strip().lower()
        if remove_choice == 'yes':
            removeItemsFromCart()
            displayCartItems()
            displayTotalCost()
        elif remove_choice == 'no':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid input! Enter 'yes' or 'no'.")

# Run the main function
main()
