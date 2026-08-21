from app.database.connection import SessionLocal
from app.database.models import SentimentData


def save_results(results):
    db = SessionLocal()

    try:
        for result in results:
            record = SentimentData(
                text=result["text"],
                cleaned_text=result["text"],
                sentiment=result["sentiment"],
                confidence=result["confidence"],
            )

            db.add(record)

        db.commit()
        print("Results saved to database!")

    finally:
        db.close()