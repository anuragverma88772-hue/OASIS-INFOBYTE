import pandas as pd
import numpy as np

df = pd.read_csv("apps.csv")

df = df.drop_duplicates()

df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")

df["Installs"] = (
    df["Installs"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("+", "", regex=False)
)

df["Installs"] = pd.to_numeric(df["Installs"], errors="coerce")

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

df["Size"] = df["Size"].replace("Varies with device", np.nan)

df["Rating"].fillna(df["Rating"].median(), inplace=True)

df.to_csv("cleaned_data.csv", index=False)

print("Data Cleaning Completed")