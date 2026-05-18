from fastapi import APIRouter, Depends
from transformers import pipeline

from app.schemas import TextRequest
from app.security import verify_api_key

router = APIRouter()

classifier = pipeline(
    "text-classification",
    model="mrm8488/bert-tiny-finetuned-sms-spam-detection"
)


@router.post(
    "/analyze",
    dependencies=[Depends(verify_api_key)]
)
async def analyze_text(data: TextRequest):

    result = classifier(data.text)[0]

    return {
        "label": result["label"],
        "score": round(result["score"], 4),
        "model_name": "mrm8488/bert-tiny-finetuned-sms-spam-detection"
    }