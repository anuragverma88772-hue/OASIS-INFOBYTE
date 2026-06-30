import pandas as pd

df = pd.read_csv("retail_sales_dataset.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()

print("Final Insights\n")

print("1. Total Revenue:")
print(df["Total Amount"].sum())

print("\n2. Best Product Category by Revenue:")
print(df.groupby("Product Category")["Total Amount"].sum().idxmax())

print("\n3. Total Quantity Sold by Category:")
print(df.groupby("Product Category")["Quantity"].sum())

print("\n4. Gender Wise Customers:")
print(df["Gender"].value_counts())

print("\n5. Monthly Sales:")
print(df.groupby("Month")["Total Amount"].sum())

print("\nConclusion:")
print("Retail sales analysis helped identify top product categories, customer distribution, revenue trends, and monthly sales performance.")