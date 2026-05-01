import streamlit as st
from src.predict import predict_price

# Page config
st.set_page_config(page_title="House Price Predictor", page_icon="🏠")

# Title
st.title("🏠 House Price Predictor")

# Inputs
area = st.number_input("Area (sq ft)", min_value=500, max_value=5000, value=1200)

bedrooms = st.slider("Bedrooms", 1, 5, 2)

bathrooms = st.slider("Bathrooms", 1, 4, 2)

age = st.slider("Age of Property", 0, 30, 5)

location = st.selectbox(
    "Location",
    ["Bangalore", "Mumbai", "Delhi", "Chennai"]
)

# Predict button
if st.button("Predict"):
    try:
        price = predict_price(area, bedrooms, bathrooms, age, location)

        st.success(f"Estimated Price: ₹ {int(price):,}")

    except Exception as e:
        st.error("Error making prediction")
        st.write(e)