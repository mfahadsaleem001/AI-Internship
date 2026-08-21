from fastapi import APIRouter
from pydantic import BaseModel

from app.sentiment.model import predict_sentiment
from app.pipeline import run_pipeline


router = APIRouter()


class TextRequest(BaseModel):
    text: str


class PipelineRequest(BaseModel):
    texts: list[str]


@router.post("/predict")
def predict(request: TextRequest):
    return predict_sentiment(request.text)


@router.post("/pipeline")
def pipeline(request: PipelineRequest):
    return run_pipeline(request.texts)