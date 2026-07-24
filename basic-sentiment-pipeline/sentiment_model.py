from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from text_cleaner import clean_text
import joblib

reviews = [
    "I love AI",
    "Python is amazing",
    "This project is excellent",
    "I hate bugs",
    "This is very bad",
    "The code is terrible"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(reviews)

model = DecisionTreeClassifier()

model.fit(X, labels)

def predict_sentiment(text):
    clean_words = clean_text(text)
    clean_text_string = " ".join(clean_words)

    text_vector = vectorizer.transform([clean_text_string])

    prediction = model.predict(text_vector)

    return prediction[0]

joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")