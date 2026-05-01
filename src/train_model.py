import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from src.data_preprocessing import load_data, preprocess_data

# Load data
df = load_data()
X, y, preprocessor = preprocess_data(df)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Models
models = {
    "linear": LinearRegression(),
    "rf": RandomForestRegressor(),
    "xgb": XGBRegressor()
}

best_model = None
best_score = -1

for name, model in models.items():
    pipe = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipe.fit(X_train, y_train)
    score = pipe.score(X_test, y_test)

    print(f"{name} R2 Score:", score)

    if score > best_score:
        best_score = score
        best_model = pipe

# Save best pipeline
joblib.dump(best_model, "models/pipeline.pkl")

print("Best model saved!")