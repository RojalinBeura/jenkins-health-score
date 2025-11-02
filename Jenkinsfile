pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/RojalinBeura/jenkins-health-score.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
                sh 'python --version'
            }
        }

        stage('Health Scoring') {
            steps {
                sh 'python score_health.py'
            }
        }

        stage('Security Scan') {
            steps {
                dependencyCheck additionalArguments: '--scan .', odcInstallation: 'OWASPDC'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }

        stage('Report') {
            steps {
                echo 'Build and security analysis complete!'
            }
        }
    }
}