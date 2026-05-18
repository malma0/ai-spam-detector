from fastapi import APIRouter, Depends
from transformers import pipeline

from app.schemas import TextRequest
from app.security import verify_api_key

router = APIRouter()

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


@router.post(
    "/summarize",
    dependencies=[Depends(verify_api_key)]
)
async def summarize_text(data: TextRequest):

    result = summarizer(
        data.text,
        max_length=50,
        min_length=10,
        do_sample=False
    )

    return {
        "summary": result[0]["summary_text"]
    }