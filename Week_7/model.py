from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier

# Training Data
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

# Convert text into numerical features
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(reviews)

# Train Decision Tree Model
sentiment_model = DecisionTreeClassifier(
    random_state=42,
    ccp_alpha=0.0
)

sentiment_model.fit(X, labels)

# Prediction Function
def predict_sentiment(text):

    new_vector = vectorizer.transform([text])

    prediction = sentiment_model.predict(new_vector)

    return prediction[0]