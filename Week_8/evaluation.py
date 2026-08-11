import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Week_7.model import vectorizer, sentiment_model


# Day 1 - Evaluation Basics
# Topics: Test Data, Actual vs Predicted, Accuracy

test_reviews = [
    "I love this movie!",
    "This was a terrible experience",
    "The plot was predictable and boring.",
    "An absolute masterpiece, would watch again.",
]

actual_labels = ["Positive", "Negative", "Negative", "Positive"]

test_vectors = vectorizer.transform(test_reviews)

predictions = sentiment_model.predict(test_vectors)

correct = 0


# Day 2 - Error Analysis
# Topics: False Positive, False Negative, Error Counting

false_positive = 0
false_negative = 0

for review, actual, predicted in zip(test_reviews, actual_labels, predictions):
    print(f"Review:{review}\nActual Sentiment: {actual}\nPredicted Sentiment: {predicted}")

    result = actual == predicted

    if actual == "Negative" and predicted == "Positive":
        print("False Positive: The model predicted a positive sentiment for a negative review.")
        false_positive = false_positive + 1

    if actual == "Positive" and predicted == "Negative":
        print("False Negative: The model predicted a negative sentiment for a positive review.")
        false_negative = false_negative + 1

    if result:
        correct = correct + 1

    print("Result:", result)
    print()


total = len(test_reviews)

print(f"False Positives: {false_positive}")
print(f"False Negatives: {false_negative}")

print("Error Analysis:")
print("False Negative Case: 'An absolute masterpiece, would watch again.'")
print("Reason: The model has limited positive training examples and vocabulary.")

accuracy = correct / total * 100
print(f"Accuracy: {accuracy}")