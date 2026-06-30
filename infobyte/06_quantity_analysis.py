import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("output", exist_ok=True)

df = pd.read_csv("retail_sales_dataset.csv")

quantity = df.groupby("Product Category")["Quantity"].sum()

plt.figure(figsize=(8, 5))
quantity.plot(kind='bar')
plt.title("Quantity Sold by Product Category")
plt.xlabel("Product Category")
plt.ylabel("TotalQuantity")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("output/quantity_by_category.png")
plt.show()

print(quantity)