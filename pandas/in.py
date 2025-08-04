# import pandas as pd
# df = pd.read_json("sample_Data.json")
# print("display the info for the json file")
# print(df.info())


import pandas as pd

data ={
  "Name":["Ankit", "Ankita", "Amit", "Aman"],
  "Age":[23, 22, 24, 25],
  "City":["Delhi", "Mumbai", "Bangalore", "Chennai"]
  }

df = pd.DataFrame(data)
print(df.info())

#df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)

