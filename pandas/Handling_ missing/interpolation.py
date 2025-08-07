import pandas as pd
data = {
  "value":[1, 2, None, 4, None, 6],
  "category":["A", "B", "A", "B", None, "A"],
  }

df =pd.DataFrame(data)
print(df)
# fill the missing values using interpolation
df["value"] = df["value"].interpolate(method='linear')
df["category"] = df["category"].interpolate(method='pad')
print(df)
