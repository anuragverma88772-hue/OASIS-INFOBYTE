import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

df = pd.read_csv("retail_sales_dataset.csv")
df.columns = df.columns.str.strip()

# exit()

category_count = df["Product Category"].value_counts() 

plt.figure(figsize=(8, 5))
category_count.plot(kind="bar")
plt.title("Product Category Distribution")
plt.xlabel("Product Category")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("plots/product_category_distribution.png")
plt.show()

print(category_count)
