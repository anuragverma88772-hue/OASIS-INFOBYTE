import pandas as pd

df = pd.read_csv("retail_sales_dataset.csv")

print("Duplicates:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)