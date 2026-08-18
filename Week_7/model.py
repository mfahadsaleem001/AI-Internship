from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier

# Day 4
# Topics: CountVectorizer, Decision Tree Training

reviews = [
    "I love this movie",
    "This movie is bad",
    "Amazing product",
    "Worst experience"
]

labels = [
    "Positive",
    "Negative",
    "Positive",
    "Negative"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(reviews)

sentiment_model = DecisionTreeClassifier(
    random_state=42,
    ccp_alpha=0.0
)

sentiment_model.fit(X, labels)

# Day 5
# Topics: Prediction Function, API Integration

def predict_sentiment(text):

    new_vector = vectorizer.transform([text])

    prediction = sentiment_model.predict(new_vector)

    return prediction[0]