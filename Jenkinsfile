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
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train ML Model') {
            steps {
                bat 'python train_model.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-score-app .'
            }
        }

    }
}