import os
import pandas as pd

from text_cleaner import clean_text
from keyword_extractor import extract_keywords
from sentiment_model import predict_sentiment


# Project folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Load input CSV
input_file = os.path.join(BASE_DIR, "input_posts.csv")

data = pd.read_csv(input_file)


# Store results
results = []


# Process every post
for index, row in data.iterrows():

    post = row["post"]

    # Clean text
    cleaned_text = clean_text(post)

    # Extract keywords
    keywords = extract_keywords(post)

    # Predict sentiment
    sentiment = predict_sentiment(post)


    # Save result
    results.append({
        "id": row["id"],
        "post": post,
        "cleaned_text": cleaned_text,
        "keywords": keywords,
        "sentiment": sentiment
    })


# Convert results into DataFrame
output_data = pd.DataFrame(results)


# Save output CSV
output_file = os.path.join(BASE_DIR, "output_dataset.csv")

output_data.to_csv(
    output_file,
    index=False
)


print("Pipeline completed successfully!")
print("Output saved:", output_file)