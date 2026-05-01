import streamlit as st
import requests

st.title("🏠 House Price Predictor (API Version)")

area = st.number_input("Area", 500, 5000)
bedrooms = st.slider("Bedrooms", 1, 5)
bathrooms = st.slider("Bathrooms", 1, 4)
age = st.slider("Age", 0, 30)
location = st.selectbox("Location", ["Bangalore", "Mumbai", "Delhi", "Chennai"])

if st.button("Predict"):
    url = "http://127.0.0.1:5000/predict"

    data = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "location": location
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        price = response.json()["predicted_price"]
        st.success(f"Estimated Price: ₹ {price:,}")
    else:
        st.error("Error connecting to API")