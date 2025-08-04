import pandas as pd
df = pd.read_json("sample_Data.json")
print("display the starting 5 rows of the dataframe")
print(df.head(5))

print("display the last 5 rows of the dataframe")
print(df.tail(5))