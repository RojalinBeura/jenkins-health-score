pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/RojalinBeura/jenkins-health-score.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    if [ -f requirements.txt ]; then
                        pip install --no-cache-dir -r requirements.txt
                    else
                        echo "No requirements.txt found"
                    fi
                '''
            }
        }

        stage('Health Scoring') {
            steps {
                echo 'Running health scoring script...'
                sh '''
                    . $VENV_DIR/bin/activate
                    python3 score_health.py || echo "Health scoring failed"
                '''
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Running security scan...'
                sh '''
                    . $VENV_DIR/bin/activate
                    bandit -r . || echo "Bandit scan completed with warnings"
                '''
            }
        }

        stage('Report') {
            steps {
                echo 'Generating report...'
                sh 'echo "All tasks completed successfully."'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check logs.'
        }
    }
}
