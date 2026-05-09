from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import Base, engine
from app.routes import health, analyze, history


Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Spam Detector")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(analyze.router)
app.include_router(history.router)


@app.get("/")
def root():
    return {
        "message": "AI Spam Detector API"
    }