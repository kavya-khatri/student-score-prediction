# # Student Score Prediction System

## Project Overview
This project is a Machine Learning based web application that predicts student final scores using:
- Hours Studied
- Attendance Percentage
- Practice Tests

The application is developed using:
- Python
- Flask
- Scikit-learn
- Docker
- Jenkins CI/CD
- GitHub

---

## Features
- Machine Learning Prediction
- Web Interface using Flask
- Monitoring Script
- Docker Containerization
- Jenkins Pipeline Automation
- GitHub Integration

---

## Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Docker
- Jenkins
- GitHub

---

## Project Structure

student-score-prediction/
│
├── app.py
├── train_model.py
├── monitor.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── dataset.csv
├── model.pkl
└── templates/
    └── index.html

---

## How to Run Project

### Install Dependencies
pip install -r requirements.txt

### Train Model
python train_model.py

### Run Flask App
python app.py

### Run Monitoring Script
python monitor.py

### Docker Build
docker build -t student-score-app .

### Docker Run
docker run -p 5000:5000 student-score-app

---

## GitHub Repository
https://github.com/kavya-khatri/student-score-prediction

---

## Author
Kavya Khatri