# Day 1
# Topics: FastAPI, GET API

from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_sentiment

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Week 7 of AI Internship",
        "status": "Success",
        "data": "API"
    }


# Day 2
# Topics: Path Parameter, Query Parameter, Pydantic, POST API

@app.get("/user/{id}")
def user(id: int):
    return {
        "user_id": id,
    }

@app.get("/search")
def search(name: str):
    return {
        "name": name,
    }

class Post(BaseModel):
    text: str


# Day 3
# Topics: AI Model Integration

@app.post("/predict")
def predict(post: Post):

    prediction = predict_sentiment(post.text)

    return {
        "text": post.text,
        "prediction": prediction
    }