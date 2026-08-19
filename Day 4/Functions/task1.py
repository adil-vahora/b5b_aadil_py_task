def build_invoice(customer_name, *prices, **details):
    total = sum(prices)

    print("Customer:", customer_name)
    print("Total:", total)

    for key, value in details.items():
        print(key, ":", value)


build_invoice(
    "Adil",
    200, 150, 300,
    discount=50,
    tax=20
)