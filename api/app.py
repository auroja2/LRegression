from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Allow all origins (or restrict to your frontend URL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Day0 model
model = pickle.load(open("day0.pkl", "rb"))

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
