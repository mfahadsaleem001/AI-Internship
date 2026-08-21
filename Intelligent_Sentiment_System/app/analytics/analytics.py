from collections import Counter


def sentiment_distribution(sentiments):
    total = len(sentiments)

    if total == 0:
        return {}

    counts = Counter(sentiments)

    return {
        sentiment: round((count / total) * 100, 2)
        for sentiment, count in counts.items()
    }


def confidence_filter(results, threshold=0.70):
    return [
        result
        for result in results
        if result["confidence"] >= threshold
    ]


def keyword_trends(keywords):
    return sorted(
        keywords,
        key=lambda item: item[1],
        reverse=True
    )