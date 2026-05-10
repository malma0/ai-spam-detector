from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db import get_db
from app.services.ml_service import classifier, MODEL_NAME


router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
def health_check(db: Session = Depends(get_db)):
    database_status = "connected"

    try:
        db.execute(text("SELECT 1"))
    except Exception:
        database_status = "error"

    model_loaded = classifier is not None

    return {
        "status": "ok" if database_status == "connected" and model_loaded else "error",
        "api": "working",
        "database": database_status,
        "model_loaded": model_loaded,
        "model_name": MODEL_NAME
    }