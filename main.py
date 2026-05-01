import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Create folders if not exist
os.makedirs("images", exist_ok=True)
os.makedirs("models", exist_ok=True)

# -------------------------------
# STEP 1: CREATE DATA
# -------------------------------
np.random.seed(42)

data = pd.DataFrame({
    'area': np.random.randint(500, 4000, 200),
    'bedrooms': np.random.randint(1, 5, 200),
    'bathrooms': np.random.randint(1, 4, 200),
    'age': np.random.randint(0, 30, 200),
})

# Create realistic price formula
data['price'] = (
    data['area'] * 3000 +
    data['bedrooms'] * 500000 +
    data['bathrooms'] * 300000 -
    data['age'] * 10000 +
    np.random.randint(-200000, 200000, 200)
)

print("Dataset Preview:")
print(data.head())

# -------------------------------
# STEP 2: EDA
# -------------------------------
sns.pairplot(data)
plt.savefig("images/pairplot.png")
plt.close()

plt.figure(figsize=(8,6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.savefig("images/heatmap.png")
plt.close()

# -------------------------------
# STEP 3: FEATURES
# -------------------------------
X = data.drop("price", axis=1)
y = data["price"]

# -------------------------------
# STEP 4: SPLIT
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# STEP 5: TRAIN MODELS
# -------------------------------
lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100)

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)

# -------------------------------
# STEP 6: PREDICT
# -------------------------------
lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)

# -------------------------------
# STEP 7: EVALUATION FUNCTION
# -------------------------------
def evaluate(name, y_true, y_pred):
    print(f"\n{name} Results:")
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_true, y_pred)))
    print("R2 Score:", r2_score(y_true, y_pred))

evaluate("Linear Regression", y_test, lr_pred)
evaluate("Random Forest", y_test, rf_pred)

# -------------------------------
# STEP 8: VISUALIZATION
# -------------------------------
plt.scatter(y_test, rf_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted (Random Forest)")
plt.savefig("images/prediction.png")
plt.close()

# -------------------------------
# STEP 9: SAVE MODEL
# -------------------------------
joblib.dump(rf, "models/random_forest_model.pkl")

# -------------------------------
# STEP 10: USER INPUT PREDICTION
# -------------------------------
print("\n--- House Price Prediction ---")
area = int(input("Enter area (sqft): "))
bedrooms = int(input("Enter bedrooms: "))
bathrooms = int(input("Enter bathrooms: "))
age = int(input("Enter age of house: "))

sample = np.array([[area, bedrooms, bathrooms, age]])
prediction = rf.predict(sample)

print(f"\nEstimated Price: ₹{int(prediction[0])}")