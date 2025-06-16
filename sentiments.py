from textblob import TextBlob

def sentiment_score(text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity


        if polarity >= 0.05:
            sentiment_label = "It is a Positive text"
        elif polarity <= -0.05:
            sentiment_label = "It is a Negative text"
        else:
            sentiment_label = "It is a Neutral text"

        return {
            "polarity" :round(polarity, 2),
            "subjectivity": round(subjectivity, 2),
            "label": sentiment_label
        }
'''

# implement nltk version