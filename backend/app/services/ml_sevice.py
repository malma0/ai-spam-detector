import joblib


model = joblib.load("app/ml/spam_model.pkl")


def predict_spam(text: str):
    prediction = model.predict([text])[0]

    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities)

    return {
        "label": prediction,
        "probability": round(float(confidence), 2)
    }