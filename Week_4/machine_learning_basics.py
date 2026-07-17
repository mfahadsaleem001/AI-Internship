# Imports
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer


print("=" * 50)
print("Week 4 - Machine Learning Basics")
print("=" * 50)


# PART 1 - Basic Decision Tree Example

print("\n1. Basic Decision Tree Example\n")

X = [[8], [6], [4], [1], [5]]
y = ["Pass", "Pass", "Fail", "Fail", "Pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=15
)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("X Test :", X_test)
print("Actual :", y_test)
print("Prediction :", prediction)

accuracy = accuracy_score(y_test, prediction)

print("Accuracy :", accuracy)


# PART 2 - NLP (Sentiment Analysis)

print("\n" + "=" * 50)
print("2. Sentiment Analysis")
print("=" * 50)

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

sentiment_model = DecisionTreeClassifier()

sentiment_model.fit(X, labels)

# Predict New Review

new_review = ["This is bad"]

new_vector = vectorizer.transform(new_review)

prediction = sentiment_model.predict(new_vector)

print("\nNew Review :", new_review[0])
print("Prediction :", prediction[0])