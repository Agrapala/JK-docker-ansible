pipeline {
    agent any

    environment {
        IMAGE_NAME = "yourdockerhubusername/flask-demo"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/my-devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('app') {
                    sh 'docker build -t $IMAGE_NAME:latest .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME:latest'
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i ansible/inventory.ini ansible/deploy.yml'
            }
        }
    }
}