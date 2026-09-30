import os

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from .schemas import TitanicPredictionInput, PredictionResponse


MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "06_champion_model.joblib"
)

try:
    model = joblib.load(MODEL_PATH)
except Exception as exc:
    raise RuntimeError(
        f"Could not load model from {MODEL_PATH}: {exc}"
    )


app = FastAPI(
    title="Titanic Survival Prediction API",
    description="REST API for the trained Titanic survival classification model.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Titanic Survival Prediction API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(data: TitanicPredictionInput):

    input_data = pd.DataFrame([{
        "pclass": data.pclass,
        "age": data.age,
        "sibsp": data.sibsp,
        "parch": data.parch,
        "fare": data.fare,
        "sex": data.sex,
        "embarked": data.embarked,
        "class": data.class_name,
        "who": data.who,
        "adult_male": data.adult_male,
        "deck": data.deck,
        "embark_town": data.embark_town,
        "alive": data.alive,
        "alone": data.alone
    }])

    try:
        prediction = int(model.predict(input_data)[0])
        probabilities = model.predict_proba(input_data)[0]

        return PredictionResponse(
            prediction=prediction,
            prediction_label=(
                "Survived" if prediction == 1 else "Did not survive"
            ),
            probability_negative=float(probabilities[0]),
            probability_positive=float(probabilities[1])
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {exc}"
        )