from fastapi import FastAPI
import numpy as np
import pickle
from pydantic import BaseModel
import os

app = FastAPI()

# Define input format
class CustomerData(BaseModel):
    tenure: float
    monthly_charges: float
    total_charges: float
    gender_male: int
    contract_one_year: int
    contract_two_year: int


@app.post("/predict")
def predict(data: CustomerData):
    try:
        print("STEP 1: Loading model...")

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
        scaler = pickle.load(open(os.path.join(BASE_DIR, "scaler.pkl"), "rb"))

        print("STEP 2: Model loaded")

        input_data = np.array([[ 
            data.tenure,
            data.monthly_charges,
            data.total_charges,
            data.gender_male,
            data.contract_one_year,
            data.contract_two_year
        ]])

        print("STEP 3: Input ready")

        scaled_data = scaler.transform(input_data)
        print("STEP 4: Scaling done")

        prediction = model.predict(scaled_data)[0]
        probability = model.predict_proba(scaled_data)[0][1]

        print("STEP 5: Prediction done")

        return {
            "churn_prediction": int(prediction),
            "probability": float(probability)
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}


@app.get("/")
def home():
    return {"message": "API is running"}
