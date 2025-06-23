#  Challenge - Create an inventory system tracking items and quantities with a dictionary
# way 1 - Basic
inventory = {}

# Add item
inventory['Apple'] = 12
inventory['Banana'] = 20

# Update item
inventory['Banana'] += 8
inventory['Mango'] = 8
inventory['Cherry'] = 1

# Remove an item
del inventory['Cherry']

# Display current inventory
for item, qty in inventory.items():
  print(f"{item} : {qty}")


# way 2 - Inventory system using key list/dict/set methods
# Initialize inventory (dictionary)
inventory = {}

# Add items using update()
inventory.update({"apple": 10})
inventory.update({"banana": 5})

# Add new item using a tuple
item = ("orange", 8)
inventory.update({item[0]: item[1]})

# Prevent duplicate using set
items_set = set(inventory.keys())
if "apple" not in items_set:
    inventory.update({"apple": 3})
else:
    print("apple already exists.")

# Update item quantity
inventory.update({"banana": 7})

# Remove item using pop()
inventory.pop("banana")

# Show inventory
print("Inventory:")
for item, qty in inventory.items():
    print(f"{item}: {qty}")


# way 3 - Advancec inventory system with user interaction
inventory = {}

# Display Inventory
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    print("-" * 30) 

# Add Item
def add_item():
    item = input("Enter item name to add: ").lower()
    quantity = int(input("Enter quantity: "))
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"{quantity} {item}(s) added.")

# Update Item
def update_item():
    item = input("Enter item name to update: ").lower()
    if item in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[item] = quantity
        print(f"{item} updated to {quantity}.")
    else:
        print(f"{item} not found in inventory.")

# Remove Item
def remove_item():
    item = input("Enter item name to remove: ").lower()
    if item in inventory:
        del inventory[item]
        print(f"{item} removed from inventory.")
    else:
        print(f"{item} not found in inventory.")

# Main loop
while True:
    print("\n📦 Inventory Menu:")
    print("1. Display Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        display_inventory()
    elif choice == "2":
        add_item()
    elif choice == "3":
        update_item()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        print("Exiting inventory system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
