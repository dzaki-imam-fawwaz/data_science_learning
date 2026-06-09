import pandas as pd

data = {"Age": [25, 30, 22]}

df = pd.DataFrame(data)

print(df["Age"].mean())
print(df["Age"].max())
print(df["Age"].min())
