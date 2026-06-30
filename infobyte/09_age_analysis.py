import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

df = pd.read_csv("retail_sales_dataset.csv")

plt.figure(figsize=(8, 5))
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("images/age_distribution.png")
plt.show()

print(df["Age"].describe())