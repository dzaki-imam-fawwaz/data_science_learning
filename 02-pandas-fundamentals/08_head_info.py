import pandas as pd

data = {
    "Name": ["Andi", "Budi", "Siti"],
    "Age": [25, 30, 22]
}

df = pd.DataFrame(data)

print(df.head())
print(df.info())
