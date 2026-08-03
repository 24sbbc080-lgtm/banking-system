pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/your-username/loan-eligibility.git'
            }
        }

        stage('Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python loan_eligibility.py --test'
            }
        }
    }

    post {
        success {
            echo 'Loan Eligibility Tests Passed!'
        }

        failure {
            echo 'Tests Failed!'
        }
    }
}