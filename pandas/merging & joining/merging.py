import pandas as pd
df_customer = {
      "Name":["Alice", None, "Charlie", "David", "Eve", "Frank"],
      "Age":[24, None, 22, 32, 29,45],
}
df_order = {

      "OrderID":[101, 102, 103, 104, 105, 106],
      "Amount":[250, 150, 300, 400, 350, 500]
}

df_merged=pd.merge(df_customer, df_order, left_index=True, right_index=True, how='inner')
print(df_merged) 