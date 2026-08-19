
product = ("Laptop", 55000, 10)
print("Original product:", product)

#error
try:
    product[1] = 60000 # trying to update price
except TypeError as e:
    print("Error:", e)

#correct way
name, price, qty = product # unpack
updated_product = (name, 60000, qty) # new tuple with new price

print("Updated product:", updated_product)