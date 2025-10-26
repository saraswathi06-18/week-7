pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                // Pull code from your GitHub repo
                git branch: 'main',
                    url: 'https://github.com/saraswathi06-18/week-7.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image for your project
                    sh 'docker build -t week7-app .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop & remove old container if exists
                    sh 'docker stop week7-container || true'
                    sh 'docker rm week7-container || true'

                    // Run new container
                    sh 'docker run -d -p 5000:5000 --name week7-container week7-app'
                }
            }
        }
    }
}
