# 11.4.py

import pandas as pd
import re


df = pd.read_csv("countries.csv")

# head(n) displays first n rows
print(df.head(10))

# rename the column names
# inplace means that the cols are renamed in-place in the
# original DataFrame rather than a new DataFrame being returned.
df.rename(
    columns={
        "#": "Order",
        "Country/territory": "Country",
        "Date of first store": "Date",
        "First outlet location": "Location",
        "Max. no. ofoperatingoutlets": "Outlets",
    },
    inplace=True,
)

date_re = re.compile("[A-Z][a-z]+ [0-9]{1,2}, [0-9]{4}")
df["Date"] = df["Date"].apply(lambda d: date_re.findall(d)[0])
df["Date"] = pd.to_datetime(df["Date"])

print(df.head(10))
