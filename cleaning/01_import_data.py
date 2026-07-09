import pandas as pd

apps_df = pd.read_csv("apps.csv")

print("Dataset Loaded Successfully")
print(apps_df.head())
print("\nShape:", apps_df.shape)