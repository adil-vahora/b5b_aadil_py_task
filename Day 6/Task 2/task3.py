import pandas as pd

df = pd.read_csv("marks.csv")

average = df["Maths"].mean()

print("Average Maths marks:", average)

topper_index = df["Maths"].idxmax()

print("Topper:")
print(df.loc[topper_index, "Student"])
print(df.loc[topper_index, "Maths"])