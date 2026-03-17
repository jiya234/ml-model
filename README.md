
# 🚀 ML Function Name Predictor
## 🔗 Live Demo  
👉 [ML Function Predictor](https://ml-model-n2eq.onrender.com/)
---

## 📌 Project Overview

This is an **end-to-end Machine Learning web application** that predicts the most suitable **function name** based on a given description.

**Example:**

* Input → *"Adds two integers and returns sum"*
* Output → *"addNumbers"*

---

## 🧠 Tech Stack

* **Frontend:** HTML, JavaScript
* **Backend:** FastAPI
* **Machine Learning:** scikit-learn
* **Deployment:** Render

---

## ⚙️ Features

* ✅ Accepts function description as input
* ✅ Predicts function name using ML model
* ✅ Fast API-based response
* ✅ Fully deployed and accessible online

---

## 🛠️ How It Works

1. User enters a function description
2. Input text is converted using TF-IDF vectorization
3. Trained ML model processes the input
4. Predicted function name is returned and displayed

---

## 🧪 Run Locally


git clone https://github.com/jiya234/ml-model.git
cd ml-model

pip install -r requirements.txt

uvicorn main:app --reload


Open in browser:
(http://127.0.0.1:8000)

---

## 📡 API Endpoint

GET /predict?text=your

