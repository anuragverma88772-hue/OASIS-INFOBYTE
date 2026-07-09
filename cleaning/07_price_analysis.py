import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

paid_apps = df[df["Price"] > 0]

plt.figure(figsize=(8,5))

plt.hist(paid_apps["Price"], bins=20)

plt.title("Paid Apps Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")

plt.savefig("price_analysis.png")

plt.show()