from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import joblib

app = FastAPI()

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# 👇 HTML serve karega
@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r") as f:
        return f.read()

# 👇 prediction API
@app.get("/predict")
def predict(text: str):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)
    return {"prediction": pred[0]}