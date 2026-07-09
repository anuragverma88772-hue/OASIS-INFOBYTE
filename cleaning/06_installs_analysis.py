import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

installs = (
    df.groupby("Category")["Installs"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

installs.plot(kind="bar")

plt.title("Average Installs by Category")
plt.ylabel("Average Installs")

plt.tight_layout()

plt.savefig("installs_by_category.png")

plt.show()