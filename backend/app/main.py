from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import analyze
from app.routes import history
from app.routes import health
from app.routes import summarize

app = FastAPI(
    title="AI Spam Detector API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze.router)
app.include_router(history.router)
app.include_router(health.router)
app.include_router(summarize.router)


@app.get("/")
async def root():
    return {
        "message": "AI Spam Detector API is running"
    }