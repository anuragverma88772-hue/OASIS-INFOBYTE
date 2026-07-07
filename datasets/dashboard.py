import pandas as pd
import plotly.express as px

df = pd.read_csv("apps.csv")

df["Installs"] = (
    df["Installs"]
    .astype(str)
    .str.replace("+","",regex=False)
    .str.replace(",","",regex=False)
)

df["Installs"] = pd.to_numeric(
    df["Installs"],
    errors="coerce"
)

category_counts = (
    df["Category"]
    .value_counts()
    .head(10)
)

fig = px.bar(
    x=category_counts.index,
    y=category_counts.values,
    title="Top Categories"
)

fig.show(renderer="browser")

fig2 = px.scatter(
    df,
    x="Rating",
    y="Installs",
    color="Category",
    title="Rating vs Installs"
)

fig2.show(renderer="browser")