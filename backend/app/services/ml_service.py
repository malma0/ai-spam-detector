import os
import logging
from dotenv import load_dotenv
from transformers import pipeline


load_dotenv()

logger = logging.getLogger(__name__)

MODEL_NAME = os.getenv("MODEL_NAME", "mshenoda/roberta-spam")

try:
    classifier = pipeline(
        "text-classification",
        model=MODEL_NAME
    )
    logger.info(f"Модель загружена: {MODEL_NAME}")
except Exception as error:
    logger.error(f"Ошибка загрузки модели: {error}")
    classifier = None


def predict_spam(text: str):
    if classifier is None:
        raise RuntimeError("Модель не загружена")

    result = classifier(text)[0]

    label = result["label"].upper()
    score = round(float(result["score"]), 2)

    if label in ["LABEL_1", "SPAM"]:
        final_label = "SPAM"
    else:
        final_label = "NOT_SPAM"

    return {
        "label": final_label,
        "probability": score,
        "model_name": MODEL_NAME
    }