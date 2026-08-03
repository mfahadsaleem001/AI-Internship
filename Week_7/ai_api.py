from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
    "message" : "Week 7 of AI Internship",
    "status" : "Success",
    "data" : "API"
}