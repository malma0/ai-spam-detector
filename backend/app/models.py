from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db import Base


class AnalysisHistory(Base):
    __tablename__ = "analysis_history"

    id = Column(Integer, primary_key=True, index=True)
    user_ip = Column(String, index=True)
    text = Column(String)
    label = Column(String)
    probability = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)