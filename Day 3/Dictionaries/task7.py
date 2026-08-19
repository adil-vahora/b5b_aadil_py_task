inventory = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15
}

# Add new stock
product = "Laptop"
quantity = 5
inventory[product] = inventory.get(product, 0) + quantity

# Sell an item
product = "Mouse"
quantity = 3

if product in inventory:
    if inventory[product] >= quantity:
        inventory[product] -= quantity
        print("Sale successful")
    else:
        print("Not enough stock")
else:
    print("Product does not exist")

print(inventory)