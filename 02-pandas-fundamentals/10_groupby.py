import pandas as pd

data = {
    "City": ["Jakarta", "Jakarta", "Bandung"],
    "Sales": [100, 150, 200]
}

df = pd.DataFrame(data)

print(df.groupby("City")["Sales"].sum())
