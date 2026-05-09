from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import AnalysisHistory
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.services.ml_service import predict_spam


router = APIRouter(prefix="/analyze", tags=["Analyze"])


@router.post("", response_model=AnalyzeResponse)
def analyze_text(
    data: AnalyzeRequest,
    request: Request,
    db: Session = Depends(get_db)
):
    user_ip = request.client.host

    result = predict_spam(data.text)

    label = result["label"]
    probability = result["probability"]

    if label == "SPAM":
        message = "Сообщение похоже на спам"
    else:
        message = "Сообщение похоже на обычное сообщение"

    history_item = AnalysisHistory(
        user_ip=user_ip,
        text=data.text,
        label=label,
        probability=probability
    )

    db.add(history_item)
    db.commit()

    return {
        "label": label,
        "probability": probability,
        "message": message
    }