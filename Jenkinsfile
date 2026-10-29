pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -3 --version'
                bat 'py -3 -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat '.venv\\Scripts\\python.exe monitor.py'
            }
        }
    }

    post {
        success {
            echo 'UAT Pipeline completed successfully.'
        }

        failure {
            echo 'UAT Pipeline failed. Check the console output.'
        }
    }
}