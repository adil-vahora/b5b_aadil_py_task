def apply_discount(price, percent=10):
    discount = price * percent / 100
    final_price = price - discount
    return final_price


print(apply_discount(500))

print(apply_discount(500, percent=20))