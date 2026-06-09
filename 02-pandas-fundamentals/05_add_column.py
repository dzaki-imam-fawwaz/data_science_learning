import pandas as pd

data = {
    "Name": ["Andi", "Budi", "Siti"],
    "Age": [25, 30, 22]
}

df = pd.DataFrame(data)

df["Age_Next_Year"] = df["Age"] + 1

print(df)
