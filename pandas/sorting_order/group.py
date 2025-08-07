import pandas as pd
data = {
      "Name":["Alice", None, "Charlie", "David", "Eve", "Frank"],
      "Age":[24, None, 22, 32, 29,45],
      "City":["New York", None, "Chicago", "Houston", "Phoenix", "Philadelphia"],
      "Salary":[70000, None, 60000, 90000, 85000, 95000],
      "Department":["HR", None, "IT", "Marketing", "Sales", "Operations"]
}

df= pd.DataFrame(data)
print(df)

grouped =df.groupby("Age")["Salary"].sum()
print("Grouped by Age and summed Salary:")
print(grouped)
