import pandas as pd

df = pd.read_csv("phones.csv")
df2 = pd.read_csv("prices.csv")

# head = df.head()
# info = df.info()
# describe = df.describe()
# loc = df.loc[0, "models"]
# brand_filter = df[df["brand"] == "Apple"]
# total_brand = df.groupby("brand")["phone_id"].count()
# sorting_na = df.sort_values("phone_id", ascending=True)
# null_checker = df.isnull().sum()
# df["launch_date"] = df["launch_date"].fillna("June 23, 2023")
# drop_null = df.dropna()
# merge_phones_prices = pd.merge(df, df2, on="phone_id", how="outer")

print()
