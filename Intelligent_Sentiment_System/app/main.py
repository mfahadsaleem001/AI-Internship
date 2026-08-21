from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Intelligent Sentiment System",
    description="AI-powered sentiment analysis and analytics system",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Intelligent Sentiment System API is running"
    }