import pandas as pd
data = {
     "Name":["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
      "Age":[24, 27, 22, 32, 29,45],
      "City":["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
      "Salary":[70000, 80000, 60000, 90000, 85000, 95000],
      "Department":["HR", "Finance", "IT", "Marketing", "Sales", "Operations"]
}

df  = pd.DataFrame(data)
print(df)

df["Bonus"] = df['Salary'] * 0.1
print(df)

#adding a new column

df.insert(0,"employee_id" ,[10,20,30,40,50,60])
print(df)
