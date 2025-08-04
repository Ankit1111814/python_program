import pandas as pd

data ={
  "Name":["Ankit", "Ankita", "Amit", "Aman", "Anjali", "Anshul",  "Ankush", "Ananya", "Aniket", "Anushka",  "Anirudh", "Anjali"],
  "Age":[23, 22, 24, 25, 21, 26, 27, 28, 29, 30, 31, 32],
  "City":["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow", "Kanpur", "Nagpur"]
}

df =  pd.DataFrame(data)
print(df)
print("DataFrame Info:")
print(df.info())

print(df.describe())


