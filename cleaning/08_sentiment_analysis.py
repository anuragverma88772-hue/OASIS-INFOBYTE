import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv("user_reviews.csv")

sentiment = reviews["Sentiment"].value_counts()

plt.figure(figsize=(6,4))

sentiment.plot(kind="bar")

plt.title("User Review Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("sentiment_analysis.png")

plt.show()