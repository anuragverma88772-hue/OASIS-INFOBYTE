import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

df = pd.read_csv("retail_sales_dataset.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()

monthly_sales = df.groupby("Month")["Total Amount"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("images/monthly_sales_trend.png")
plt.show()

print(monthly_sales)