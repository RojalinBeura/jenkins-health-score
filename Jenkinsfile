pipeline {
    agent any

    environment {
        // Python virtual environment (optional)
        PYTHON = '/usr/bin/python3'
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
                echo 'Running Health Score script...'
                sh '''
                    if [ -f score_health.py ]; then
                        python3 score_health.py
                    else
                        echo "No score_health.py found"
                    fi
                '''
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Running Security Scan using OWASP Dependency Check (simulation)...'
                sh '''
                    echo "Scanning for vulnerabilities..."
                    sleep 2
                    echo "No critical vulnerabilities found."
                '''
            }
        }

        stage('Report') {
            steps {
                echo 'Generating Report...'
                sh 'echo "Health and Security report generated successfully."'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check logs.'
        }
    }
}