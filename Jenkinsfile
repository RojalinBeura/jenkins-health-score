pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t healthscore-app .'
            }
        }

        stage('Run OWASP Dependency Check') {
            steps {
                dependencyCheck additionalArguments: '--scan .'
            }
        }

        stage('Run Health Scoring Script') {
            steps {
                sh 'python3 score_health.py'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportDir: 'reports',
                    reportFiles: 'index.html',
                    reportName: 'Health & Security Score Report'
                ])
            }
        }
    }
}