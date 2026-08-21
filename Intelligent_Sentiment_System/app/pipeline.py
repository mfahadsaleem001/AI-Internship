from app.preprocessing.cleaner import clean_data
from app.sentiment.model import predict_sentiment
from app.keywords.extractor import extract_keywords
from app.analytics.analytics import (
    sentiment_distribution,
    confidence_filter,
)


def run_pipeline(texts):

    cleaned_texts = clean_data(texts)

    results = []

    for text in cleaned_texts:
        prediction = predict_sentiment(text)

        results.append({
            "text": text,
            "sentiment": prediction["sentiment"],
            "confidence": prediction["confidence"],
        })

    sentiments = [
        result["sentiment"]
        for result in results
    ]

    distribution = sentiment_distribution(sentiments)

    high_confidence = confidence_filter(results)

    keywords = extract_keywords(cleaned_texts)

    return {
        "results": results,
        "sentiment_distribution": distribution,
        "confidence_filtered": high_confidence,
        "keyword_trends": keywords,
    }