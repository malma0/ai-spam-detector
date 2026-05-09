from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import AnalysisHistory
from app.schemas import HistoryItem

router = APIRouter(prefix="/history", tags=["History"])


@router.get("", response_model=list[HistoryItem])
def get_history(request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host

    history = (
        db.query(AnalysisHistory)
        .filter(AnalysisHistory.user_ip == user_ip)
        .order_by(AnalysisHistory.created_at.desc())
        .limit(10)
        .all()
    )

    return history