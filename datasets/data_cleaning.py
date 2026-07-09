import pandas as pd
import numpy as np

def clean_data():

    df = pd.read_csv("apps.csv")

    df.drop_duplicates(inplace=True)

    df["Installs"] = (
        df["Installs"]
        .astype(str)
        .str.replace("+","",regex=False)
        .str.replace(",","",regex=False)
    )

    df["Installs"] = pd.to_numeric(df["Installs"], errors="coerce")

    df["Price"] = (
        df["Price"]
        .astype(str)
        .str.replace("$","",regex=False)
    )

    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")

    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

    df["Size"] = (
        df["Size"]
        .astype(str)
        .str.replace("M","",regex=False)
        .str.replace("k","",regex=False)
    )

    df["Size"] = pd.to_numeric(df["Size"], errors="coerce")

    return df
if __name__ == "__main__":
    df = clean_data()
    df.to_csv("cleaned_apps.csv", index=False)
    print("Data cleaned successfully!")