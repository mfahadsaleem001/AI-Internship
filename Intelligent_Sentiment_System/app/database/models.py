from sqlalchemy import Column, Integer, Text, Float, DateTime
from datetime import datetime

from app.database.connection import Base


class SentimentData(Base):
    __tablename__ = "sentiment_data"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    cleaned_text = Column(Text)
    sentiment = Column(Text)
    confidence = Column(Float)
    keywords = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)