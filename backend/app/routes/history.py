from fastapi import APIRouter, Depends, Request, HTTPException
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
        .limit(20)
        .all()
    )

    return history


@router.get("/{history_id}", response_model=HistoryItem)
def get_history_item(history_id: int, db: Session = Depends(get_db)):
    item = (
        db.query(AnalysisHistory)
        .filter(AnalysisHistory.id == history_id)
        .first()
    )

    if item is None:
        raise HTTPException(status_code=404, detail="Запись истории не найдена")

    return item