from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib


texts = [
    "I love this product",
    "This product is amazing",
    "Excellent service",
    "I am very happy",
    "Great experience",
    "I hate this product",
    "This is terrible",
    "Very bad service",
    "Worst experience",
    "I am disappointed",
    "This product is okay",
    "The service is average",
    "It is fine",
    "Nothing special",
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Neutral",
    "Neutral",
    "Neutral",
    "Neutral",
]


model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])


model.fit(texts, labels)

joblib.dump(model, "models/sentiment_model.pkl")

print("Sentiment model trained successfully!")
print("Model saved to models/sentiment_model.pkl")