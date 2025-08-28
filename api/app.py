from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np
from mangum import Mangum  # Required for Vercel serverless

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Can later restrict to your Vercel frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = pickle.load(open("day0.pkl", "rb"))

class InputData(BaseModel):
    values: list[float]

@app.post("/predict")
def predict(data: InputData):
    try:
        X = np.array(data.values).reshape(1, -1)
        prediction = model.predict(X)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

# Required for Vercel serverless
handler = Mangum(app)
