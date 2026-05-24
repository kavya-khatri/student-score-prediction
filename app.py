from flask import Flask, render_template, request
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Create flask app
app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours = float(request.form['hours'])
        attendance = float(request.form['attendance'])
        tests = float(request.form['tests'])

        features = np.array([[hours, attendance, tests]])

        prediction = model.predict(features)[0]

        return render_template(
            'index.html',
            prediction_text=f"Predicted Final Score: {prediction:.2f}"
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"Error: {str(e)}"
        )

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)