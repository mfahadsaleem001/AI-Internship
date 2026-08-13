# WEEK 4 - MACHINE LEARNING BASICS

# DAY 1 - MACHINE LEARNING & DECISION TREE INTRODUCTION
# Topics: Machine Learning Basics, Decision Tree Classifier,Features and Labels

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

# DAY 2 - TRAINING AND TESTING THE MACHINE LEARNING MODEL
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=15
)

# FIX 1: Add random_state and ccp_alpha to remove SonarQube warning
model = DecisionTreeClassifier(random_state=15, ccp_alpha=0.0)

model.fit(X_train, y_train)

# DAY 3 - MODEL PREDICTION AND EVALUATION
prediction = model.predict(X_test)

print("X Test :", X_test)
print("Actual :", y_test)
print("Prediction :", prediction)

accuracy = accuracy_score(y_test, prediction)
print("Accuracy :", accuracy)

# DAY 4 - NLP AND TEXT FEATURE EXTRACTION
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
X_text = vectorizer.fit_transform(reviews)

# FIX 2: Split text data too for proper evaluation
X_train_text, X_test_text, y_train_text, y_test_text = train_test_split(
    X_text, labels, test_size=0.25, random_state=15
)

# DAY 5 - SENTIMENT MODEL TRAINING AND FINAL PREDICTION
sentiment_model = DecisionTreeClassifier(random_state=15, ccp_alpha=0.0)
sentiment_model.fit(X_train_text, y_train_text)

# Check accuracy on test data
text_pred = sentiment_model.predict(X_test_text)
print("Text Model Accuracy:", accuracy_score(y_test_text, text_pred))

# Predict New Review
new_review = ["This is bad"]
new_vector = vectorizer.transform(new_review)
prediction = sentiment_model.predict(new_vector)

print("\nNew Review :", new_review[0])
print("Prediction :", prediction[0])