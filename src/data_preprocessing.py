import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_data():
    return pd.read_csv("data/housing.csv")

def preprocess_data(df):
    X = df.drop("price", axis=1)
    y = df["price"]

    categorical = ["location"]
    numeric = ["area", "bedrooms", "bathrooms", "age"]

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(), categorical),
        ("num", "passthrough", numeric)
    ])

    return X, y, preprocessor