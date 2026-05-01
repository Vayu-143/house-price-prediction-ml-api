from flask import Flask, request, jsonify
from src.predict import predict_price

app = Flask(__name__)

@app.route("/")
def home():
    return "House Price Prediction API"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    price = predict_price(
        data["area"],
        data["bedrooms"],
        data["bathrooms"],
        data["age"],
        data["location"]
    )

    return jsonify({"predicted_price": int(price)})

if __name__ == "__main__":
    app.run(debug=True)