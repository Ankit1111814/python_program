import pandas as pd
data = {
      "Name":["Alice", None, "Charlie", "David", "Eve", "Frank"],
      "Age":[24, None, 22, 32, 29,45],
      "City":["New York", None, "Chicago", "Houston", "Phoenix", "Philadelphia"],
      "Salary":[70000, None, 60000, 90000, 85000, 95000],
      "Department":["HR", None, "IT", "Marketing", "Sales", "Operations"]
}

df = pd.DataFrame(data)

df.sort_values(by=["Age","Salary"],ascending=[True,False],inplace=True)
# df.sort_values(by="Age", ascending=True, inplace=True)
print("sorting the by age")
print(df)

avg_salary = df["Salary"].mean()
print ("Average Salary:", avg_salary)