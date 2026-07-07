from data_cleaning import clean_data
from eda import *
from sentiment_analysis import analyze_sentiment

df = clean_data()

print("\nDataset Shape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nAverage Rating")
print(df["Rating"].mean())

print("\nAverage Price")
print(df["Price"].mean())

print("\nTop Categories")
print(df["Category"].value_counts().head())

top_categories(df)
rating_distribution(df)
installs_vs_rating(df)
price_analysis(df)
content_rating_analysis(df)
correlation_heatmap(df)
top_installed_apps(df)
top_rated_apps(df)

analyze_sentiment()