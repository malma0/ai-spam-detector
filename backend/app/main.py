from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI Spam Detector API is running"}