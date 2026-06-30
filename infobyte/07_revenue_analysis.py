import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

df = pd.read_csv("retail_sales_dataset.csv")

revenue = df.groupby("Product Category")["Total Amount"].sum()

plt.figure(figsize=(8, 5))
revenue.plot(kind="bar")
plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("images/revenue_by_category.png")
plt.show()

print(revenue)