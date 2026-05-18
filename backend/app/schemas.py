from pydantic import BaseModel, Field
from datetime import datetime


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=1000
    )


class AnalyzeResponse(BaseModel):
    label: str
    score: float
    model_name: str


class HistoryResponse(BaseModel):
    id: int
    input_text: str
    result_text: str
    score: float
    created_at: datetime

    class Config:
        from_attributes = True