pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/RojalinBeura/jenkins-health-score.git'
'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies using virtual environment...'
                sh '''
                    echo "Creating Python virtual environment..."
                    python3 -m venv venv
                    source venv/bin/activate
                    if [ -f requirements.txt ]; then
                        echo "Installing dependencies..."
                        pip install --no-cache-dir -r requirements.txt
                    else
                        echo "No requirements.txt found"
                    fi
                '''
            }
        }

        stage('Health Scoring') {
            steps {
                echo 'Running health scoring...'
                sh '''
                    source venv/bin/activate
                    python3 score_health.py
                '''
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Running security scan...'
                sh '''
                    source venv/bin/activate
                    bandit -r . || true
                '''
            }
        }

        stage('Report') {
            steps {
                echo 'Generating final report...'
                sh '''
                    echo "Health and Security Scan Completed!"
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed. Please check logs.'
        }
    }
}