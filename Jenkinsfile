pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Pratik02-07/fastapi-ci-cd.git'
            }
        }

        stage('Install & Test') {
            steps {
                sh '''
                    python3 --version
                    pip3 --version

                    pip3 install -r app/requirements.txt --quiet

                    python3 -c "from app.main import app; print('FastAPI app imports OK')"
                '''
            }
        }

        stage('Info') {
            steps {
                sh '''
                    python3 --version
                    pip3 list | grep -Ei "fastapi|sqlalchemy|uvicorn"
                '''
            }
        }

    }

    post {

        success {
            echo 'Pipeline SUCCESS'
        }

        failure {
            echo 'Pipeline FAILED'
        }

    }
}
