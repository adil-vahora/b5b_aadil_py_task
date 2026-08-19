def process_order(order):
    try:
        item = order["item"]
        price = order["price"]

    except KeyError:
        print("Error: Order must contain item and price.")

    else:
        print("Item:", item)
        print("Price:", price)

    finally:
        print("Processing complete")


order1 = {
    "item": "Laptop",
    "price": 50000
}

order2 = {
    "item": "Mouse"
}

process_order(order1)
process_order(order2)