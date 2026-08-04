# Day 1
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {
    "message" : "Week 7 of AI Internship",
    "status" : "Success",
    "data" : "API"
}

# Day 2
@app.get("/user/{id}")
def user(id:int):
    return {
        "user_id" : id,
    }

@app.get("/search")
def search(name: str):
    return {
        "name" : name,
    }

class Post(BaseModel):
    text: str
    
@app.post("/predict")
def predict(post : Post):
    return {
        "text": post.text
    }