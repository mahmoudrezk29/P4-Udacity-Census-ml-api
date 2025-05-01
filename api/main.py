from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from model.model import inference
from model.data import process_data

app = FastAPI()

# Load model artifacts
model = joblib.load("model/model.pkl")
encoder = joblib.load("model/encoder.pkl")
lb = joblib.load("model/lb.pkl")

# Categorical features
cat_features = [
    "workclass", "education", "marital-status", "occupation",
    "relationship", "race", "sex", "native-country"
]

class CensusInput(BaseModel):
    age: int
    workclass: str
    fnlgt: int
    education: str
    education_num: int = Field(..., alias="education-num")
    marital_status: str = Field(..., alias="marital-status")
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int = Field(..., alias="capital-gain")
    capital_loss: int = Field(..., alias="capital-loss")
    hours_per_week: int = Field(..., alias="hours-per-week")
    native_country: str = Field(..., alias="native-country")

    class Config:
        schema_extra = {
            "example": {
                "age": 39,
                "workclass": "State-gov",
                "fnlgt": 77516,
                "education": "Bachelors",
                "education-num": 13,
                "marital-status": "Never-married",
                "occupation": "Adm-clerical",
                "relationship": "Not-in-family",
                "race": "White",
                "sex": "Male",
                "capital-gain": 2174,
                "capital-loss": 0,
                "hours-per-week": 40,
                "native-country": "United-States"
            }
        }

@app.get("/")
def root():
    return {"message": "Welcome to the Census Income Prediction API!"}

@app.post("/predict")
def predict(data: CensusInput):
    input_df = pd.DataFrame([data.dict(by_alias=True)])
    X, _, _, _ = process_data(
        input_df, categorical_features=cat_features,
        training=False, encoder=encoder, lb=lb
    )
    pred = inference(model, X)
    label = lb.inverse_transform(pred)[0]
    return {"prediction": label}
