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


# Day 3 - Confidence Filtering
# Topics: Prediction Probability, Confidence Score, Threshold

probabilities = sentiment_model.predict_proba(test_vectors)

confidence_threshold = 0.80
low_confidence_count = 0

correct = 0


# Day 2 - Error Analysis
# Topics: False Positive, False Negative, Error Counting

false_positive = 0
false_negative = 0

for review, actual, predicted, probability in zip(
    test_reviews, actual_labels, predictions, probabilities
):

    print(
        f"Review:{review}\n"
        f"Actual Sentiment: {actual}\n"
        f"Predicted Sentiment: {predicted}"
    )

    confidence = max(probability)
    print(f"Confidence: {confidence * 100:.0f}%")

    if confidence < confidence_threshold:
        print("Low Confidence: Prediction needs review.")
        low_confidence_count = low_confidence_count + 1

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
print(f"Low Confidence Predictions: {low_confidence_count}")
print()

print("Error Analysis:")
print("False Negative Case: 'An absolute masterpiece, would watch again.'")
print("Reason: The model has limited positive training examples and vocabulary.")
print()

accuracy = correct / total * 100
print(f"Accuracy: {accuracy}")
print()

print(sentiment_model.classes_)
print(probabilities)