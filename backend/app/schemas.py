from pydantic import BaseModel
from datetime import datetime


class AnalyzeRequest(BaseModel):
    text: str


class AnalyzeResponse(BaseModel):
    label: str
    probability: float
    message: str


class HistoryItem(BaseModel):
    id: int
    text: str
    label: str
    probability: float
    created_at: datetime

    class Config:
        from_attributes = True