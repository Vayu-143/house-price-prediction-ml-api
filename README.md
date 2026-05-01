# 🏠 House Price Prediction (ML + API + UI)

## 🚀 Live Demo

👉 https://house-price-prediction-ml-api-24crbhankqmzwpvsp7ukgm.streamlit.app/

## 📂 GitHub Repository

👉 https://github.com/Vayu-143/house-price-prediction-ml-api

---

## 📌 Project Overview

This project is an end-to-end Machine Learning application that predicts house prices based on user inputs such as area, number of bedrooms, bathrooms, age of property, and location.

It includes:

* Machine Learning model for prediction
* Flask API (for backend integration)
* Streamlit web interface (for user interaction)
* Deployment on Streamlit Cloud for real-time usage

---

## 🧠 Architecture

Frontend (Streamlit) → ML Model (Scikit-learn Pipeline)

*(Flask API also implemented for backend architecture understanding)*

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Flask
* Streamlit
* Joblib

---

## 🔧 Features

* Predict house prices in real-time
* Interactive UI with sliders and dropdowns
* Clean and responsive design
* End-to-end ML pipeline (preprocessing + model)
* Deployment-ready structure

---

## 📊 Input Example

```json
{
  "area": 2000,
  "bedrooms": 3,
  "bathrooms": 2,
  "age": 5,
  "location": "Bangalore"
}
```

## 📈 Output Example

```json
{
  "predicted_price": 6840000
}
```

---

## ▶️ How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/Vayu-143/house-price-prediction-ml-api.git
cd house-price-prediction-ml-api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train Model

```bash
python -m src.train_model
```

### 4. Run Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```bash
house-price-prediction-ml-api/
│
├── api/                # Flask API (backend)
│   ├── __init__.py
│   └── app.py
│
├── data/               # Dataset
│   └── housing.csv
│
├── images/             # Screenshots & graphs
│   ├── heatmap.png
│   ├── pairplot.png
│   └── prediction.png
│
├── models/             # Saved ML model
│   └── pipeline.pkl
│
├── src/                # Core ML logic
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── predict.py
│   └── train_model.py
│
├── app.py              # Streamlit frontend
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📸 Screenshots

### 🔹 App Interface

![App UI](images/prediction.png)

### 🔹 Data Visualization (Heatmap)

![Heatmap](images/heatmap.png)

### 🔹 Pairplot

![Pairplot](images/pairplot.png)

---

## 💼 Author

**Vayunandan Mishra**

---

## 🎯 Key Learnings

* Built an end-to-end ML system
* Implemented model deployment workflow
* Created REST API using Flask
* Developed interactive frontend using Streamlit
* Debugged real-world integration issues
* Deployed ML application on cloud

---

## 📌 Future Improvements

* Use real-world dataset (Kaggle)
* Add more features (location encoding, amenities)
* Improve model accuracy (XGBoost, tuning)
* Deploy full architecture (API + UI separately)
* Add authentication & user history

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
