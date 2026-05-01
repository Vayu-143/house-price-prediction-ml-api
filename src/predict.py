import joblib
import pandas as pd
import os

# Correct absolute path
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/pipeline.pkl")

# Load model safely
model = joblib.load(MODEL_PATH)

def predict_price(area, bedrooms, bathrooms, age, location):
    data = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "location": location
    }])

    return model.predict(data)[0]