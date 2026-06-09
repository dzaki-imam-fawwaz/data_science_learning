import pandas as pd

data = {
    "Product": ["A", "A", "B", "B", "C"],
    "Sales": [100, 150, 200, 100, 50]
}

df = pd.DataFrame(data)

print("Total:", df["Sales"].sum())
print("Average:", df["Sales"].mean())

print(df.groupby("Product")["Sales"].sum())
