import pandas as pd

df = pd.read_csv("apps.csv")

print("\nFirst 5 Rows")
print(df.head())

print("\nColumns")
print(df.columns)

print("\nInfo")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nStatistical Summary")
print(df.describe())