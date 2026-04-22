pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        IMAGE_NAME = "essay-app"
        K8S_IMAGE = "docker.io/your-user/essay-app:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $K8S_IMAGE .'
                sh 'docker push $K8S_IMAGE'
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i ansible/inventory.ini ansible/deploy.yml -e k8s_image=$K8S_IMAGE'
            }
        }
        stage('clean ws') {
            steps {
                cleanWs()
            }
        }
    }
}