import pandas as pd

df = pd.read_csv("products.csv")

print("First 2 rows:")
print(df.head(2))

print("Shape:")
print(df.shape)