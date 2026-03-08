import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# 1 load dataset
df = pd.read_csv("functions_dataset.csv")

# 2 combine metadata columns
df["input_text"] = (
    df["description"] + " " +
    df["parameters"] + " " +
    df["return_type"] + " " +
    df["keywords"]
)

# 3 input and output
X = df["input_text"]
y = df["function_name"]

# 4 text → numbers
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# 5 split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# 6 train model
model = MultinomialNB()
model.fit(X_train, y_train)

print("Model training completed")

# 7 accuracy check
pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print("Model Accuracy:", accuracy)

# 8 inference demo
test_input = "Adds two integers int a int b return int keywords add sum"

test_vec = vectorizer.transform([test_input])

prediction = model.predict(test_vec)

print("Predicted function:", prediction[0])

# 9 save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved successfully")