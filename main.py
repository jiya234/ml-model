from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()

# ✅ CORS fix
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "ML API is running"}

@app.get("/predict")
def predict(text: str):
    vec = vectorizer.transform([text])
    result = model.predict(vec)
    return {"prediction": result[0]}