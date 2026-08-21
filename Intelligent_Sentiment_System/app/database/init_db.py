from app.database.connection import engine, Base
from app.database.models import SentimentData

Base.metadata.create_all(bind=engine)

print("Database initialized successfully!")