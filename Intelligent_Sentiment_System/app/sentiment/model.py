import joblib
import os


MODEL_PATH = "models/sentiment_model.pkl"


def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Sentiment model not found.")

    return joblib.load(MODEL_PATH)


def predict_sentiment(text):
    model = load_model()

    prediction = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]

    confidence = max(probabilities)

    return {
        "sentiment": prediction,
        "confidence": round(float(confidence), 4)
    }