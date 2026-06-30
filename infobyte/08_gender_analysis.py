import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

df = pd.read_csv("retail_sales_dataset.csv")

gender_count = df["Gender"].value_counts()

plt.figure(figsize=(6, 5))
gender_count.plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/gender_distribution.png")
plt.show()

print(gender_count)