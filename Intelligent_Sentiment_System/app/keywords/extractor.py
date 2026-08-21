from collections import Counter
import re


def extract_keywords(texts, top_n=10):
    words = []

    stopwords = {
        "the", "is", "a", "an", "this", "that",
        "and", "or", "to", "of", "in", "for",
        "with", "on", "it", "was", "very"
    }

    for text in texts:
        cleaned = re.sub(r"[^a-zA-Z\s]", "", text.lower())
        words.extend(cleaned.split())

    words = [
        word for word in words
        if word not in stopwords and len(word) > 2
    ]

    return Counter(words).most_common(top_n)