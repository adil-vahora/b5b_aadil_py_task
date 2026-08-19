price = [100, 250, 75, 500, 150, 300, 450, 200, 125, 350, 600, 175]

ave = sum(price) / len(price)

ave2 = [p for p in price if p > ave]

print("Average price:", ave)
print("Prices above average:", ave2)