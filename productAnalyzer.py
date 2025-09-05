import pandas as pd
from textblob import TextBlob
import streamlit as st

# Load sample data (CSV with 'review' column)
data = {
    "review": [
        "This product is amazing, loved it!",
        "Worst purchase ever, totally disappointed.",
        "Good value for money.",
        "Battery drains too fast.",
        "Excellent quality, very satisfied."
    ]
}
df = pd.DataFrame(data)

# Sentiment Analysis
def analyze_sentiment(review):
    analysis = TextBlob(review)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["review"].apply(analyze_sentiment)

# Streamlit UI
st.title("📊 Flipkart Product Review Analyzer")
st.write("This app analyzes product reviews and classifies them as Positive, Negative, or Neutral.")

st.write("### Sample Reviews with Sentiment")
st.table(df)

sentiment_counts = df["Sentiment"].value_counts()
st.bar_chart(sentiment_counts)
