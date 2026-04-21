pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        IMAGE_NAME = "essay-app"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                dir('app') {
                    sh 'docker build -t $IMAGE_NAME:latest .'
                }
            }
        }

        stage('Run Local Container') {
            steps {
                sh '''
                    docker rm -f flask-demo || true
                    docker run -d --name flask-demo -p 5000:5000 \
                      -e FLASK_HOST=0.0.0.0 \
                      -e FLASK_PORT=5000 \
                      $IMAGE_NAME:latest
                '''
            }
        }
    }
}