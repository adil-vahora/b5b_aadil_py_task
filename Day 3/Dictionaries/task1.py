products = {
    "Laptop": 800,
    "Mouse": 50,
    "Keyboard": 120,
    "Monitor": 250,
    "Headphones": 150
}

expensive_products = {
    product: price
    for product, price in products.items()
    if price > 100
}

print(expensive_products)