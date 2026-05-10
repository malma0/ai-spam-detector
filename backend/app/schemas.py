from pydantic import BaseModel, Field
from datetime import datetime


class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1)


class AnalyzeResponse(BaseModel):
    label: str
    probability: float
    message: str
    model_name: str


class HistoryItem(BaseModel):
    id: int
    text: str
    label: str
    probability: float
    model_name: str
    created_at: datetime

    class Config:
        from_attributes = True