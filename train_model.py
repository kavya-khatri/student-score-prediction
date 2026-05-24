import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset
df = pd.read_csv("dataset.csv")

# Features and target
X = df[['Hours_Studied', 'Attendance', 'Practice_Tests']]
y = df['Final_Score']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Trained Successfully")
print("MAE:", mae)
print("R2 Score:", r2)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")