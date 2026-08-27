import pandas as pd

df = pd.read_csv("products.csv")

result = df[df["Price"] > 5000]

print(result)