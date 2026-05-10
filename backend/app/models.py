from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from app.db import Base


class AnalysisHistory(Base):
    __tablename__ = "requests_history"

    id = Column(Integer, primary_key=True, index=True)
    user_ip = Column(String, index=True)
    text = Column(Text)
    label = Column(String)
    probability = Column(Float)
    model_name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)