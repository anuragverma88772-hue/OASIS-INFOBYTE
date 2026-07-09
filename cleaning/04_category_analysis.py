import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/dell/Downloads/archive (1)/datasets/cleaned_data.csv")

category_count = df["Category"].value_counts()

plt.figure(figsize=(12,6))
category_count.head(10).plot(kind="bar")
plt.title("Top 10 App Categories")
plt.xlabel("Category")
plt.ylabel("Number of Apps")

plt.tight_layout()
plt.savefig("category_distribution.png")

plt.show()