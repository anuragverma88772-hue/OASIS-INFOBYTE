import pandas as pd 

df = pd.read_csv("retail_sales_dataset.csv")    

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()

print(df[["Date", "Month"]].head())