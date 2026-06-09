import pandas as pd

"""
MATERIAL: Creating a DataFrame
"""

data = {
    "Name": ["Andi", "Budi", "Siti"],
    "Age": [25, 30, 22],
    "City": ["Jakarta", "Bandung", "Surabaya"]
}

df = pd.DataFrame(data)

print(df)
