from app.pipeline import run_pipeline
from app.database.save_data import save_results


texts = [
    "I absolutely love this product!",
    "This product is amazing and excellent.",
    "Very bad experience with this service.",
    "I hate this product.",
    "The product is okay.",
]


result = run_pipeline(texts)

save_results(result["results"])

print("\n===== INTELLIGENT SENTIMENT SYSTEM =====")

print("\nSentiment Distribution:")
print(result["sentiment_distribution"])

print("\nConfidence Filtered Results:")
print(result["confidence_filtered"])

print("\nKeyword Trends:")
print(result["keyword_trends"])

print("\n===== PIPELINE COMPLETED =====")