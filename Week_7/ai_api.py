# Day 1
# Topics: FastAPI, GET API

from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_sentiment

app = FastAPI()

# Root Endpoint
@app.get("/")
def root():
    return {
        "message": "Week 7 of AI Internship",
        "status": "Success",
        "data": "API"
    }

# Day 2
# Topics: Path Parameter, Query Parameter, Pydantic, POST API

# Path Parameter
@app.get("/user/{id}")
def user(id: int):
    return {
        "user_id": id,
    }

# Query Parameter
@app.get("/search")
def search(name: str):
    return {
        "name": name,
    }

# Request Body Model
class Post(BaseModel):
    text: str

# POST Endpoint
@app.post("/predict")
def predict(post: Post):

    prediction = predict_sentiment(post.text)

    return {
        "text": post.text,
        "prediction": prediction
    }