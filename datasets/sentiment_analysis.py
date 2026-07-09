import pandas as pd
import matplotlib.pyplot as plt

def analyze_sentiment():

    reviews = pd.read_csv("user_reviews.csv")

    sentiment = reviews["Sentiment"].value_counts()

    print("\nSentiment Summary\n")
    print(sentiment)

    plt.figure(figsize=(7,7))

    sentiment.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.ylabel("")
    plt.title("User Review Sentiment")
    plt.show()
    if __name__ == "__main__":
        analyze_sentiment()