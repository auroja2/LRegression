# api/predict.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum  # Required for serverless

app = FastAPI()

# Allow CORS for all origins (or restrict to your frontend URL later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your model (put day0.pkl in the same folder as this file)
model = pickle.load(open("day0.pkl", "rb"))

# Request schema
class InputData(BaseModel):
    values: list[float]

@app.get("/")
def home():
    return {"message": "API is running!"}

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