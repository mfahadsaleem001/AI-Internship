import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Week_7.model import vectorizer, sentiment_model

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

for review, actual, predicted in zip(test_reviews, actual_labels, predictions):
    print(f"Review:{review}\n Actual Sentiment: {actual}\n Predicted Sentiment: {predicted}")
    result = actual == predicted
    if result == True:
        correct = correct + 1
    print("Result:", result)
    print()

total = len(test_reviews)
accuracy = correct / total * 100
print(f"Accuracy: {accuracy}")