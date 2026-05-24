pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning GitHub Repository'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\kavya\\anaconda3\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Train ML Model') {
            steps {
                bat '"C:\\Users\\kavya\\anaconda3\\python.exe" train_model.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-score-app .'
            }
        }

    }
}