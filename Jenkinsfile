pipeline {
    agent any

    environment {
        PROJECT_DIR = 'Ticket-Booking-Management-System'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Chaitanya-G15/Ticket-Booking-Management-System.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                dir("${PROJECT_DIR}") {
                    bat 'docker-compose build'
                }
            }
        }

        stage('Run Migrations') {
            steps {
                dir("${PROJECT_DIR}") {
                    bat 'docker-compose run web python manage.py migrate'
                }
            }
        }

        stage('Start Server') {
            steps {
                dir("${PROJECT_DIR}") {
                    bat 'docker-compose up -d'
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful!"
        }
        failure {
            echo "❌ Deployment failed!"
        }
    }
}
