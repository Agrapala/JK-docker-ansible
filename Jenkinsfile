pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    parameters {
        string(
            name: 'K8S_IMAGE',
            defaultValue: 'docker.io/samithaagrapala/essay-app:latest',
            description: 'Registry image URL used for Kubernetes deployment'
        )
        string(
            name: 'DOCKERHUB_CREDENTIALS_ID',
            defaultValue: 'dockerhub-creds',
            description: 'Jenkins credentials ID for Docker registry login'
        )
    }

    environment {
        IMAGE_NAME = "essay-app"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: params.DOCKERHUB_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo "$DOCKER_PASS" | docker login docker.io -u "$DOCKER_USER" --password-stdin'
                }
                sh "docker build -t ${params.K8S_IMAGE} ."
                sh "docker push ${params.K8S_IMAGE}"
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh "ansible-playbook -i ansible/inventory.ini ansible/deploy.yml -e k8s_image=${params.K8S_IMAGE}"
            }
        }
        stage('clean ws') {
            steps {
                cleanWs()
            }
        }
    }
}