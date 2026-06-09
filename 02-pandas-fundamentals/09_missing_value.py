import pandas as pd
import numpy as np

data = {
    "Name": ["Andi", "Budi", "Siti"],
    "Age": [25, np.nan, 22]
}

df = pd.DataFrame(data)

print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)
