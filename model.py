from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

sia = SentimentIntensityAnalyzer()

def predict_sentiment(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^\w\s]", "", text)

    score = sia.polarity_scores(text)['compound']

    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

