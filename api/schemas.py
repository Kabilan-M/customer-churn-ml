from pydantic import BaseModel, Field


class TitanicPredictionInput(BaseModel):
    pclass: int = Field(..., ge=1, le=3)
    age: float = Field(..., ge=0)
    sibsp: int = Field(..., ge=0)
    parch: int = Field(..., ge=0)
    fare: float = Field(..., ge=0)

    sex: str
    embarked: str
    class_name: str
    who: str
    adult_male: bool
    deck: str
    embark_town: str
    alive: str
    alone: bool


class PredictionResponse(BaseModel):
    prediction: int
    prediction_label: str
    probability_negative: float
    probability_positive: float