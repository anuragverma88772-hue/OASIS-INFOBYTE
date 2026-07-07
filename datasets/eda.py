import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import clean_data

def top_categories(df):

    plt.figure(figsize=(12,6))

    df["Category"].value_counts().head(10).plot(
        kind="bar"
    )

    plt.title("Top 10 App Categories")
    plt.tight_layout()
    plt.show()

def rating_distribution(df):

    plt.figure(figsize=(8,5))

    sns.histplot(
        df["Rating"].dropna(),
        bins=20
    )

    plt.title("Rating Distribution")
    plt.show()

def installs_vs_rating(df):

    plt.figure(figsize=(10,6))

    sns.scatterplot(
        data=df,
        x="Rating",
        y="Installs"
    )

    plt.title("Installs vs Rating")
    plt.show()

def price_analysis(df):

    plt.figure(figsize=(8,5))

    sns.boxplot(
        x=df["Price"]
    )

    plt.title("Price Distribution")
    plt.show()

def content_rating_analysis(df):

    plt.figure(figsize=(10,5))

    df["Content Rating"].value_counts().plot(
        kind="bar"
    )

    plt.title("Content Rating Distribution")
    plt.show()

def correlation_heatmap(df):

    cols = [
        "Rating",
        "Reviews",
        "Installs",
        "Price",
        "Size"
    ]

    plt.figure(figsize=(8,6))

    sns.heatmap(
        df[cols].corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")
    plt.show()

def top_installed_apps(df):

    top = df.sort_values(
        by="Installs",
        ascending=False
    ).head(10)

    plt.figure(figsize=(12,6))

    sns.barplot(
        data=top,
        x="Installs",
        y="App"
    )

    plt.title("Top Installed Apps")
    plt.show()

def top_rated_apps(df):

    top = (
        df[df["Rating"] > 4.8]
        .sort_values(
            by="Rating",
            ascending=False
        )
        .head(10)
    )

    plt.figure(figsize=(12,6))

    sns.barplot(
        data=top,
        x="Rating",
        y="App"
    )

    plt.title("Top Rated Apps")
    plt.show()
    

df = clean_data()

top_categories(df)
rating_distribution(df)
installs_vs_rating(df)
price_analysis(df)
content_rating_analysis(df)
correlation_heatmap(df)
top_installed_apps(df)
top_rated_apps(df)