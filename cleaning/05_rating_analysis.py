import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

plt.figure(figsize=(8,5))

plt.hist(df["Rating"].dropna(), bins=20)

plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")

plt.savefig("rating_distribution.png")

plt.show()